#!/usr/bin/env python3
"""直接覆盖本项目 DOCX，删除图片及其前后相邻的连续空段落。

支持 macOS / Windows，要求 Python 3.9+，无需第三方依赖或安装 Word。

Windows：
    py -3 remove_docx_images.py
    py -3 remove_docx_images.py operating-system/input

macOS：
    python3 remove_docx_images.py
    python3 remove_docx_images.py operating-system/input

默认递归扫描脚本所在的项目目录，跳过 workspace、虚拟环境和旧的去图结果。
路径参数均相对于项目根目录，只处理本项目内的文件。
处理成功后直接覆盖原文档，不生成副本，无需 --overwrite 参数。
先写入临时文件并关闭原文档，再替换原文件；无可删除图片时保持文件不变。
空行按空段落处理，不修改段前段后间距；混排时保留同段文字。
"""

from __future__ import annotations

import argparse
import os
import posixpath
import stat
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote
from xml.dom import Node, minidom
from zipfile import ZipFile


PROJECT_ROOT = Path(__file__).resolve().parent
SKIP_DIRECTORIES = {
    ".git", ".obsidian", ".venv", "venv", "__pycache__", "node_modules", "workspace", "去图结果"
}


W = {
    "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "http://purl.oclc.org/ooxml/wordprocessingml/main",
}
PIC = {
    "http://schemas.openxmlformats.org/drawingml/2006/picture",
    "http://purl.oclc.org/ooxml/drawingml/picture",
}
R = {
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "http://purl.oclc.org/ooxml/officeDocument/relationships",
}
V = "urn:schemas-microsoft-com:vml"
MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"


def is_w(node: Node, name: str) -> bool:
    return node.nodeType == Node.ELEMENT_NODE and node.namespaceURI in W and node.localName == name


def elements(node: Node) -> list:
    return [child for child in node.childNodes if child.nodeType == Node.ELEMENT_NODE]


def ancestor(node: Node, predicate):
    current = node.parentNode
    while current is not None:
        if predicate(current):
            return current
        current = current.parentNode
    return None


def text_of(node: Node) -> str:
    return "".join(
        child.data for child in node.childNodes
        if child.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE)
    )


def has_text(node: Node) -> bool:
    return any(is_w(child, "t") and text_of(child).strip() for child in node.getElementsByTagName("*"))


def is_blank(node: Node) -> bool:
    """只把可确认无内容的段落视为空白，保留分页、分节、编号、域及其他对象。"""
    if node.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE):
        return not node.data.strip()
    if node.nodeType in (Node.COMMENT_NODE, Node.PROCESSING_INSTRUCTION_NODE):
        return True
    if node.nodeType != Node.ELEMENT_NODE:
        return False
    if node.namespaceURI in W:
        if node.localName == "pPr":
            protected = {"sectPr", "pageBreakBefore", "numPr", "pBdr"}
            return not any(
                child.namespaceURI in W and child.localName in protected
                for child in node.getElementsByTagName("*")
            )
        if node.localName == "rPr":
            return True
        if node.localName == "br":
            kind = next((node.getAttributeNS(ns, "type") for ns in W if node.hasAttributeNS(ns, "type")), "")
            return kind in ("", "textWrapping")
        if node.localName not in {
            "p", "r", "t", "tab", "cr", "hyperlink", "pict", "proofErr", "lastRenderedPageBreak"
        }:
            return False
    elif not (node.namespaceURI == MC and node.localName in {"AlternateContent", "Choice", "Fallback"}):
        return False
    return all(is_blank(child) for child in node.childNodes)


def sibling_element(node: Node, backwards: bool):
    current = node.previousSibling if backwards else node.nextSibling
    while current is not None and current.nodeType != Node.ELEMENT_NODE:
        current = current.previousSibling if backwards else current.nextSibling
    return current


