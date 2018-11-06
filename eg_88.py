# -*- coding:utf-8 -*-
# 问题：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的*。
for i in range(7):
    num = int(input('please input a integer(1 to 50):'))
    print('*'*num)