# -*- coding：utf-8 -*-
# 问题：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
a = 2
b = 1
num = 0
for i in range(1, 21):
    s = a/b
    a, b = a+b, a
    num = num+s
print(num)