def clean_xml(document: minidom.Document) -> tuple[int, int]:
    pictures = [
        node for node in document.getElementsByTagName("*")
        if (node.namespaceURI in PIC and node.localName == "pic")
        or (node.namespaceURI == V and node.localName == "imagedata")
    ]
    anchors = set()
    removed_images = 0
    for picture in pictures:
        if ancestor(picture, lambda n: n is document) is None:
            continue
        # 嵌入对象的预览图属于该对象，保留它们。
        if ancestor(picture, lambda n: is_w(n, "object")) is not None:
            continue
        target = picture
        if picture.namespaceURI in PIC:
            drawing = ancestor(picture, lambda n: is_w(n, "drawing"))
            graphic_data = ancestor(
                picture,
                lambda n: n.nodeType == Node.ELEMENT_NODE
                and n.localName == "graphicData"
                and n.namespaceURI in {
                    "http://schemas.openxmlformats.org/drawingml/2006/main",
                    "http://purl.oclc.org/ooxml/drawingml/main",
                },
            )
            if drawing is not None and graphic_data is not None:
                if graphic_data.getAttribute("uri") in PIC and not has_text(drawing):
                    target = drawing
        else:
            shape = ancestor(
                picture,
                lambda n: n.namespaceURI == V and n.localName in {"shape", "rect", "roundrect", "oval"},
            )
            if shape is not None and not has_text(shape):
                target = shape
        paragraph = ancestor(target, lambda n: is_w(n, "p"))
        if paragraph is not None:
            anchors.add(paragraph)
        parent = target.parentNode
        parent.removeChild(target)
        removed_images += 1
        # 清理失去内容的旧式图片容器和兼容容器。
        current = parent
        while current is not None and not is_w(current, "p"):
            outer = current.parentNode
            empty_pict = is_w(current, "pict") and not elements(current)
            empty_alternate = (
                current.namespaceURI == MC and current.localName == "AlternateContent"
                and all(n.namespaceURI == MC for n in current.getElementsByTagName("*"))
            )
            if outer is not None and (empty_pict or empty_alternate):
                outer.removeChild(current)
            current = outer

    doomed = set()
    for paragraph in anchors:
        if is_blank(paragraph):
            doomed.add(paragraph)
        for backwards in (True, False):
            neighbor = sibling_element(paragraph, backwards)
            while neighbor is not None and is_w(neighbor, "p") and is_blank(neighbor):
                doomed.add(neighbor)
                neighbor = sibling_element(neighbor, backwards)
    # Word 要求表格单元格末尾保留一个段落。
    for paragraph in list(doomed):
        parent = paragraph.parentNode
        if is_w(parent, "tc") and elements(parent)[-1] is paragraph:
            doomed.discard(paragraph)
    for paragraph in doomed:
        paragraph.parentNode.removeChild(paragraph)
    return removed_images, len(doomed)


def serialize(document: minidom.Document) -> bytes:
    return document.toxml(encoding="UTF-8", standalone=document.standalone)


def relationship_source(name: str) -> str:
    if name == "_rels/.rels":
        return ""
    folder, filename = posixpath.split(name)
    return posixpath.join(posixpath.dirname(folder), filename[:-5])


def resolve_target(source: str, target: str) -> str:
    target = unquote(target.split("#", 1)[0])
    if target.startswith("/"):
        return posixpath.normpath(target).lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(source), target))


