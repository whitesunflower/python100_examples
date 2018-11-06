# -*- coding:utf-8 -*-
#  问题：输入某年某月某日，判断这一天是这一年的第几天？
#  思路：闰年2月29天，因此当输入月份>=2时，需要做出判断看是否加一。
year = int(input('please enter the year:'))
month = int(input('please enter the month:'))
day = int(input('please enter the day:'))
month_value = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 1 <= month <= 12:
    sum1 = month_value[month-1]
else:
    print('data error')
sum1 = sum1 + day
if ((year % 4 == 0 and year % 400 != 0) or (year % 400 == 0)) and (month >= 2):
    sum1 += 1
print("it's the %dth day." % sum1)

