# -*- coding:utf -*-
# 问题：八进制转换为十进制
# 思路：比如123=3*8^0+2*8^1+1*8^2
str1 = input("please input a str:")
str2 = str1[::-1]  # 实现逆序
n = 0
for i in range(len(str2)):
    n = n+int(str2[i])*8**i
print(n)