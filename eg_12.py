# -* coding:utf-8 -*-
# 问题：判断101-200之间有多少个素数，并输出所有素数
# 思路：素数是仅有1和本身两个因数的数
from math import sqrt
num = 0
for i in range(101, 201):
    for j in range(2, int(sqrt(i)+1)):
        if i % j == 0:
            break
    else:
        num = num + 1
        print(i, end=' ')
        if num % 10 == 0:
            print()
print('\n the total is: %d' % num)
