# -*- coding：utf-8 -*-
# 问题：使用lambda来创建匿名函数。
maxvalue = lambda x, y: (x > y)*x+(x < y)*y

if __name__ == "__main__":
    a = 5
    b = 18
    print('the larger one is: %d' % maxvalue(a, b))