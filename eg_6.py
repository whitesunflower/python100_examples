# -*- coding:utf-8 -*-
# 问题：斐波那契数列
# 思路：斐波那契数列：F(1)=1
#                   F(2)=1
#                   F(n)=F(n-1)+F(n-2)(n>=3)


# def fib(n):
#     a, b = 1, 1
#     for i in range(1, n-1):
#         a, b = b, a + b
#     return b
#
#
# print(fib(10))


# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
#
# print(fib(10))

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    else:
        fibs = [1, 1]
        for i in range(2, n):
            fibs.append(fibs[-1]+fibs[-2])
        return fibs


print(fib(10))