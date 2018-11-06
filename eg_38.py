# -*- coding:utf-8 -*-
# 问题：求一个3*3矩阵主对角线元素之和
s = [[0 for i in range(0, 3)]for j in range(0, 3)]
num=0
for i in range(3):
    for j in range(3):
        s[i][j] = int(input('please input a integer:'))
        if i == j:
            num = num+s[i][j]
print(s)
print(num)