# 模拟小测 05：综合模拟与易错点

范围：前三课（L01 体系结构导论、L02 性能与 RISC-V 指令集、L03 ALU 与基础架构）。建议用时：40 分钟；满分：100 分。

答题约定：除题干另有说明，采用 RV64、32 位非压缩指令、按字节编址和小端序；涉及浮点或原子指令时，假定具备相应扩展。流水线题采用顺序发射的 IF—ID—EX—MEM—WB 五级教学模型，具体转发与时序条件以题干为准。计算结果可保留三位有效数字。

## 一、判断题（共 8 题，每题 2 分，共 16 分）

在括号中填写“对”或“错”。

1. RTL 只描述用户应用的需求，不涉及寄存器之间的数据传送和硬件操作。（　）

2. 两颗芯片总功耗相同，就意味着它们的功率密度一定相同。（　）

3. 按同一段执行的总指令数与总周期数计算，若 $\mathrm{IPC}=0.5$，则 $\mathrm{CPI}=2$。（　）

4. 某编译优化减少了动态指令数，就可以不检查 CPI 和时钟周期而断定程序必然更快。（　）

5. 在无异常的情况下，一条 32 位 `beq` 的分支条件不成立时，顺序下一条指令地址为当前 PC 加 4。（　）

6. $n$ 位有符号补码整数的取值范围是 $-2^{n-1}$ 到 $2^{n-1}-1$。（　）

7. 只要增加流水线级数，程序总执行时间就一定进一步缩短。（　）

8. 将分支比较从 EX 提前到 ID 后，原先只面向 EX 的转发硬件可能不再足够。（　）

## 二、单项选择题（共 8 题，每题 4 分，共 32 分）

每题只有一个正确选项。

**9.** 当工作频率不变时，下列哪项仍可能提高程序执行性能？

- A. 只缩短源代码行数，实际执行的机器指令和时序均不变
- B. 只增加不参与该程序执行的空闲硬件
- C. 改善数据访问与指令调度，减少等待和气泡
- D. 只把性能报告中的 CPI 换算成 IPC

**10.** 多核中的 Cache 一致性主要处理什么问题？

- A. 让所有核心的时钟频率完全相同
- B. 保证所有线程都不需要同步
- C. 让所有 Cache 的容量相同
- D. 协调同一内存位置在不同 Cache 中的副本及其更新

**11.** 某机器两个程序的归一化执行时间分别为 $0.5$ 和 $2$，其几何平均是多少？

- A. $1.25$
- B. $1$
- C. $0.8$
- D. $2.5$

**12.** 下列哪条指令把一个常数作为直接编码在指令中的算术源操作数？

- A. `addi x5, x6, 12`
- B. `add x5, x6, x7`
- C. `sub x5, x6, x7`
- D. `and x5, x6, x7`

**13.** 下面两条指令执行完毕后，`x5` 的值是多少？

```asm
addi x0, x0, 7
addi x5, x0, 3
```

- A. $0$
- B. $7$
- C. $3$
- D. $10$

**14.** IEEE 754 单精度中，指数域全为 1 且小数字段非零，表示什么？

- A. NaN
- B. 正零或负零
- C. 规格化有限数
- D. 一定是正无穷

**15.** 五级流水线中，某 ALU 指令与依赖它的 ALU 指令紧邻。第一条结果在 EX 末产生，有完整 EX 转发且无其他冒险。当第二条进入 EX 时，应从哪里取得第一条的结果？

- A. 从指令存储器
- B. 从 PC
- C. 只能等到结果正式写回寄存器后再执行
- D. 从 EX/MEM 流水线寄存器

**16.** 五级流水线有到 EX 的完整转发，加载数据在 MEM 末产生，`x9`、`x10`、`x11` 与其他指令无相关。仅考虑加载结果引起的停顿，以下序列还需插入几个气泡？

```asm
ld  x5, 0(x6)
add x9, x10, x11
add x7, x5, x8
```

- A. 1 个
- B. 0 个
- C. 2 个
- D. 3 个

## 三、填空题（共 6 题，每题 6 分，共 36 分）

