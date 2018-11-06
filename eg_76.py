# -*- coding:utf-8 -*-
# 问题：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n。


def add_odd(n):
    num = 0
    for i in range(1, n+1, 2):
        num = num+1/i
    return num


def add_even(n):
    num = 0
    for i in range(2, n+1, 2):
        num = num + 1 / i
    return num


if __name__ == '__main__':
    n = int(input("please input a number: "))
    if n == 0:
        print("data error")
    if n % 2 == 0:
        print(add_even(n))
    if n % 2 != 0:
        print(add_odd(n))