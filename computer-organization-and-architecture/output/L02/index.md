---
schema_version: 1
type: "lecture-index"
title: "L02 性能与指令集"
course: "computer-organization-and-architecture"
lecture: "L02"
---

# L02 性能与指令集

[课程目录](../index.md)

性能比较从任务和指标出发：用执行时间方程找出指令数、CPI与时钟周期的影响，再用Amdahl定律计算局部优化收益。RISC-V部分把指令语义、二进制字段、字节地址、调用约定和原子更新连接起来，练习从代码推算数据与控制流。

## 章节导航

- [01 系统设计的约束](chapters/section-1.md)
- [02 性能指标与执行时间](chapters/section-2.md)
- [03 性能汇总与优化收益](chapters/section-3.md)
- [04 指令集与RISC设计](chapters/section-4.md)
- [05 寄存器与指令编码](chapters/section-5.md)
- [06 数据访问与立即数](chapters/section-6.md)
- [07 控制流与过程调用](chapters/section-7.md)
- [08 原子更新与同步](chapters/section-8.md)

## 本讲小结

评估性能要使用实际工作量和动态执行时间：频率、IPC或核心数只能解释其中一部分，优化收益还受未优化时间、数据供给、功耗与成本限制。理解ISA时，把数据宽度、寄存器编号和指令编码分开；执行代码时依次追踪源值、立即数、有效地址及下一PC。跨调用保存按ABI分工，LR/SC更新则按最新保留、覆盖范围、冲突写入和SC结果判断。

## 来源

- L02.docx-DOCX body 1-50
- L02.docx-DOCX body 51-90
- L02.docx-DOCX body 91-123
- L02.docx-DOCX body 124-160
- L02.pdf-PDF p.3
- L02.pdf-PDF p.4
- L02.pdf-PDF p.5
- L02.pdf-PDF p.6
- L02.pdf-PDF p.7
- L02.pdf-PDF p.8
- L02.pdf-PDF p.9
- L02.pdf-PDF p.10
- L02.pdf-PDF p.11
- L02.pdf-PDF p.12
- L02.pdf-PDF p.13
- L02.pdf-PDF p.14
- L02.docx-DOCX body 161-196
- L02.docx-DOCX body 197-243
- L02.pdf-PDF p.15
- L02.pdf-PDF p.16
- L02.pdf-PDF p.17
- L02.pdf-PDF p.18
- L02.pdf-PDF p.19
- L02.pdf-PDF p.20
- L02.pdf-PDF p.21
- L02.pdf-PDF p.22
- L02.pdf-PDF p.23
- L02.pdf-PDF p.24
- L02.pdf-PDF p.25
- L02.pdf-PDF p.26
- L02.pdf-PDF p.27
- L02.pdf-PDF p.28
- L02.docx-DOCX body 244-280
- L02.docx-DOCX body 281-324
- L02.pdf-PDF p.30
- L02.pdf-PDF p.31
- L02.pdf-PDF p.32
- L02.pdf-PDF p.33
- L02.pdf-PDF p.34
- L02.pdf-PDF p.35
- L02.pdf-PDF p.36
- L02.pdf-PDF p.37
- L02.pdf-PDF p.38
- L02.pdf-PDF p.39
- L02.pdf-PDF p.40
- L02.pdf-PDF p.41
- L02.pdf-PDF p.42
- L02.pdf-PDF p.43
- L02.pdf-PDF p.44
- L02.pdf-PDF p.73
- L02.docx-DOCX body 325-371
- L02.docx-DOCX body 372-407
- L02.docx-DOCX body 408-450
- L02.docx-DOCX body 565-612
- L02.pdf-PDF p.45
- L02.pdf-PDF p.46
- L02.pdf-PDF p.47
- L02.pdf-PDF p.48
- L02.pdf-PDF p.49
- L02.pdf-PDF p.50
- L02.pdf-PDF p.51
- L02.pdf-PDF p.70
- L02.docx-DOCX body 451-490
- L02.pdf-PDF p.52
- L02.pdf-PDF p.53
- L02.pdf-PDF p.54
- L02.pdf-PDF p.55
- L02.pdf-PDF p.56
- L02.pdf-PDF p.57
- L02.pdf-PDF p.58
- L02.pdf-PDF p.71
- L02.pdf-PDF p.72
- L02.docx-DOCX body 491-525
- L02.pdf-PDF p.59
- L02.pdf-PDF p.60
- L02.pdf-PDF p.61
- L02.pdf-PDF p.62
- L02.pdf-PDF p.63
- L02.pdf-PDF p.64
- L02.pdf-PDF p.65
- L02.docx-DOCX body 526-564
- L02.pdf-PDF p.66
- L02.pdf-PDF p.67
- L02.pdf-PDF p.68
- L02.pdf-PDF p.69