同一题有多个空时，每空均分；等价表达均可。

17. 保持电容与活动因子不变，若频率和电压都提高到原来的 $1.5$ 倍，则动态功耗变为原来的 ________ 倍。

18. 某程序动态执行 $8\times10^8$ 条指令，频率为 $2\,\mathrm{GHz}$。平均 CPI 从 $1.5$ 降为 $1.2$，其余不变。原执行时间为 ________ $\mathrm{s}$，新执行时间为 ________ $\mathrm{s}$，加速比为 ________。

19. 采用小端序，用 `sd` 把 64 位值 `0x1122334455667788` 存到起始地址 `0x1000`。地址 `0x1000` 处的字节是 ________，地址 `0x1007` 处的字节是 ________。（用十六进制表示。）

20. 一位全加器输入为 $A=1,B=0,C_{\mathrm{in}}=1$，则本位和 $S=$ ________，进位输出 $C_{\mathrm{out}}=$ ________。

21. 某多周期处理器的 load、store、R 型、分支分别用 5、4、4、3 周期。动态指令占比分别为 $30\%,20\%,40\%,10\%$，平均 CPI 为 ________。

22. RISC-V 基本非压缩指令长度为 ________ 位；普通 I 型立即数字段为 ________ 位；U 型编码中的立即数字段为 ________ 位。

## 四、简答题（共 1 题，16 分）

**23.** 某处理器执行同一程序时，分支占动态指令的 $20\%$，其余指令均按基础 $\mathrm{CPI}=1$ 执行。两种方案都在取到分支后停止继续取指，直到分支判定完成；下列额外停顿互不重叠。忽略填充、排空与其他冒险，指令数不变。

| 方案 | 分支判定位置 | 每个分支额外停顿 | 时钟周期 |
| --- | --- | --- | --- |
| 原方案 | MEM | 3 周期 | $1.0\,\mathrm{ns}$ |
| 新方案 | ID | 1 周期 | $1.2\,\mathrm{ns}$ |

- （1）分别求两个方案的平均 CPI。（6 分）
- （2）计算新方案相对原方案的加速比，判断是否值得改进。（6 分）
- （3）保持表中停顿数不变，新方案的时钟周期必须小于多少，才会严格快于原方案？这说明评价分支提前判定时需要考虑什么权衡？（4 分）

---

## 参考答案与解析

### 一、判断题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 1 | 错 | RTL 是寄存器传输级，描述硬件的数据传送和操作关系。 [L01·01](../computer-organization-and-architecture/output/L01/chapters/01-architecture-definition-and-system-stack.md) |
| 2 | 错 | 功率密度还取决于发热面积；同样的功耗集中在更小面积上，平均功率密度更高。 [L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md) |
| 3 | 对 | 对同一段执行，二者互为倒数。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) |
| 4 | 错 | 需要比较 $\mathrm{IC}\times\mathrm{CPI}\times\mathrm{CC}$，单个因子改善不能保证总耗时下降。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) |
| 5 | 对 | 非压缩指令长 4 字节，不跳转就顺序执行。 [L03·04](../computer-organization-and-architecture/output/L03/chapters/04-single-cycle-datapath.md) |
| 6 | 对 | 负数端比正数端多一个可表示值。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md) |
| 7 | 错 | 还受级间寄存器开销、阶段不平衡和冒险代价限制。 [L03·06](../computer-organization-and-architecture/output/L03/chapters/06-pipeline-design-and-performance.md) |
| 8 | 对 | 操作数更早被需要，可能要增加 ID 级转发和额外的数据冒险停顿。 [L03·08](../computer-organization-and-architecture/output/L03/chapters/08-control-hazards.md) |

### 二、单项选择题

