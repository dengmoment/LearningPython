# # 根据出生日期判断星座


# (month,day) = (12,6)
# zodiac_day = list(filter(lambda x: x<=(month,day),zodiac_days))
# print(zodiac_day)
# zodiac_len = list(zodiac_day)

#  print(list(zodiac_day))
# zodiac_len = len(list(zodiac_day))%12
# print(zodiac_name[zodiac_len])
# a_list = ['456','abc','xyz']
# a_list.append('D')
# # 添加大写字母D
# print(a_list)
# a_list.remove('456')
# print(a_list)
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

int_month = int(input("请输入月份："))
int_day = int(input("请输入日期："))

for zd_num in range(len(zodiac_days)):
    if zodiac_days[zd_num] >= (int_month, int_day):
        print("你的星座是：" +zodiac_name[zd_num])
        break
    elif int_month == 12 and int_day > 23:
        print("你的星座是：" +zodiac_name(0))
        break
