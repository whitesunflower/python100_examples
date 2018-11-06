# -*- coding:utf-8 -*-
# 问题：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。


def palindromic_number(s):
    if len(s) != 5:
        print('You have entered a incorrect number')
    else:
        if s[0] == s[-1] and s[1] == s[-2]:
            print('Yes')
        else:
            print('No')


while True:
    num = input('please input a integer:')
    if num == 'q':
        break
    else:
        palindromic_number(num)