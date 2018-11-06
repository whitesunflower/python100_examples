# -*- coding:utf-8 -*-
# 问题：输出指定格式的日期
# 思路：使用time模块的 strftime 方法来格式化日期
import time
print(time.strftime("%w %Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

