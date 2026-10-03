---
schema_version: 1
type: "lecture-index"
title: "L03 运算与流水线"
course: "computer-organization-and-architecture"
lecture: "L03"
---

# L03 运算与流水线

[课程目录](../index.md)

算术电路决定结果怎样产生，数据通路与控制决定结果何时保存和使用。沿这条线索，从整数与浮点运算进入单周期、多周期和流水线，再按数据就绪时间处理冒险。

## 章节导航

- [01 整数运算电路](chapters/section-1.md)
- [02 乘除法机制](chapters/section-2.md)
- [03 浮点表示与运算](chapters/section-3.md)
- [04 单周期数据通路](chapters/section-4.md)
- [05 多周期实现](chapters/section-5.md)
- [06 流水线组织与性能](chapters/section-6.md)
- [07 冒险检测与处理](chapters/section-7.md)

## 本讲小结

评价执行组织要同时看周期长度与平均CPI，不能把缩短周期等同于缩短程序时间。判断旁路是否可行，则先找程序顺序中最新的有效生产者，再比较结果就绪时刻与消费者的使用阶段；来得及就转发，来不及就保持消费者并让生产者继续推进。

## 来源

- L03.pdf-PDF p.3
- L03.pdf-PDF p.4
- L03.pdf-PDF p.5
- L03.pdf-PDF p.6
- L03.pdf-PDF p.7
- L03.pdf-PDF p.8
- L03.pdf-PDF p.9
- L03.docx-DOCX body 1-39
- L03.docx-DOCX body 40-75
- L03.pdf-PDF p.10
- L03.pdf-PDF p.11
- L03.pdf-PDF p.12
- L03.pdf-PDF p.13
- L03.pdf-PDF p.14
- L03.pdf-PDF p.15
- L03.pdf-PDF p.16
- L03.pdf-PDF p.17
- L03.pdf-PDF p.124
- L03.pdf-PDF p.125
- L03.docx-DOCX body 76-112
- L03.docx-DOCX body 113-150
- L03.docx-DOCX body 151-211
- L03.pdf-PDF p.18
- L03.pdf-PDF p.19
- L03.pdf-PDF p.20
- L03.pdf-PDF p.21
- L03.pdf-PDF p.126
- L03.pdf-PDF p.23
- L03.pdf-PDF p.24
- L03.pdf-PDF p.25
- L03.pdf-PDF p.26
- L03.pdf-PDF p.27
- L03.pdf-PDF p.28
- L03.pdf-PDF p.29
- L03.pdf-PDF p.30
- L03.pdf-PDF p.31
- L03.pdf-PDF p.32
- L03.pdf-PDF p.33
- L03.pdf-PDF p.34
- L03.pdf-PDF p.35
- L03.pdf-PDF p.36
- L03.pdf-PDF p.37
- L03.pdf-PDF p.38
- L03.pdf-PDF p.39
- L03.pdf-PDF p.40
- L03.pdf-PDF p.41
- L03.pdf-PDF p.42
- L03.pdf-PDF p.43
- L03.pdf-PDF p.44
- L03.pdf-PDF p.45
- L03.pdf-PDF p.46
- L03.pdf-PDF p.47
- L03.pdf-PDF p.48
- L03.pdf-PDF p.49
- L03.pdf-PDF p.50
- L03.pdf-PDF p.51
- L03.pdf-PDF p.127
- L03.pdf-PDF p.128
- L03.pdf-PDF p.129
- L03.pdf-PDF p.141
- L03.docx-DOCX body 212-254
- L03.docx-DOCX body 255-295
- L03.docx-DOCX body 296-335
- L03.pdf-PDF p.52
- L03.pdf-PDF p.53
- L03.pdf-PDF p.54
- L03.pdf-PDF p.55
- L03.pdf-PDF p.56
- L03.pdf-PDF p.57
- L03.pdf-PDF p.58
- L03.pdf-PDF p.59
- L03.pdf-PDF p.60
- L03.pdf-PDF p.61
- L03.pdf-PDF p.62
- L03.pdf-PDF p.63
- L03.pdf-PDF p.64
- L03.pdf-PDF p.130
- L03.pdf-PDF p.131
- L03.pdf-PDF p.132
- L03.pdf-PDF p.133
- L03.pdf-PDF p.134
- L03.pdf-PDF p.135
- L03.pdf-PDF p.136
- L03.docx-DOCX body 336-383
- L03.docx-DOCX body 384-429
- L03.pdf-PDF p.65
- L03.pdf-PDF p.66
- L03.pdf-PDF p.67
- L03.pdf-PDF p.68
- L03.pdf-PDF p.69
- L03.pdf-PDF p.70
- L03.pdf-PDF p.71
- L03.pdf-PDF p.72
- L03.pdf-PDF p.73
- L03.pdf-PDF p.74
- L03.pdf-PDF p.75
- L03.pdf-PDF p.76
- L03.pdf-PDF p.77
- L03.pdf-PDF p.78
- L03.pdf-PDF p.79
- L03.pdf-PDF p.80
- L03.pdf-PDF p.81
- L03.pdf-PDF p.82
- L03.pdf-PDF p.83
- L03.pdf-PDF p.84
- L03.pdf-PDF p.85
- L03.pdf-PDF p.86
- L03.pdf-PDF p.87
- L03.pdf-PDF p.88
- L03.pdf-PDF p.89
- L03.pdf-PDF p.90
- L03.pdf-PDF p.137
- L03.pdf-PDF p.138
- L03.pdf-PDF p.139
- L03.pdf-PDF p.140
- L03.pdf-PDF p.142
- L03.docx-DOCX body 430-484
- L03.docx-DOCX body 485-528
- L03.pdf-PDF p.91
- L03.pdf-PDF p.92
- L03.pdf-PDF p.93
- L03.pdf-PDF p.94
- L03.pdf-PDF p.95
- L03.pdf-PDF p.96
- L03.pdf-PDF p.97
- L03.pdf-PDF p.98
- L03.pdf-PDF p.99
- L03.pdf-PDF p.100
- L03.pdf-PDF p.101
- L03.pdf-PDF p.102
- L03.pdf-PDF p.103
- L03.pdf-PDF p.104
- L03.pdf-PDF p.105
- L03.pdf-PDF p.106
- L03.pdf-PDF p.107
- L03.pdf-PDF p.108
- L03.pdf-PDF p.109
- L03.pdf-PDF p.110
- L03.pdf-PDF p.111
- L03.pdf-PDF p.112
- L03.pdf-PDF p.113
- L03.pdf-PDF p.114
- L03.pdf-PDF p.115
- L03.pdf-PDF p.116
- L03.pdf-PDF p.117
- L03.pdf-PDF p.118
- L03.pdf-PDF p.119
- L03.pdf-PDF p.120
- L03.pdf-PDF p.121
- L03.docx-DOCX body 529-575
- L03.docx-DOCX body 576-611
