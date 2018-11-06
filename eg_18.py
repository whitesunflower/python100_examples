# -*- coding：utf-8 -*-
# 问题：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
while True:
    s = 0
    result = 0
    n, num = map(int, input('please input a integer and the number:').split())
    for i in range(num):
        change = n * 10**i
        s = s+change
        result = result + s
        if i == num-1:
            print('{}'.format(s), end='')
        else:
            print('{}+'.format(s), end='')
    print('={}'.format(result))