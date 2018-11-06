# -*- coding:utf-8 -*-
# 问题：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 思路：先列出所有排列再除去不满足条件的组合
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                # print(i*100+j*10+k)
                print(i, j, k)
                count = count+1
print(count)