# -*- coding：utf-8 -*-
# 利用递归方法求5!


def num(n):
    result = 0
    if n == 0:
        result = 1
    else:
        result = n * num(n-1)
    return result


print('5!= %d' % num(5))