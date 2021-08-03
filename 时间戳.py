import time

# 格式化成2020-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2020形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2020"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))



import calendar
cal = calendar.month(2021, 7)
print("以下输出2020年9月份的日历:")
print(cal)


print('here')

