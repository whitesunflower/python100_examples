# -*- coding：utf-8 -*-
# 问题:列表连接
# 思路：连接使用 + 号或 extend() 方法
a = [1, 2, 4, 5, 7]
b = [8, 7, 7, 7]
print(a+b)
a.extend(b)
print(a)

