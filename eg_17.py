# -*- coding:utf-8 -*-
# 问题：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数


def decide(s):
    letter = 0
    digit = 0
    space = 0
    others = 0
    for i in range(len(s)):
        if s[i].isdigit():
            digit += 1
        elif s[i].isalpha():
            letter += 1
        elif s[i].isspace():
            space += 1
        else:
            others += 1
    print('英文字母：%d' % letter)
    print('空格：%d' % space)
    print('数字：%d' % digit)
    print('其他：%d' % others)


while True:
    string = input('please:')
    if string == 'q':
        break
    else:
        decide(string)
