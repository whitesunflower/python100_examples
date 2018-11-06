# -*- coding:utf-8 -*-
# 问题：按逗号分隔列表
# 思路：利用join()方法拼接
L = [1, 2, 3, 4, 5, 6, 7, 8]
s = ','.join(str(i) for i in L)
print(s)  