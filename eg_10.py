# -*- coding：utf-8 -*-
# 问题：暂停一秒输出，并格式化当前时间
# 思路：使用time模块的strftime()方法来格式化日期

import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
time.sleep(2)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


