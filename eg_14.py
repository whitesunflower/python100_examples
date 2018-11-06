# -*- coding:utf-8 -*-
# 问题：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
# 思路：先找到除了1和本身的所有因数，然后再将一个正整数分解质因数


def separate(num):
    if num == 1:
        print('{} ={}'.format(num, 1), end='')
    else:
        print('{} ='.format(num), end='')
        while num != 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    num //= i
                    if num == 1:
                        print(i)
                    else:
                        print('{} *'.format(i), end='')
                    break


while True:
    num = int(input("Please enter an integer:"))
    if num == 'q':
        break
    else:
        separate(int(num))
        print()