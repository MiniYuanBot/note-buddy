# 模拟小测 04：互连与流水线冒险

范围：前三课（L01 体系结构导论、L02 性能与 RISC-V 指令集、L03 ALU 与基础架构）。建议用时：40 分钟；满分：100 分。

答题约定：除题干另有说明，采用 RV64、32 位非压缩指令、按字节编址和小端序；涉及浮点或原子指令时，假定具备相应扩展。流水线题采用顺序发射的 IF—ID—EX—MEM—WB 五级教学模型，具体转发与时序条件以题干为准。计算结果可保留三位有效数字。

## 一、判断题（共 8 题，每题 2 分，共 16 分）

在括号中填写“对”或“错”。

1. 将内存控制器集成进 CPU，可以缩短处理器与内存控制器之间的连接路径。（　）

2. 接口只要采用更多并行信号线，其实际传输速度就一定比串行接口高。（　）

3. 若动态指令数增加，而平均 CPI 与时钟频率均不变，则 CPU 执行时间增加。（　）

4. RISC-V 的浮点寄存器 `f0` 与整数寄存器 `x0` 是同一个寄存器，并且都恒为零。（　）

5. `sc.d` 执行成功时，写入其状态目的寄存器的是非零值。（　）

6. 对于有符号补码加法，只要最高位向外产生进位，就能断定发生有符号溢出。（　）

7. 把指令存储器与数据存储器分开，可以避免取指与数据访存同时争用同一个单端口存储器。（　）

8. 若寄存器堆在周期前半写、后半读，则 ID 级可以在同一周期读到 WB 级刚写入的值。（　）

## 二、单项选择题（共 8 题，每题 4 分，共 32 分）

每题只有一个正确选项。

**9.** 针对 NAND 闪存原始位错误增多，哪种机制直接用于检测或纠正数据错误？

- A. 提高 CPU 主频
- B. 增大 Cache 的容量
- C. ECC
- D. 扩大存储容量但不引入冗余编码

**10.** 在动态功耗模型中，电压降为原来的 $90\%$，其他因素不变，动态功耗变为原来的多少倍？

- A. $0.9$
- B. $0.81$
- C. $1.1$
- D. $1.21$

**11.** 时钟周期为 $500\,\mathrm{ps}$，对应时钟频率是多少？

- A. $0.5\,\mathrm{GHz}$
- B. $500\,\mathrm{GHz}$
- C. $5\,\mathrm{GHz}$
- D. $2\,\mathrm{GHz}$

**12.** 某程序原执行时间有 $40\%$ 可以优化，其余部分完全不变。即使把可优化部分加速到耗时趋近于零，整体加速比上限也是多少？

- A. $\frac53$
- B. $2.5$
- C. $4$
- D. $\infty$

**13.** 一条 `beq` 位于 `0x1000`，分支成立。编码中的 `imm[12:1]` 按 12 位有符号数解释为十进制 12，最低位 `imm[0]` 隐含为 0。分支目标地址是什么？

- A. `0x100C`
- B. `0x101C`
- C. `0x1030`
- D. `0x1018`

**14.** `sc.d` 因保留失效而失败时，应产生什么效果？

- A. 仍执行本次存储，只返回失败标记
- B. 不执行本次存储，状态寄存器为非零
- C. 不执行本次存储，状态寄存器为零
- D. 必须把目标内存清零

**15.** 某五级流水线只有一个指令与数据共用的单端口存储器。IF 取指与 MEM 数据访问在同周期冲突，属于哪类冒险？

- A. 结构冒险
- B. 控制冒险
- C. 仅属于算术溢出
- D. 仅属于 RAW 数据冒险

**16.** 忽略填充、排空与其他冒险，基础 $\mathrm{CPI}=1$。分支占动态指令的 $25\%$，每个分支固定额外停顿 2 周期，实际 CPI 为多少？

- A. $1.25$
- B. $2$
- C. $1.5$
- D. $3$

## 三、填空题（共 6 题，每题 6 分，共 36 分）

同一题有多个空时，每空均分；等价表达均可。

17. 数字系统的三类基本构建模块中，负责处理数据的是 ________，负责保存数据的是 ________，负责搬运数据的是 ________。

18. 编译优化把动态指令数减少 $20\%$，同时使平均 CPI 增加 $25\%$，时钟频率不变。新执行时间与原执行时间之比为 ________。

19. 一条 `jal x1, L` 位于 `0x2000`，标签 L 的地址为 `0x2080`。执行后 `x1` 为 ________，新 PC 为 ________。（用十六进制表示。）

20. 4 位补码加法中，进入符号位的进位 $c_3=1$，送出符号位的进位 $c_4=0$。溢出标志 $O=c_3\oplus c_4$ 的值为 ________。

21. 检测到需要停顿的 load-use 冒险时，应冻结 ________ 和 ________，同时将新进入 ________ 的控制信号清零，以便在 EX 插入气泡。（填写 PC 或流水线寄存器名称。）

22. 一条开始为空的五级流水线，以 $1\,\mathrm{GHz}$ 运行，无停顿完成 100 条指令需要 ________ 个周期，总时间为 ________ $\mathrm{ns}$。

## 四、简答题（共 1 题，16 分）

**23.** 五级流水线有到 EX 的完整转发，ALU 结果在 EX 末产生，忽略其他冒险。初始 `x1=5`、`x2=2`、`x3=1`、`x4=3`，依次执行：

