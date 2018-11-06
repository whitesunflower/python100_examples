# -*- coding:utf-8 -*-
# 问题：对10个数进行排序
s=[]
for k in range(10):
    num = int(input('please input a integer:'))
    s.append(num)
for i in range(10):
    for j in range(i+1, 10):
        if s[i] < s[j]:
            s[i], s[j] = s[j], s[i]
print(s)
for m in s:
    print(m, end=' ')