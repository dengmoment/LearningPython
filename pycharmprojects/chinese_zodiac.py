# 根据年份计算生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print(chinese_zodiac[0])
# # 通过元素下标进行访问
# print(chinese_zodiac[0:6])
# print(chinese_zodiac[-1])
year = 2020
# print([2020%12])
print(chinese_zodiac[year%12])

print('鼠' in chinese_zodiac)

print('鼠' not in chinese_zodiac)

print(chinese_zodiac+chinese_zodiac)

print(chinese_zodiac+' '+chinese_zodiac)

print(chinese_zodiac+'cyd')

print(chinese_zodiac*3)
