# -*- coding:utf-8 -*-
# 问题：字符串排序。
# 从小到大排序
string1 = input("please input a string:")
string2 = input("please input a string:")
string3 = input("please input a string:")
if string1 > string2:
    string1, string2 = string2, string1
if string1 > string3:
    string1, string3 = string3, string1
if string2 > string3:
    string2, string3 = string3, string2
print(string1, string2, string3)


