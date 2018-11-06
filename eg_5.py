# -*- coding:utf-8 -*-
#  问题：输入三个整数x,y,z，请把这三个数由小到大输出
#  思路：利用append给列表添加整数，然后利用sort()排序
In = []
for i in range(3):
    x = int(input('please input a integer :'))
    In.append(x)
In.sort()
for j in In:
    print(j, end=' ')
