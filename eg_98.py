# -*- coding：utf-8 -*-
# 问题：从键盘输入一个字符串，将小写字母全部转换成大写字母，
# 然后输出到一个磁盘文件"test"中保存。

str_b = input('please input a string(lowercase and uppercase letters)')
str_a = str_b.upper()
with open('test.txt', 'w') as f:
    f.write(str_a)

