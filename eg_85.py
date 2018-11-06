# -*- coding:utf-8 -*-
# 问题：输入一个奇数，然后判断最少几个9 除于该数的结果为整数。
num = int(input('please input a odd number:'))
s = 9
i = 1
while s % num != 0:
    s = s+10**i*9
    i = i+1
print('至少需要 %d 个9: %d' % (i, s))
