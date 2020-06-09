# 根据年份计算生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# year = int(input('请用户输入当前年份：'))

# print([year%12])

# if (chinese_zodiac[year%12]) == '鼠':
#
#     print('鼠年的运势……')

for cz in (chinese_zodiac):
    print(cz)

for i in range(1,13):
    print(i)

for year in range(2000,2021):

    print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))