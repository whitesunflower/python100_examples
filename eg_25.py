# -*- coding：utf-8 -*-
# 问题：求1+2!+3!+...+20!的和
num = 0
for i in range(1, 21):
    fac = 1
    for j in range(1, i+1):
        fac = fac*j
    num = num+fac
print('1+2!+3!+...+20!=%d' % num)
