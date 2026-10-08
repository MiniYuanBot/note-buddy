# 模拟小测 01：基础概念与性能入门

范围：前三课（L01 体系结构导论、L02 性能与 RISC-V 指令集、L03 ALU 与基础架构）。建议用时：40 分钟；满分：100 分。

答题约定：除题干另有说明，采用 RV64、32 位非压缩指令、按字节编址和小端序；涉及浮点或原子指令时，假定具备相应扩展。流水线题采用顺序发射的 IF—ID—EX—MEM—WB 五级教学模型，具体转发与时序条件以题干为准。计算结果可保留三位有效数字。

## 一、判断题（共 8 题，每题 2 分，共 16 分）

在括号中填写“对”或“错”。

1. 实现同一 ISA 的两款处理器，可以采用不同的微架构。（　）

2. 处理器计算速度与主存访问速度之间的差距，是内存墙问题的重要来源。（　）

3. 比较同一个程序在两台机器上的运行情况时，主频较高的机器一定具有更短的 CPU 执行时间。（　）

4. RV64 中的“64”表示每条指令都占 64 位。（　）

5. 执行 `addi x0, x0, 7` 后，`x0` 的值仍为 0。（　）

6. 一位全加器的本位和等于三个输入位的异或。（　）

7. 把单周期处理器改成流水线后，每条指令从开始到完成的延迟一定缩短。（　）

8. 在五级流水线中，只要提供 ALU 操作数转发，就能消除所有数据冒险引起的停顿。（　）

## 二、单项选择题（共 8 题，每题 4 分，共 32 分）

每题只有一个正确选项。

**9.** 按“逻辑—状态—互连”的分类，用于保存中间结果的寄存器主要属于哪一类？

- A. 逻辑
- B. 状态
- C. 互连
- D. 应用

**10.** 采用 $P\approx\frac12 CV^2Af$，保持 $C,V,A$ 不变，将频率提高到原来的 2 倍，动态功耗变为原来的多少倍？

- A. $1/2$
- B. $1$
- C. $2$
- D. $4$

**11.** 某程序动态执行 $10^9$ 条指令，平均 $\mathrm{CPI}=1.5$，时钟频率为 $3\,\mathrm{GHz}$。CPU 执行时间是多少？

- A. $0.5\,\mathrm{s}$
- B. $1.5\,\mathrm{s}$
- C. $2\,\mathrm{s}$
- D. $4.5\,\mathrm{s}$

**12.** RISC-V R 型指令的目的寄存器字段 `rd` 占多少位？

- A. 3 位
- B. 6 位
- C. 7 位
- D. 5 位

**13.** 已知 `x6` 保存地址 `0x1000`。执行 `ld x5, 24(x6)` 时，访问的起始地址是哪一个？

- A. `0x1003`
- B. `0x1018`
- C. `0x10C0`
- D. `0x1024`

**14.** 十进制 $-5$ 的 4 位二进制补码是哪一个？

- A. `0101`
- B. `1010`
- C. `1011`
- D. `1101`

**15.** 对本课程支持 R 型、`ld`、`sd`、`beq` 的单周期数据通路，时钟周期必须满足哪项要求？

- A. 等于各类指令执行时间的平均值
- B. 由最快指令的路径决定
- C. 对不同指令临时使用不同长度
- D. 容纳最慢指令的完整组合路径及状态元件时序开销

**16.** 五级流水线具有到 EX 的完整转发，加载数据在 MEM 末产生，其他冒险忽略。以下两条指令之间至少需要插入几个气泡？

```asm
ld  x5, 0(x6)
add x7, x5, x8
```

- A. 1 个
- B. 0 个
- C. 2 个
- D. 3 个

## 三、填空题（共 6 题，每题 6 分，共 36 分）

同一题有多个空时，每空均分；等价表达均可。

17. 按本课程系统栈的划分，计算机体系结构覆盖的中间三层，自上而下为 ________、________、________。

18. 时钟频率为 $2.5\,\mathrm{GHz}$ 时，时钟周期为 ________ $\mathrm{ns}$。

19. 某程序有三类指令，动态执行占比分别为 $50\%,25\%,25\%$，各类 CPI 分别为 $1,2,4$。平均 CPI 为 ________。

20. IEEE 754 单精度格式中，符号、指数、小数字段分别占 ________、________、________ 位。

21. 五级流水线开始时为空，无停顿地执行 10 条指令，从第一条进入 IF 到最后一条完成 WB，共需 ________ 个周期。

22. 忽略时钟偏斜，已知寄存器输出延迟 $T_{\mathrm{clk\_q}}=30\,\mathrm{ps}$、最长组合路径延迟 $450\,\mathrm{ps}$、建立时间 $20\,\mathrm{ps}$。最短时钟周期为 ________ $\mathrm{ps}$，对应最高频率为 ________ $\mathrm{GHz}$。

## 四、简答题（共 1 题，16 分）

**23.** 两台机器 A、B 执行同一程序，动态指令数均为 $1.2\times10^9$。A 的平均 $\mathrm{CPI}=1.2$、频率为 $2\,\mathrm{GHz}$；B 的平均 $\mathrm{CPI}=2.0$、频率为 $3\,\mathrm{GHz}$。忽略 I/O 等待。

