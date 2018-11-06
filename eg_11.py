# -*- coding：utf-8 -*-
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
# 问每个月的兔子总数为多少？
# 思路：其实质就是斐波那契数列，F(1)=1;F(2)=1;F(n)=F(n-1)+F(n-2)


def num_rabbit(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        a, b = 1, 1
        for i in range(1, n-1):
            a, b = b, a+b
        return b


while True:
    month = (input("please input the month:"))
    if month == 'q':
        break
    else:
        print(num_rabbit(int(month)))