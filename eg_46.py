# -*- coding:utf-8 -*-
# 求输入数字的平方，如果平方运算后小于 50 则退出。
flag = 1
while flag:
    num = input('please input a number:')
    if num == 'q':
        break
    else:
        result = int(num)**2
        if result < 50:
            print('结果小于50')
            flag = 0
        else:
            print(result)
            flag = 1