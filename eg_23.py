# -*- coding：utf-8 -*-
# 问题：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
from sys import stdout
for i in range(4):
    for j in range(3-i):
        stdout.write(' ')
    for k in range(2*i+1):
        stdout.write('*')
    print()
for m in range(3):
    for n in range(m+1):
        stdout.write(' ')
    for p in range(5-2*m):
        stdout.write('*')
    print()