```asm
add x1, x1, x2
sub x1, x1, x3
add x5, x1, x4
```

- （1）按程序语义给出每条指令产生的结果，以及最终 `x5` 的值。（6 分）
- （2）第三条指令进入 EX 时，EX/MEM 与 MEM/WB 中均有针对 `x1` 的结果，应选择哪一个？若错误地选择较旧结果，`x5` 会变成多少？（6 分）
- （3）除“目的寄存器号与源寄存器号相同”外，转发检测还必须检查哪两个条件？（4 分）

---

## 参考答案与解析

### 一、判断题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 1 | 对 | 课程以北桥功能逐步并入 CPU 说明这种集成趋势。 [L01·03](../computer-organization-and-architecture/output/L01/chapters/03-motherboard-and-system-interconnect.md) |
| 2 | 错 | 还受工作频率、线间同步、距离等因素影响，针脚多不等于更快。 [L01·03](../computer-organization-and-architecture/output/L01/chapters/03-motherboard-and-system-interconnect.md) |
| 3 | 对 | $T_{\mathrm{CPU}}=\mathrm{IC}\times\mathrm{CPI}/f$。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) |
| 4 | 错 | 浮点与整数寄存器独立，`f0` 也不是恒零寄存器。 [L03·02](../computer-organization-and-architecture/output/L03/chapters/02-multiplication-division-and-floating-point.md) |
| 5 | 错 | 成功状态为 0，失败状态为非 0。 [L02·08](../computer-organization-and-architecture/output/L02/chapters/08-synchronization-and-addressing-modes.md) |
| 6 | 错 | 有符号溢出取决于进入和送出符号位的两个进位是否不同。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md) |
| 7 | 对 | 这是缓解结构冒险的一种方法。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |
| 8 | 对 | 这是教学流水线处理同周期读写关系的约定。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |

### 二、单项选择题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 9 | C | ECC 使用冗余编码信息检测或纠正一定范围内的错误。 [L01·06](../computer-organization-and-architecture/output/L01/chapters/06-multicore-energy-and-reliability.md) |
| 10 | B | 平方关系给出 $P^\prime/P=0.9^2=0.81$。 [L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md) |
| 11 | D | $500\,\mathrm{ps}=0.5\,\mathrm{ns}$，频率为其倒数。 [L02·01](../computer-organization-and-architecture/output/L02/chapters/01-performance-metrics-and-clock.md) |
| 12 | A | 剩余 $60\%$ 的时间不可消除，故上限为 $1/0.6=5/3$。 [L02·03](../computer-organization-and-architecture/output/L02/chapters/03-performance-summary-and-amdahls-law.md) |
| 13 | D | 实际字节偏移为 $12\times2=24$，从分支指令自身的 PC 加起：`0x1000 + 0x18 = 0x1018`。 [L02·07](../computer-organization-and-architecture/output/L02/chapters/07-branches-procedure-calls-and-stack.md) |
| 14 | B | 失败的条件存储不会进行此次内存写入，调用方可以据非零状态重试。 [L02·08](../computer-organization-and-architecture/output/L02/chapters/08-synchronization-and-addressing-modes.md) |
| 15 | A | 冲突源于硬件资源不足，而非分支或寄存器值尚未产生。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |
| 16 | C | $\mathrm{CPI}=1+0.25\times2=1.5$。 [L03·08](../computer-organization-and-architecture/output/L03/chapters/08-control-hazards.md) |

### 三、填空题

17. **答案：** 逻辑；状态；互连。

    按功能区分，分别对应计算、存储、传输。 [L01·02](../computer-organization-and-architecture/output/L01/chapters/02-building-blocks-and-research-method.md)

18. **答案：** $1$。

    $T^\prime/T=0.8\times1.25=1$，两种影响恰好抵消。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md)

19. **答案：** `0x2004`；`0x2080`。

    `x1` 保存顺序下一条地址，而 PC 改为目标地址。 [L02·07](../computer-organization-and-architecture/output/L02/chapters/07-branches-procedure-calls-and-stack.md)

20. **答案：** $1$。

    两个进位不同，发生有符号溢出。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md)

21. **答案：** PC；IF/ID；ID/EX。

    前端保持不动，让前面的 load 继续前进，并让使用者延后进入 EX。前两空顺序可交换。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md)

22. **答案：** $104$；$104$。

    $5+100-1=104$，时钟周期为 $1\,\mathrm{ns}$。 [L03·06](../computer-organization-and-architecture/output/L03/chapters/06-pipeline-design-and-performance.md)

### 四、简答题

**23. 参考答案与评分要点：**

- （1）第一条结果为 $5+2=7$，第二条为 $7-1=6$，第三条为 $6+3=9$，最终 `x5=9`。三项结果各 2 分。
- （2）EX/MEM 保存第二条指令的新结果 6，MEM/WB 保存第一条的旧结果 7（2 分）。应优先从 EX/MEM 转发 6，因为顺序语义要求读取最近一次写入的值（2 分）。若错误选择 7，将得到 $7+3=10$（2 分）。
- （3）检查生产者的 `RegWrite` 是否有效（2 分），并检查其目的寄存器是否不是 `x0`（2 分）。不写寄存器的指令和写 `x0` 的指令都不应作为这次转发的数据来源。

复习：[L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md)
