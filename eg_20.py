# -*- coding：utf-8 -*-
# 问题：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
#      再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


def height(n):
    sum_h = 100
    h1 = 100 / 2
    for i in range(2, n+1):
        h2 = 100 / (2**(i-1))
        h1 = h1 / 2
        sum_h = sum_h + h2*2
    print("the returned height is:%.3f" % h1)
    print("the total height is:%.3f" % sum_h)


height(10)

