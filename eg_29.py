# -*- coding:utf-8 -*-
# 问题：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。


def reverse_print(n):
    number = len(n)
    print("it's a %d digit number" % number)
    print("tne inverse of that is:")
    for i in range(1, number+1):
        print(n[-i], end=' ')
    print()


while True:
    num = input('please input a integer:')
    if num == 'q':
        break
    else:
        reverse_print(num)