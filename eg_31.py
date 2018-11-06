# -*- coding:utf-8 -*-
# 问题：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。


def week(ss):
    if ss.lower() == 'm':
        print('today is Monday')
    if ss.lower == 'w':
        print('today is Tuesday')
    if ss.lower == 'f':
        print('today is Friday')
    if ss.lower() == 't':
        print('请输入前两个字母')
    if ss.lower() == 'tu':
        print('today is Tuesday')
    elif ss.lower() == 'th':
        print('today is Thursday')
    if ss.lower() == 's':
        print('请输入前两个字母')
    if ss.lower() == 'sa':
        print('today is Saturday')
    elif ss.lower() == 'su':
        print('today is Sunday')


while True:
    s = input("please input the first letter:")
    if s == "q":
        break
    else:
        week(s)