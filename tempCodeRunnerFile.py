# 根据年份计算生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = int(input('请用户输入当前年份：'))

print([year%12])
print(chinese_zodiac[year%12])


