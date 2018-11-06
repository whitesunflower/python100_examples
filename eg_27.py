# -*- coding：utf-8 -*-
# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def output(s, amount):
    if amount == 0:
        return
    print(s[amount-1], end='')
    output(s, amount-1)


s = input('please input a string:')
amount = len(s)
output(s, amount)