# 模拟小测 03：运算与数据通路

范围：前三课（L01 体系结构导论、L02 性能与 RISC-V 指令集、L03 ALU 与基础架构）。建议用时：40 分钟；满分：100 分。

答题约定：除题干另有说明，采用 RV64、32 位非压缩指令、按字节编址和小端序；涉及浮点或原子指令时，假定具备相应扩展。流水线题采用顺序发射的 IF—ID—EX—MEM—WB 五级教学模型，具体转发与时序条件以题干为准。计算结果可保留三位有效数字。

## 一、判断题（共 8 题，每题 2 分，共 16 分）

在括号中填写“对”或“错”。

1. 只要增加处理器核心数，任何程序的执行时间都会按核心数等比例缩短。（　）

2. ECC 的作用是利用冗余信息检测或纠正错误，而不是保证存储介质永远不产生原始位错误。（　）

3. 用户观察到的任务总耗时可能包含 I/O 等待，因此不一定等于性能铁律中的 CPU 执行时间。（　）

4. 性能铁律中的指令数，可以直接用高级语言源代码的行数代替。（　）

5. 小端序把多字节数据的最低有效字节放在最低内存地址处。（　）

6. RV64 的 `mul` 将完整乘积的低 64 位写入目的寄存器，因此数学乘积一定不会超出结果可表示的范围。（　）

7. 本课程单周期处理器中，较短指令仍需使用由最慢指令路径决定的时钟周期。（　）

8. 本课程的非流水多周期处理器中，不同指令必然同时占据不同执行步骤。（　）

## 二、单项选择题（共 8 题，每题 4 分，共 32 分）

每题只有一个正确选项。

**9.** 在固定芯片面积预算下，决定增加 Cache 还是增加执行单元，最合理的依据是什么？

- A. 永远选择 Cache
- B. 永远选择执行单元
- C. 只比较主频，忽略 CPI 和功耗
- D. 结合目标负载、测量结果和瓶颈进行权衡

**10.** 线程频繁从一个核心迁移到另一个核心，原本缓存的数据可能不能直接就近使用。这主要涉及哪个概念？

- A. Cache 亲和性
- B. 指令长度
- C. 补码溢出
- D. 立即数符号扩展

**11.** 同一机器依次执行两个动态指令数相等的程序，两程序的 IPC 分别为 1 和 4，时钟频率相同。合并两次执行后，总指令数除以总周期数得到的 IPC 是多少？

- A. $2.5$
- B. $2$
- C. $1.6$
- D. $4$

**12.** 内存中某字节为 `0x80`，RV64 执行 `lb` 把该字节装入整数寄存器。结果是哪一个？

- A. `0x0000000000000080`
- B. `0x0000000000000000`
- C. `0xFFFFFFFFFFFFFFFF`
- D. `0xFFFFFFFFFFFFFF80`

**13.** 按课程所用的 RISC-V 调用约定，被调用函数若使用并修改下列哪个寄存器，应在返回前恢复其原值？

- A. `x10 (a0)`
- B. `x8 (s0)`
- C. `x5 (t0)`
- D. `x11 (a1)`

**14.** IEEE 754 单精度规格化数 $-1.5$ 的符号位 $s$、指数域无符号值 $E$、小数字段对应小数 $F$ 分别是什么？

- A. $s=1,E=127,F=0.5$
- B. $s=1,E=128,F=0.5$
- C. $s=0,E=127,F=0.5$
- D. $s=1,E=127,F=1.5$

**15.** 寄存器的保持时间 $T_h$，要求输入数据在哪段时间保持稳定？

- A. 有效时钟沿之前
- B. 有效时钟沿之后
- C. 从程序开始直到结束
- D. 只在无时钟信号时

**16.** 为在同一周期读取两个源寄存器并写回一个目的寄存器，本课程的整数寄存器堆采用哪种基本端口配置？

- A. 1 个读端口、1 个写端口
- B. 1 个读端口、2 个写端口
- C. 2 个读端口、1 个写端口
- D. 2 个读端口、2 个写端口

## 三、填空题（共 6 题，每题 6 分，共 36 分）

同一题有多个空时，每空均分；等价表达均可。

17. 保持电容与活动因子不变，电压和频率都降到原来的 $80\%$，动态功耗降到原来的 ________ 倍。

18. 三个程序的执行时间分别为 $2\,\mathrm{s}$、$4\,\mathrm{s}$、$9\,\mathrm{s}$，执行时间的算术平均为 ________ $\mathrm{s}$。

19. 依次执行下面两条指令后，`x5` 的值用十六进制表示为 ________。

```asm
lui  x5, 0x12345
addi x5, x5, 0x678
```

20. 十进制 $-3$ 的 4 位补码为 ________；用 4 位补码计算 $7+(-3)$ 并丢弃最高位进位，结果位串为 ________。

21. 忽略时钟偏斜，寄存器输出延迟为 $40\,\mathrm{ps}$，最长组合逻辑延迟为 $600\,\mathrm{ps}$，建立时间为 $30\,\mathrm{ps}$，则最短时钟周期为 ________ $\mathrm{ps}$。

22. 一条五级流水线开始时为空，时钟周期为 $200\,\mathrm{ps}$。无冒险、无停顿地执行 8 条指令直到全部完成，需要 ________ 个周期，总时间为 ________ $\mathrm{ns}$。

## 四、简答题（共 1 题，16 分）

**23.** 比较单周期数据通路中 `ld x5, 16(x6)` 与 `sd x5, 16(x6)` 的执行过程。设地址有效且正确对齐。

