# -*- coding:utf-8 -*-
# 问题：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
num = int(input('please input a number:'))
s = [1, 3, 5, 7, 9, 11, 13]
print(s)
for i in range(len(s)):
    if num >= int(s[len(s)-1]):
        s.insert(len(s), num)
        break
    if (num >= int(s[i])) and (num <= int(s[i+1])):
        s.insert(i+1, num)
        break
    else:
        continue
print(s)