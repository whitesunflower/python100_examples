# -*- coding:utf-8 -*-
# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
import numpy as np
num = np.array([1, 4, 7, 9, 2, 5, 0, 1, 7, 6])
print('before:', num)
max_value = np.max(num)
point_1 = np.where(num == np.max(num))
min_value = np.min(num)
point_2 = np.where(num == np.min(num))
num[0], num[point_1] = num[point_1], num[0]
num[len(num)-1], num[point_2] = num[point_2], num[len(num)-1]
print('after :', num)