- （1）写出 CPU 执行时间公式，并计算 A、B 的执行时间。（6 分）
- （2）哪台机器更快？给出较快机器相对较慢机器的性能之比。（4 分）
- （3）结合本例，解释为什么不能仅用主频评价性能。（6 分）

---

## 参考答案与解析

### 一、判断题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 1 | 对 | ISA 规定软件可见的接口与指令行为，微架构规定具体实现。 [L01·01](../computer-organization-and-architecture/output/L01/chapters/01-architecture-definition-and-system-stack.md) |
| 2 | 对 | 计算部件变快，若数据供给跟不上，处理器就会等待。 [L01·04](../computer-organization-and-architecture/output/L01/chapters/04-system-block-diagram-and-memory-wall.md) |
| 3 | 错 | 还需比较动态指令数和 CPI，不能只看主频。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) |
| 4 | 错 | 它表示整数寄存器宽度等字长特征；本卷采用的非压缩基本指令长 32 位。 [L02·05](../computer-organization-and-architecture/output/L02/chapters/05-risc-v-overview-and-instruction-formats.md) |
| 5 | 对 | `x0` 恒为 0，对它的写入被丢弃。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md) |
| 6 | 对 | $S=A\oplus B\oplus C_{\mathrm{in}}$。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md) |
| 7 | 错 | 流水线主要提高吞吐量；单条指令延迟还受级数、级间寄存器开销和阶段不平衡影响。 [L03·06](../computer-organization-and-architecture/output/L03/chapters/06-pipeline-design-and-performance.md) |
| 8 | 错 | 例如紧邻的 load-use：加载结果到 MEM 末才可用，下一条指令原本在同周期 EX 就需要它。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |

### 二、单项选择题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 9 | B | 寄存器保存数据与当前状态。 [L01·02](../computer-organization-and-architecture/output/L01/chapters/02-building-blocks-and-research-method.md) |
| 10 | C | 只有 $f$ 变化，故 $P^\prime/P=2$。 [L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md) |
| 11 | A | $T=10^9\times1.5/(3\times10^9)=0.5\,\mathrm{s}$。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) |
| 12 | D | $2^5=32$，可以编号 32 个整数寄存器。 [L02·05](../computer-organization-and-architecture/output/L02/chapters/05-risc-v-overview-and-instruction-formats.md) |
| 13 | B | 偏移以字节计；十进制 24 等于十六进制 `0x18`。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md) |
| 14 | C | $5$ 为 `0101`，逐位取反再加 1 得 `1011`。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md) |
| 15 | D | 所有指令共用一个时钟周期，最慢路径决定周期下限；本课程模型中通常是 `ld`。 [L03·04](../computer-organization-and-architecture/output/L03/chapters/04-single-cycle-datapath.md) |
| 16 | A | 停顿 1 周期后，加载结果可从 MEM/WB 转发到 `add` 的 EX 级。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |

### 三、填空题

17. **答案：** ISA（指令集体系结构）；微架构；RTL（寄存器传输级）。

    分别关注软件接口、实现组织与寄存器传输层面的硬件描述。 [L01·01](../computer-organization-and-architecture/output/L01/chapters/01-architecture-definition-and-system-stack.md)

18. **答案：** $0.4$。

    $T=1/f=1/(2.5\times10^9)=0.4\,\mathrm{ns}$。 [L02·01](../computer-organization-and-architecture/output/L02/chapters/01-performance-metrics-and-clock.md)

19. **答案：** $2$。

    $0.5\times1+0.25\times2+0.25\times4=2$。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md)

20. **答案：** $1$；$8$；$23$。

    总计 32 位；规格化数的隐藏前导 1 不存入小数字段。 [L03·02](../computer-organization-and-architecture/output/L03/chapters/02-multiplication-division-and-floating-point.md)

21. **答案：** $14$。

    $5+(10-1)=14$，需计入开始填充和最后排空。 [L03·06](../computer-organization-and-architecture/output/L03/chapters/06-pipeline-design-and-performance.md)

22. **答案：** $500$；$2$。

    $T_{\min}=30+450+20=500\,\mathrm{ps}$，$f_{\max}=1/T_{\min}=2\,\mathrm{GHz}$。 [L03·03](../computer-organization-and-architecture/output/L03/chapters/03-datapath-elements-and-clocking.md)

### 四、简答题

**23. 参考答案与评分要点：**

- （1）$T_{\mathrm{CPU}}=\mathrm{IC}\times\mathrm{CPI}/f$。A：$T_A=1.2\times10^9\times1.2/(2\times10^9)=0.72\,\mathrm{s}$；B：$T_B=1.2\times10^9\times2/(3\times10^9)=0.8\,\mathrm{s}$。公式 2 分，两项结果各 2 分。
- （2）A 更快，性能之比为 $\Pi_A/\Pi_B=T_B/T_A=10/9\approx1.111$。判断 2 分，比值 2 分。
- （3）主频只决定每个周期多长，程序耗时还取决于动态指令数和平均 CPI（2 分）。本例指令数相同，A 每条指令平均耗时 $1.2/2=0.6\,\mathrm{ns}$，B 为 $2/3\approx0.667\,\mathrm{ns}$（2 分）；B 的更高频率没有抵消其更高 CPI，因此更慢（2 分）。

复习：[L02·01](../computer-organization-and-architecture/output/L02/chapters/01-performance-metrics-and-clock.md) · [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md)
