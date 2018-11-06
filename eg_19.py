# -*- coding：utf-8 -*-
# 问题：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
#       例如6=1＋2＋3.编程找出1000以内的所有完数。

for j in range(1, 1001):
    num = 0
    for i in range(1, j):
        if j % i == 0:
            num = num + i
        else:
            continue
    if num == j:
        print(j, end=' ')