# -*- coding:utf-8 -*-
# 问题：将一个数组逆序输出
# 思路：首尾交换
s = []
for i in range(7):
    num = int(input("please input numbers:"))
    s.append(num)
print(s)
for j in range(len(s)//2):
    s[j], s[len(s)-j-1] = s[len(s)-j-1], s[j]
print(s)