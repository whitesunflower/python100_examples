# -*- coding:utf-8 -*-
# 问题：打印出所有的"水仙花数"，即一个三位数，其各位数字立方和等于该数本身。
num = 0
for i in range(100, 1000):
    L = i // 100
    S = i % 10
    M = i % 100 // 10
    if i == S**3 + L**3 + M**3:
        num = num+1
        print(i, end=' ')