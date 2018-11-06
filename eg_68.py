# -*- coding：utf-8 -*-
# 问题：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数。
# 思路：倒序改变,先把最后一个值传给一个变量。
n = int(input('please input n:'))
move = int(input('please input move:'))
num = []
for i in range(n):
    number = int(input('please input a number:'))
    num.append(number)
print('before:', num)

for j in range(move):
    store = num[-1]
    for i in range(n-1, -1, -1):
        num[i] = num[i-1]
    num[0] = store
print('after:', num)