| 题号 | 答案 | 解析与复习 |
| --- | --- | --- |
| 9 | C | 同频性能可以通过更高效的数据供给、执行和调度改善。 [L01·06](../computer-organization-and-architecture/output/L01/chapters/06-multicore-energy-and-reliability.md) |
| 10 | D | 多个核心缓存同一数据时，写入需要按一致性规则协调，避免读取不应继续使用的旧副本。 [L01·06](../computer-organization-and-architecture/output/L01/chapters/06-multicore-energy-and-reliability.md) |
| 11 | B | $\sqrt{0.5\times2}=1$。 [L02·03](../computer-organization-and-architecture/output/L02/chapters/03-performance-summary-and-amdahls-law.md) |
| 12 | A | `addi` 的立即数 12 直接参与运算，属于立即数寻址。 [L02·08](../computer-organization-and-architecture/output/L02/chapters/08-synchronization-and-addressing-modes.md) |
| 13 | C | 第一条对 `x0` 的写入无效，第二条仍计算 $0+3$。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md) |
| 14 | A | 指数全 1、小数为 0 才表示无穷；小数非零表示 NaN。 [L03·02](../computer-organization-and-architecture/output/L03/chapters/02-multiplication-division-and-floating-point.md) |
| 15 | D | 第一条的 EX 结果已被 EX/MEM 保存，可转发给下一条的 ALU。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |
| 16 | B | 独立指令提供了一拍间隔，第三条到 EX 时可从 MEM/WB 取得加载值。 [L03·07](../computer-organization-and-architecture/output/L03/chapters/07-structural-and-data-hazards.md) |

### 三、填空题

17. **答案：** $3.375$。

    $P^\prime/P=1.5^2\times1.5=3.375$；写成 3.38 也可。 [L01·05](../computer-organization-and-architecture/output/L01/chapters/05-technology-trends-and-power-wall.md)

18. **答案：** $0.6$；$0.48$；$1.25$。

    分别代入 $T=\mathrm{IC}\times\mathrm{CPI}/f$；加速比 $0.6/0.48=1.25$。 [L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md)

19. **答案：** `0x88`；`0x11`。

    最低有效字节放低地址，最高有效字节放高地址。 [L02·06](../computer-organization-and-architecture/output/L02/chapters/06-arithmetic-and-memory-instructions.md)

20. **答案：** $0$；$1$。

    $1+0+1=10_2$；也可用异或和多数函数计算。 [L03·01](../computer-organization-and-architecture/output/L03/chapters/01-alu-and-integer-addition.md)

21. **答案：** $4.2$。

    $0.3\times5+0.2\times4+0.4\times4+0.1\times3=4.2$。 [L03·05](../computer-organization-and-architecture/output/L03/chapters/05-multicycle-datapath.md)

22. **答案：** $32$；$12$；$20$。

    U 型的 20 位立即数字段用于构成高位常量；不要把字段宽度与寄存器字长混淆。 [L02·05](../computer-organization-and-architecture/output/L02/chapters/05-risc-v-overview-and-instruction-formats.md)

### 四、简答题

**23. 参考答案与评分要点：**

- （1）$\mathrm{CPI}_{\mathrm{old}}=1+0.2\times3=1.6$；$\mathrm{CPI}_{\mathrm{new}}=1+0.2\times1=1.2$。各 3 分。
- （2）同一指令数下，时间正比于 $\mathrm{CPI}\times T_{\mathrm{cycle}}$。加速比为

  $$
  S=\frac{1.6\times1.0}{1.2\times1.2}
   =\frac{10}{9}\approx1.111.
  $$

  正确比较 CPI 与周期的乘积 2 分，比值 2 分；新方案更快，性能约提高 $11.1\%$，若只按执行时间评价则值得采用（2 分）。
- （3）令新周期为 $T_{\mathrm{new}}$，要求 $1.2T_{\mathrm{new}}<1.6\times1.0\,\mathrm{ns}$，所以 $T_{\mathrm{new}}<\frac43\,\mathrm{ns}\approx1.333\,\mathrm{ns}$（2 分）。减少分支停顿能降低 CPI，但提前比较可能拉长关键路径、增加周期；必须结合两者评估（2 分）。在等号处两方案一样快。

复习：[L02·02](../computer-organization-and-architecture/output/L02/chapters/02-cpi-and-iron-law.md) · [L03·08](../computer-organization-and-architecture/output/L03/chapters/08-control-hazards.md)