- （1）两条指令都需要 ALU 计算什么？写出地址计算式。（4 分）
- （2）分别给出两条指令的 `MemRead、MemWrite、RegWrite、MemtoReg` 取值。`MemtoReg=1` 表示选择存储器数据写回，`0` 表示选择 ALU 结果；无关项可写 X。（8 分）
- （3）为什么对 `sd`，`MemtoReg` 可以是 X，而 `RegWrite` 不能写成 X？（4 分）

---

## 参考答案与解析

### 一、判断题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 1 | 错 | 串行部分、同步通信、存储带宽等都会限制多核收益。 [L01·06](../computer-organization-and-architecture/output/L01/chapters/06-multicore-energy-and-reliability.md) |
| 2 | 对 | 纠错能力有限，应区分原始误码与纠错后的残余错误。 [L01·06](../computer-organization-and-architecture/output/L01/chapters/06-multicore-energy-and-reliability.md) |
| 3 | 对 | 性能铁律分解的是 CPU 执行该程序的时间。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) |
| 4 | 错 | 这里指运行时动态执行的机器指令条数，还受循环次数、编译结果等影响。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) |
| 5 | 对 | 端序描述多字节数据在内存中的字节排列。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md) |
| 6 | 错 | 截取低 64 位可能丢失高位；不报告溢出不等于数学上不会溢出。 [L03·02](../computer-organization-and-architecture/output/L03/chapters/02-multiplication-division-and-floating-point.md) |
| 7 | 对 | 周期长度统一，较短路径的剩余时间不能单独缩短。 [L03·04](../computer-organization-and-architecture/output/L03/chapters/04-single-cycle-datapath.md) |
| 8 | 错 | 多周期仅表示一条指令跨多个周期；跨指令重叠执行是流水线的特点。 [L03·05](../computer-organization-and-architecture/output/L03/chapters/05-multicycle-datapath.md) |

### 二、单项选择题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 9 | D | 体系结构设计应由需求和量化结果驱动。 [L01·02](../computer-organization-and-architecture/output/L01/chapters/02-building-blocks-and-research-method.md) |
| 10 | A | 线程放置位置与缓存数据位置相关，迁移可能引入额外数据访问开销。 [L01·06](../computer-organization-and-architecture/output/L01/chapters/06-multicore-energy-and-reliability.md) |
| 11 | C | 设每个程序执行 $N$ 条指令，总周期为 $N+N/4$，故总 IPC 为 $2N/(N+N/4)=1.6$。 [L02·03](../computer-organization-and-architecture/output/L02/chapters/03-performance-summary-and-amdahls-law.md) |
| 12 | D | `lb` 按最高位符号扩展，结果表示 $-128$；零扩展对应 `lbu`。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md) |
| 13 | B | `s0` 是被调用者保存寄存器；参数和临时寄存器不属于这一类。 [L02·07](../computer-organization-and-architecture/output/L02/chapters/07-branches-procedure-calls-and-stack.md) |
| 14 | A | $-1.5=(-1)^1(1+0.5)2^0$，故 $E=127$。 [L03·02](../computer-organization-and-architecture/output/L03/chapters/02-multiplication-division-and-floating-point.md) |
| 15 | B | 建立时间针对时钟沿之前，保持时间针对时钟沿之后。 [L03·03](../computer-organization-and-architecture/output/L03/chapters/03-datapath-elements-and-clocking.md) |
| 16 | C | 两个读端口对应两个源操作数，一个写端口用于结果写回。 [L03·03](../computer-organization-and-architecture/output/L03/chapters/03-datapath-elements-and-clocking.md) |

### 三、填空题

17. **答案：** $0.512$。

    $P^\prime/P=0.8^2\times0.8=0.512$。 [L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md)

18. **答案：** $5$。

    $(2+4+9)/3=5\,\mathrm{s}$。 [L02·03](../computer-organization-and-architecture/output/L02/chapters/03-performance-summary-and-amdahls-law.md)

19. **答案：** `0x0000000012345678`（或省略前导零写成 `0x12345678`）。

    `lui` 先得到 `0x12345000`，再加 `0x678`；低 12 位立即数的符号位为 0。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md)

20. **答案：** `1101`；`0100`。

    `0011` 取反加一得 `1101`；$0111_2+1101_2=1\,0100_2$。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md)

21. **答案：** $670$。

    $40+600+30=670\,\mathrm{ps}$。 [L03·03](../computer-organization-and-architecture/output/L03/chapters/03-datapath-elements-and-clocking.md)

22. **答案：** $12$；$2.4$。

    $5+8-1=12$，$12\times200\,\mathrm{ps}=2.4\,\mathrm{ns}$。 [L03·06](../computer-organization-and-architecture/output/L03/chapters/06-pipeline-design-and-performance.md)

### 四、简答题

**23. 参考答案与评分要点：**

- （1）都计算有效地址 $a_{\mathrm{eff}}=\mathrm{Reg}[\mathrm{x6}]+\operatorname{sext}(\mathrm{imm}_{12})$（2 分）。本题立即数为 16，所以 $a_{\mathrm{eff}}=\mathrm{Reg}[\mathrm{x6}]+16$，ALU 执行加法（2 分）。
- （2）每个控制信号 1 分，共 8 分：

| 指令 | MemRead | MemWrite | RegWrite | MemtoReg |
| --- | --- | --- | --- | --- |
| `ld` | 1 | 0 | 1 | 1 |
| `sd` | 0 | 1 | 0 | X |

- （3）`sd` 不写寄存器，所以选哪一路写回数据都不会被使用，`MemtoReg` 可为 X（2 分）。`RegWrite` 是寄存器堆写使能，必须为 0；若误置为 1，可能破坏寄存器状态（2 分）。对 `sd` 把 `MemtoReg` 写为 0 或 1 也可得分，但应说明这是由于该信号无关。

复习：[L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md) · [L03·04](../computer-organization-and-architecture/output/L03/chapters/04-single-cycle-datapath.md)