def process_docx(source: Path) -> tuple[int, int, int]:
    """清理后原位替换文档；失败时保留原文件，无变化时不重写。"""
    if source.is_symlink():
        raise ValueError("不处理符号链接文件")
    source = source.resolve()
    if not source.is_relative_to(PROJECT_ROOT):
        raise ValueError("只处理本项目内的文件")
    updates = {}
    references = {}
    images = blanks = 0
    temporary = None
    try:
        with ZipFile(source) as archive:
            names = set(archive.namelist())
            if "word/document.xml" not in names or "[Content_Types].xml" not in names:
                raise ValueError("不是有效的 Word DOCX 文档")
            for name in names:
                if not (name.startswith("word/") and name.endswith((".xml", ".vml"))):
                    continue
                document = minidom.parseString(archive.read(name))
                try:
                    count, deleted = clean_xml(document)
                    if count:
                        updates[name] = serialize(document)
                        references[name] = {
                            attr.value
                            for node in document.getElementsByTagName("*")
                            for attr in node.attributes.values()
                            if attr.namespaceURI in R
                        }
                        images += count
                        blanks += deleted
                finally:
                    document.unlink()

            candidates, still_referenced = set(), set()
            for name in names:
                if not name.endswith(".rels"):
                    continue
                document = minidom.parseString(archive.read(name))
                try:
                    source_part = relationship_source(name)
                    changed = False
                    for rel in list(document.getElementsByTagNameNS("*", "Relationship")):
                        external = rel.getAttribute("TargetMode") == "External"
                        target = resolve_target(source_part, rel.getAttribute("Target"))
                        unused_image = (
                            source_part in references
                            and rel.getAttribute("Type").endswith("/image")
                            and rel.getAttribute("Id") not in references[source_part]
                        )
                        if unused_image:
                            rel.parentNode.removeChild(rel)
                            changed = True
                            if not external:
                                candidates.add(target)
                        elif not external:
                            still_referenced.add(target)
                    if changed:
                        updates[name] = serialize(document)
                finally:
                    document.unlink()
            deleted_media = (candidates - still_referenced) & names
            if deleted_media:
                document = minidom.parseString(archive.read("[Content_Types].xml"))
                try:
                    changed = False
                    for override in list(document.getElementsByTagNameNS("*", "Override")):
                        if unquote(override.getAttribute("PartName")).lstrip("/") in deleted_media:
                            override.parentNode.removeChild(override)
                            changed = True
                    if changed:
                        updates["[Content_Types].xml"] = serialize(document)
                finally:
                    document.unlink()

            if not updates:
                return 0, 0, 0
            with tempfile.NamedTemporaryFile(dir=source.parent, prefix=".docx-clean-", suffix=".tmp", delete=False) as file:
                temporary = Path(file.name)
            with ZipFile(temporary, "w") as result:
                result.comment = archive.comment
                for info in archive.infolist():
                    if info.filename not in deleted_media:
                        data = updates.get(info.filename)
                        result.writestr(info, archive.read(info.filename) if data is None else data)
        # macOS 等 POSIX 系统上，保留原权限，避免临时文件的 0600 权限影响共享。
        if os.name == "posix":
            os.chmod(temporary, stat.S_IMODE(source.stat().st_mode))
        # 同目录替换适用于两端；Windows 要求先关闭原文档及临时 ZIP。
        os.replace(temporary, source)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return images, blanks, len(deleted_media)


def find_documents(folder: Path, recursive: bool = True) -> list[Path]:
    files = []
    for current, directories, filenames in os.walk(folder):
        directories[:] = [name for name in directories if name not in SKIP_DIRECTORIES]
        for name in filenames:
            candidate = Path(current) / name
            if (
                name.lower().endswith(".docx") and not name.startswith(("~$", "._"))
                and not candidate.is_symlink() and candidate.resolve().is_relative_to(PROJECT_ROOT)
            ):
                files.append(candidate)
        if not recursive:
            break
    return sorted(files)


def main() -> int:
    # 重定向输出时，Windows 的旧编码可能无法表示中文或特殊文件名。
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", nargs="?", type=Path, default=Path("."), help="项目内待处理的文件夹，默认：整个项目")
    parser.add_argument("-r", "--recursive", action=argparse.BooleanOptionalAction, default=True, help="递归扫描，默认开启；--no-recursive 仅扫描指定文件夹")
    args = parser.parse_args()
    folder = (PROJECT_ROOT / args.folder.expanduser()).resolve()
    if not folder.is_relative_to(PROJECT_ROOT):
        parser.error("只处理本项目内的文件夹")
    if not folder.is_dir():
        parser.error(f"文件夹不存在：{folder}")
    files = find_documents(folder, args.recursive)
    if not files:
        print("没有找到可处理的 .docx 文件。")
        return 0
    success = skipped = failed = 0
    for source in files:
        relative = source.relative_to(PROJECT_ROOT)
        try:
            images, blanks, media = process_docx(source)
            if images == 0:
                print(f"[跳过] {relative}：没有可删除的图片，原文件未改动")
                skipped += 1
                continue
            print(f"[已覆盖] {relative}：删除 {images} 个图片节点、{blanks} 个空段落、{media} 个图片文件")
            success += 1
        except Exception as error:
            print(f"[失败] {relative}：{error}", file=sys.stderr)
            failed += 1
    print(f"\n已覆盖 {success} 个，跳过 {skipped} 个，失败 {failed} 个。")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
