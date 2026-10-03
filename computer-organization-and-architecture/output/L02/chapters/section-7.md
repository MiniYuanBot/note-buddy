---
schema_version: 1
type: "course-note"
title: "07 控制流与过程调用"
course: "computer-organization-and-architecture"
lecture: "L02"
section: "section-7"
---

# 07 控制流与过程调用

[本讲目录](../index.md) · [课程目录](../../index.md) · [上一节：06 数据访问与立即数](section-6.md) · [下一节：08 原子更新与同步](section-8.md)

## 条件分支

`beq`在两个源寄存器相等时跳转，`bne`在不相等时跳转；条件不满足则执行下一条指令。[^s1p59]

```asm
beq rs1, rs2, L1
bne rs1, rs2, L1
```

若i、j、h分别放在x22、x23、x19中，`if (i==j) h=i+j;`可写为：

```asm
bne x22, x23, L1    # 不相等就跳过赋值
add x19, x22, x23   # 相等时执行h=i+j
L1:
    # 后续代码
```

两条分支都比较源寄存器的值。[^s1p59][^s2b13]

## PC相对目标与偏移

B格式分支以**分支指令自身的地址**为基准：

$$
PC_{target}=PC_{branch}+\operatorname{signext}(imm[12:1],0)
$$

最低位隐含为0，12个编码位组成13位有符号字节偏移，范围为$[-4096,4094]$字节、粒度为2字节。它通常用于局部控制流。[^s1p60][^s1p72] [RISC-V分支规范](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)

例如，分支位于`0x1000`，目标标签位于`0x1010`，偏移为16字节。成立时下一PC为`0x1010`；不成立时，当前32位指令的下一PC为`0x1004`。

只有基础32位指令的环境要求指令地址4字节对齐；支持16位指令的相应扩展环境允许2字节对齐。[指令对齐规则](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)

## JAL与JALR

跳转并链接（jump and link）同时改变控制流并保存返回位置。对这里的32位指令，链接地址为该指令地址加4。[^s1p61]

| 指令 | 链接值 | 目标 |
| --- | --- | --- |
| `jal rd,target` | `rd = old_PC + 4` | `old_PC + signed_J_offset` |
| `jalr rd,imm(rs1)` | `rd = old_PC + 4` | `(old_rs1 + signext(imm12)) & ~1` |

JAL采用J格式，偏移范围为$[-2^{20},2^{20}-2]$字节、2字节粒度。JALR采用I格式，其立即数是$[-2048,2047]$字节，目标相加后清除bit 0，仍需满足执行环境的指令对齐。[RISC-V跳转规范](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)

常见用途如下：

```asm
jal  x1, ProcedureAddress   # 调用，ra=x1保存返回地址
jalr x0, 0(x1)             # 返回到ra，链接写到x0被丢弃
jal  x0, Label             # 无条件跳转，不保留返回地址
```

用x0作rd会丢弃链接。[^s1p61][^s1p62]

### 源寄存器与目的寄存器相同

JALR用旧rs1计算目标，并用旧PC计算链接，即使rd=rs1也遵循这一规则。在`PC=0x1000`、`x1=0x2000`时：

```asm
jalr x1, 4(x1)
```

目标为`0x2004`，最终x1保存`0x1004`。[^s2b15] [JALR定义](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)

### 高低部构造远跳转

先用LUI形成符号扩展的32位地址高部，再由JALR加上有符号低部。例如：

```asm
lui  x5, 0x12345
jalr x1, 0x678(x5)    # 目标0x12345678，链接保存到x1
```

目标`0x12345678`满足4字节对齐。[^s1p62]

低12位若作为无符号数超过2047，须向高部进位：令高部增加1、低部减4096，仍表示同一地址。例如低部2342应改为$-1754$，高部相应加1；目标还须满足前述指令对齐。[^s1p62] [JALR立即数规则](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)

## 调用者与被调用者保存

函数调用约定规定参数、返回结果和跨调用保留值如何使用寄存器。调用者（caller）保存指“调用者如果之后仍需该值，就应在调用前保护它”；被调用者（callee）保存指“被调用者若要改用该寄存器，须先保存旧值，并在返回前恢复”。[^s1p63][^s2b14]

| 寄存器 | 保存责任 | 跨调用规则 |
| --- | --- | --- |
| ra，x1 | caller | 嵌套调用会写入新链接；原返回地址需由当前函数保护 |
| t0–t6 | caller | 临时值可被被调用者改写 |
| a0–a7 | caller | 用于参数/结果，调用后原值不保证保留 |
| s0–s11 | callee | 返回时须恢复调用前的值 |
| sp，x2 | callee | 返回时恢复调用前栈位置 |
| gp、tp | 通常不改 | 全局/线程指针按约定保持用途 |
| x0 | 无需保存 | 恒为0 |

递归和嵌套调用需要保存各次调用的返回地址，可通过内存栈保存。[^s2b14]

## 栈与栈帧

栈采用后进先出（LIFO），向低地址增长。分配空间时减小sp，再存入数据；释放时先读回，再增大sp。RV64保存一个完整整数寄存器需要8字节。[^s1p64]

**补充解释**：标准RV64整数ABI要求sp在过程入口及执行期间保持16字节对齐。下例分配16字节栈帧，保存ra和s0；这是调用约定要求。[RISC-V标准ABI](https://riscv-non-isa.github.io/riscv-elf-psabi-doc/)

```asm
addi sp, sp, -16
sd   ra, 8(sp)
sd   s0, 0(sp)
# 使用s0；若调用其他函数，ra槽位保护原返回地址
# ...
ld   s0, 0(sp)
ld   ra, 8(sp)
addi sp, sp, 16
jalr x0, 0(ra)
```

栈帧可容纳额外参数、返回地址、旧帧指针、局部变量、临时值及保存的寄存器。sp随分配和释放移动；可选帧指针fp提供相对稳定的基准，以固定偏移访问局部量。[^s1p65][^s2b14]

一个典型内存布局包含保留区、代码区text、静态数据、动态数据和栈。PC指向代码，gp用于全局/静态数据访问，动态分配区域与栈分别向可用地址空间增长；具体起始地址由执行环境决定。[^s1p65]

## 应用问答

**问：函数A把临时结果保存在t0后调用B，返回后还要用它，应由谁保存？**

答：A应在调用前保存t0，或改放到按约定保护的存储位置；B可以改写t0。[^s1p63]

**问：分支地址为`0x2000`，目标为`0x1FF0`，偏移是多少？**

答：$\texttt{0x1FF0}-\texttt{0x2000}=-16$字节；基准是分支自身PC。

来源：[^s1p59] [^s1p60] [^s1p61] [^s1p62] [^s1p63] [^s1p64] [^s1p65] [^s1p72] [^s2b13] [^s2b14] [^s2b15]

[^s1p59]: L02.pdf-PDF p.59
[^s1p60]: L02.pdf-PDF p.60
[^s1p61]: L02.pdf-PDF p.61
[^s1p62]: L02.pdf-PDF p.62
[^s1p63]: L02.pdf-PDF p.63
[^s1p64]: L02.pdf-PDF p.64
[^s1p65]: L02.pdf-PDF p.65
[^s1p72]: L02.pdf-PDF p.72
[^s2b13]: L02.docx-DOCX body 491-525
[^s2b14]: L02.docx-DOCX body 526-564
[^s2b15]: L02.docx-DOCX body 565-612


[本讲目录](../index.md) · [课程目录](../../index.md) · [上一节：06 数据访问与立即数](section-6.md) · [下一节：08 原子更新与同步](section-8.md)
