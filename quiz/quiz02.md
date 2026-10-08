# 模拟小测 02：量化分析与指令语义

范围：前三课（L01 体系结构导论、L02 性能与 RISC-V 指令集、L03 ALU 与基础架构）。建议用时：40 分钟；满分：100 分。

答题约定：除题干另有说明，采用 RV64、32 位非压缩指令、按字节编址和小端序；涉及浮点或原子指令时，假定具备相应扩展。流水线题采用顺序发射的 IF—ID—EX—MEM—WB 五级教学模型，具体转发与时序条件以题干为准。计算结果可保留三位有效数字。

## 一、判断题（共 8 题，每题 2 分，共 16 分）

在括号中填写“对”或“错”。

1. 按本课程介绍的工程研究循环，通常先设计并建模基准系统，再测量、分析并设计改进系统。（　）

2. 在动态功耗模型中，其他因素不变时，功耗与电源电压的平方成正比。（　）

3. 同一任务的执行时间从 $30\,\mathrm{s}$ 缩短到 $20\,\mathrm{s}$，按执行时间倒数定义的性能提高了 $50\%$。（　）

4. 对多个程序的归一化执行时间求算术平均，比较结论一定不受参考机器选择的影响。（　）

5. RISC-V 的基本 `add` 指令可以直接把一个内存操作数与一个寄存器操作数相加。（　）

6. 两个同号补码数相加一定发生有符号溢出。（　）

7. 多周期数据通路需要内部状态寄存器，保存跨周期使用的中间结果。（　）

8. 若前一条指令计算后准备写入 `x0`，下一条读取 `x0` 时也应转发该计算结果。（　）

## 二、单项选择题（共 8 题，每题 4 分，共 32 分）

每题只有一个正确选项。

**9.** 编译器与硬件之间约定机器指令含义、寄存器和指令编码等内容的主要接口是什么？

- A. 微架构的数据通路设计
- B. ISA
- C. 操作系统的进程调度策略
- D. 具体门电路的连线

**10.** 下列哪一项最直接针对处理器等待主存数据的问题？

- A. 利用 Cache 提供更快的数据访问
- B. 只扩大主存容量，访问延迟和访存次数不变
- C. 只提高 ALU 峰值运算率，访存等待不变
- D. 只增加 SSD 容量，主存访问行为不变

**11.** 保持电容与活动因子不变，若电压和频率都变为原来的 $1.1$ 倍，动态功耗约变为原来的多少倍？

- A. $1.1$
- B. $1.21$
- C. $2.2$
- D. $1.331$

**12.** 某程序原执行时间中有 $80\%$ 可被优化，该部分速度提高到原来的 4 倍，其余部分不变。整体加速比为多少？

- A. $4$
- B. $3.2$
- C. $2.5$
- D. $1.25$

**13.** `sd x5, 16(x6)` 使用哪种指令格式？

- A. R 型
- B. S 型
- C. U 型
- D. UJ 型

**14.** 执行 32 位非压缩指令 `jal x1, L` 时，写入 `x1` 的值是什么？

- A. 目标地址 L
- B. 当前 PC
- C. 当前 PC 加 8
- D. 当前 PC 加 4

**15.** 将 4 位补码 `1000` 算术右移 1 位，结果及其有符号十进制值是什么？

- A. `0100`，$4$
- B. `0000`，$0$
- C. `1100`，$-4$
- D. `1110`，$-2$

**16.** 在本课程单周期控制表中，`beq` 对应的 `RegWrite、MemWrite、Branch、ALUSrc` 依次应为何值？

- A. `0, 0, 1, 0`
- B. `1, 0, 1, 0`
- C. `0, 1, 1, 1`
- D. `0, 0, 0, 1`

## 三、填空题（共 6 题，每题 6 分，共 36 分）

同一题有多个空时，每空均分；等价表达均可。

17. 在体系结构设计中，常见的三个量化权衡指标是 ________、________、________。（填写本课程反复强调的三项，顺序不限。）

18. 某程序执行 $6\times10^8$ 条指令，平均 $\mathrm{CPI}=2$，频率为 $2\,\mathrm{GHz}$，CPU 执行时间为 ________ $\mathrm{s}$。

19. 普通 I 型算术指令中，12 位有符号立即数能表示的最小值为 ________，最大值为 ________。（不讨论移位指令的特殊编码。）

20. 一位全加器的三个输入均为 1，则本位和为 ________，进位输出为 ________。

21. 某多周期实现中，load、store、R 型、分支分别用 5、4、4、3 个周期。若动态占比分别为 $50\%,20\%,20\%,10\%$，平均 CPI 为 ________。

22. 一个 IEEE 754 单精度规格化数的符号位为 0，指数域的无符号值 $E=130$，小数字段对应的小数值 $F=0.25$。该浮点数的十进制值为 ________。

## 四、简答题（共 1 题，16 分）

**23.** 用课程中的动态功耗模型 $P\approx\frac12 CV^2Af$ 分析“只靠提频”的局限。设 $C$ 和活动因子 $A$ 均不变。

