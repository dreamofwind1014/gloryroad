# 习题21、二进制转换为十进制
# 101 = 1*2^0 + 0*2^1 + 1*2^2 = 5
"""
1、输入一个数字，判断数字，如果不是，提示，如果数字的中含有大于1的数字，提示
2、二进制数字：
"""


# def int_2(num_2):
#     num_2 = input('>>:')
#     if not num_2.isdigit():
#         return "请输入二进制数字"
#     else:
#         num_2_list = list(str(num_2))
#         # print(num_2_list)
#         for i in num_2_list:
#             if int(i) > 1:
#                 return '二进制数字只有0，1'
#                 break
#         else:
#             num_10 = 0
#             for i in range(len(num_2_list)):
#                 num_10 += int(num_2_list[len(num_2_list)-i-1])*2**i
#         return num_10
#
#
# print(int_2(1011))


# 习题22：输入1-127的ascii码并输出对应字符
# 方法一：
# for i in range(127):
#     print(chr(i+1))
#
#
# 方法二：
# for i in range(1, 128):
#     print(chr(i))


# 习题23：输入a，b，c，d4个整数，计算a+b-c*d的结果
# def calculate(a, b, c, d):
#     if not (isinstance(a, (int, float))and isinstance(b, (int, float))and isinstance(c, (int, float))and isinstance(d, (int, float))):
#         return "必须传入数字类型的参数"
#     else:
#         return a+b-c*d
#
#
# print(calculate(1, 1, 2, 2.2))


# def input_num():
#     is_put_num = True
#     while is_put_num:
#         num = input('>> 输入数字:')
#         try:
#             num = int(num)
#
#         except:
#             try:
#                 num = float(num)
#             except:
#                 continue
#         if isinstance(num, (int, float)):
#             is_put_num = False
#     return num
#
#
# a = input_num()
# b = input_num()
# c = input_num()
# d = input_num()
# print(a+b-c*d)


# 习题24：计算一周有多少分钟、多少秒钟
# from user_defined_method import user_defined_method
#
#
# def calculate_minutes_and_second(day):
#     minutes = day*24*60
#     second = day*24*60*60
#     result = '%s天有%d分钟，%d秒' % (day, minutes, second)
#     return result
#
#
# day_num = user_defined_method.input_num()
# print(calculate_minutes_and_second(day_num))


# 习题25：3个人在餐厅吃饭，想分摊饭费。
# 总共花费35.27美元，他们还想给15%的小费。
# 每个人该怎么付钱，编程实现
# from user_defined_method import user_defined_method
# expense = user_defined_method.input_num('花费金额')
# tip_ratio = user_defined_method.input_num('小费比例%前部分数字')/100
# people_num = user_defined_method.input_num('均摊人数')
# everyone_expense = expense*(1+tip_ratio)/people_num
# print('%s人均摊%s美元的花费，并且给%s比例小费，每人应付%s美元' % (people_num, expense, str(tip_ratio*100)+'%', everyone_expense))


# 习题26：计算一个12.5m X 16.7m的矩形房间的面积和周长
def rectangle_area(long, wide):
    area = long*wide
    return area


def rectangle_perimeter(long, wide):
    perimeter = (long+wide)*2
    return perimeter


from user_defined_method import user_defined_method
rectangle_long = user_defined_method.input_num("矩形长（数字）")
rectangle_wide = user_defined_method.input_num("矩形宽（数字）")
rectangle_unit = ''
while rectangle_unit not in ['km', 'm', 'dm', 'cm', 'mm']:
    rectangle_unit = input("长度单位[km,m,dm,cm,mm]")
if rectangle_unit == 'km':
    area_unit = '平方千米'
elif rectangle_unit == 'm':
    area_unit = '平方米'
elif rectangle_unit == 'dm':
    area_unit = '平方分米'
elif rectangle_unit == 'cm':
    area_unit = '平方厘米'
else:
    area_unit = '平方毫米'
print("长{long}{unit_1},宽{wide}{unit}的矩形"
      "面积为{area}{unit_2}",)


# 习题27：怎么得到9 / 2的小数结果


# 习题28：python计算中7 * 7 *7 * 7，可以有多少种写法


# 习题29：写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)


# 习题30：一家商场在降价促销。如果购买金额50-100元（包含50元和100元）之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，
# 再显示出折扣（10%或20%）和最终价格


# 习题31：求1 + 2 + 3 +….+100


# 习题32：判断一个数n能否同时被3和5整除


# 习题33：交换两个变量的值


# 习题34：一个足球队在寻找年龄在10到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性， f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数


# 统计字符长度"一二三四五六七八九十一二三四五六七八九二一二三四五六七八九三一二三四五六七八九四一二三四五六七八九五一二三四五六七八九六一二三四五六七八九七一二三四五六七八九八一二三四五六七八九九一二三四五六七八九十一二三四五六七八九十一二三四五六七八九二一二三四五六七八九三一二三四五六七八九四一二三四五六七八九五一二三四五六七八九六一二三四五六七八九七一二三四五六七八九八一二三四五六七八九九一二三四五六七八九二一二三四五六七八九十一二三四五六七八九二一二三四五六七八九三一二三四五六七八九四一二三四五六七八九五一二三四五六七八九六一二三四五六七八九七一二三四五六七八九八一二三四五六七八九九一二三四五六七八九三一二三四五六七八九十一二三四五六七八九二一二三四五六七八九三一二三四五六七八九四一二三四五六七八九五一二三四五六七八九六一二三四五六七八九七一二三四五六七八九八一二三四五六七八九九一二三四五六七八九四一二三四五六七八九十一二三四五六七八九二一二三四五六七八九三一二三四五六七八九四一二三四五六七八九五一二三四五六七八九六一二三四五六七八九七一二三四五六七八九八一二三四五六七八九九一二三四五六"