- （1）若电压保持不变，频率提高 $20\%$，动态功耗变为原来的多少倍？（4 分）
- （2）若进一步采用近似关系 $f\propto V$，即提频时电压同比例增加，推导 $P$ 与 $f$ 的关系，并计算频率提高 $20\%$ 后的功耗倍数。（6 分）
- （3）解释这为什么会形成“功耗墙”，并给出两种不单纯依赖提频的改进方向。（6 分）

---

## 参考答案与解析

### 一、判断题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 1 | 对 | 基准系统使改进目标和比较对象明确。 [L01·02](../computer-organization-and-architecture/output/L01/chapters/02-building-blocks-and-research-method.md) |
| 2 | 对 | $P\propto V^2$，这里讨论动态功耗。 [L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md) |
| 3 | 对 | 性能比为 $30/20=1.5$；时间减少比例则为 $1/3$，两者不同。 [L02·01](../computer-organization-and-architecture/output/L02/chapters/01-performance-metrics-and-clock.md) |
| 4 | 错 | 归一化比值通常用几何平均汇总；算术平均可能随参考机变化而改变排序。 [L02·03](../computer-organization-and-architecture/output/L02/chapters/03-performance-summary-and-amdahls-law.md) |
| 5 | 错 | `add` 的源操作数来自寄存器；需先用 load 把内存数据读入寄存器。 [L02·04](../computer-organization-and-architecture/output/L02/chapters/04-isa-abstraction-and-risc.md) |
| 6 | 错 | 同号相加只是可能溢出；结果符号与操作数符号相反时才溢出。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md) |
| 7 | 对 | 例如 IR、MDR、A、B、ALUOut。 [L03·05](../computer-organization-and-architecture/output/L03/chapters/05-multicycle-datapath.md) |
| 8 | 错 | `x0` 必须保持为 0，转发条件应排除目的寄存器为 `x0` 的情况。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |

### 二、单项选择题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 9 | B | ISA 是软件可见的机器接口。 [L01·01](../computer-organization-and-architecture/output/L01/chapters/01-architecture-definition-and-system-stack.md) |
| 10 | A | Cache 利用局部性，使一部分访问由更快的存储层满足。 [L01·04](../computer-organization-and-architecture/output/L01/chapters/04-system-block-diagram-and-memory-wall.md) |
| 11 | D | $P^\prime/P=1.1^2\times1.1=1.331$。 [L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md) |
| 12 | C | $S_{\mathrm{tot}}=1/(0.2+0.8/4)=2.5$。 [L02·03](../computer-organization-and-architecture/output/L02/chapters/03-performance-summary-and-amdahls-law.md) |
| 13 | B | store 使用 S 型，立即数字段拆成高 7 位与低 5 位。 [L02·05](../computer-organization-and-architecture/output/L02/chapters/05-risc-v-overview-and-instruction-formats.md) |
| 14 | D | 保存顺序下一条指令的地址，供返回时使用。 [L02·07](../computer-organization-and-architecture/output/L02/chapters/07-branches-procedure-calls-and-stack.md) |
| 15 | C | 算术右移在高位补原符号位 1。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md) |
| 16 | A | 比较两个寄存器，不写寄存器与数据存储器，分支控制有效。 [L03·04](../computer-organization-and-architecture/output/L03/chapters/04-single-cycle-datapath.md) |

### 三、填空题

17. **答案：** 性能；功耗；面积。

    设计要结合需求，在这些资源与目标之间做取舍。 [L01·02](../computer-organization-and-architecture/output/L01/chapters/02-building-blocks-and-research-method.md)

18. **答案：** $0.6$。

    $6\times10^8\times2/(2\times10^9)=0.6\,\mathrm{s}$。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md)

19. **答案：** $-2048$；$2047$。

    范围为 $-2^{11}$ 到 $2^{11}-1$。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md)

20. **答案：** $1$；$1$。

    $1+1+1=11_2$，低位为和，高位为进位。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md)

21. **答案：** $4.4$。

    $0.5\times5+0.2\times4+0.2\times4+0.1\times3=4.4$。 [L03·05](../computer-organization-and-architecture/output/L03/chapters/05-multicycle-datapath.md)

22. **答案：** $10$。

    偏置为 127，故 $(-1)^0(1+0.25)2^{130-127}=10$。 [L03·02](../computer-organization-and-architecture/output/L03/chapters/02-multiplication-division-and-floating-point.md)

### 四、简答题

**23. 参考答案与评分要点：**

- （1）电压固定时 $P\propto f$，所以 $P^\prime/P=1.2$。关系和结果各 2 分。
- （2）由 $f\propto V$ 得 $V\propto f$，代入有 $P\propto V^2f\propto f^3$（3 分）。因此 $P^\prime/P=1.2^3=1.728$，即动态功耗增加 $72.8\%$（3 分）。
- （3）在此近似下，提频所带来的性能收益近似线性，动态功耗却按三次方增加，散热与功率密度会限制继续提频（2 分）。改进方向任答两项，每项 2 分：改善 Cache 降低访存等待；改进指令调度或执行单元以提高同频性能；用多核并行处理可并行工作；采用面向适合负载的异构加速。不能声称增加核心数对所有程序都保证线性提速。

复习：[L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md) · [L01·06](../computer-organization-and-architecture/output/L01/chapters/06-multicore-energy-and-reliability.md)
