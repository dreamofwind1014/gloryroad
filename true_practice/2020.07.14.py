# 习题12、自定义count函数，只统计单个字符出现次数情况
"""
1、首先想要统计的内容和一个想要统计的单字符
2、如果想要统计的内容不是字符串类型没法统计
3、如果想要统计的字符不是字符串类型的没法统计
4、遍例想要统计的内容，查看是否与想要统计的字符一致
5、一致的话累加，不一致的话pass
6、返回统计结果
"""


# def count_letter(sentence, letter):
#     time = 0
#     if not isinstance(sentence, str) or not isinstance(letter, str):
#         return 0
#     else:
#         for i in sentence:
#             if i == letter:
#                 time += 1
#         return time
#
#
# s = input('输入需要统计的内容>>:')
# letter_singer = input('输入需要统计的单个字符>>:')
# print(count_letter(s, letter_singer))


"""
兼容统计多个字符出现次数的情况
1、首先求出需要查找字符串的长度
2、遍历源字符串，如果当前索引加上子串长度对应的字符串等于要查找字符串的话次数加1
"""
"""
1、输入需要统计的内容和想要统计的字符串
2、判断想要统计的内容和字符串是否为字符串，如果有一者不是，就不能进行统计
3、计算统计内容的长度和想要统计字符串的长度
3、需要统计的内容从第一个字符开始遍例切割成想要统计字符串的长度
4、对比切割后的部分和想要统计的字符串是否相等
5、如果相等，次数累计，不一致的话pass
6、返回统计次数
"""


# def count_str(sentence, letter_str):
#     time = 0
#     if not isinstance(sentence, str) or not isinstance(letter_str, str):
#         return 0
#     else:
#         long = len(sentence)
#         count_long = len(letter_str)
#         for i in range(long):
#             if i+count_long <= long:
#                 if sentence[i:i+count_long] == letter_str:
#                     time += 1
#         return time
#
#
# sentence_content = input(">>:")
# count_content = input(">>:")
# print(count_str(sentence_content, count_content))


# 习题13：自定义divmod
"""
1、divmod是求除数和余数的计算
2、判断闯入参数为数字类型
3、做除法取商运算
4、做取余运算
5、返回除数和余数
"""

# def divmod_2(a, b):
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         return "%s和%s不能进行运算" % (type(a), type(b))
#     else:
#         c = a//b
#         d = a % b
#         return c, d
#

#
# print(divmod_2(24, 5))


# 习题14、把字符串中的所有数字去掉
"""
1、判断参数是否为字符串
2、遍例字符串的每个字符
3、如果不是数字，放入列表，如果是数字，不放
4、将列表中的元素拼接出来
"""


# def clean_str(s):
#     if not isinstance(s, str):
#         print("%s不是字符串类型" % s)
#     else:
#         s_list = []
#         for i in s:
#             if not i.isdigit():
#                 s_list.append(i)
#         return ''.join(s_list)
#
#
# content = input('输入要去除数字的字符串>>：')
# print(clean_str(content))


# 习题15、三个数排序
"""
倒序排
1、判断a/b/c是否都为数字类型
2、两两判断
    a>b时，如果b>c,a是最大值，c是最小值；顺序是a,b,c
          否则b<c,b是最小值，判断a和c的大小
                           如果a>c,顺序是：a,c,b
                           如果c>a,顺序是：c,a,b
    b>a时，如果a>c,b是最大值，c是最小值；顺序是b,a,c
          否则c>a,a是最小值，判断b和c的大小，
                            如果b>c，顺序是b,c,a
                            如果c>b，顺序是c,b,a
"""


# def sort_num(a, b, c):
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
#         print('请输入数字类型')
#     else:
#         if a >= b:
#             if a >= c:
#                 if b >= c:
#                     return a, b, c
#                 else:
#                     return a, c, b
#             else:
#                 return c, a, b
#         else:
#             if a >= c:
#                 return b, a, c
#             else:
#                 if b >= c:
#                     return b, c, a
#                 else:
#                     return c, b, a
#
#
# print(sort_num(1, -1, 7))


"""
正序排
1、判断a/b/c是否都为数字类型
2、两两判断
    a>b时，如果b>c,a是最大值，c是最小值；顺序是a,b,c
          否则b<c,b是最小值，判断a和c的大小
                           如果a>c,顺序是：a,c,b
                           如果c>a,顺序是：c,a,b
    b>a时，如果a>c,b是最大值，c是最小值；顺序是b,a,c
          否则c>a,a是最小值，判断b和c的大小，
                            如果b>c，顺序是b,c,a
                            如果c>b，顺序是c,b,a
"""


# def sort_num(a, b, c):
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
#         print('请输入数字类型')
#     else:
#         if a >= b:
#             if a >= c:
#                 if b >= c:
#                     return c, b, a
#                 else:
#                     return b, c, a
#             else:
#                 return b, a, c
#         else:
#             if a >= c:
#                 return c, a, b
#             else:
#                 if b >= c:
#                     return a, c, b
#                 else:
#                     return a, b, c
#
#
# print(sort_num(-1, 2, 1))
"""
正序排
1、a，b，c两两对比，ab，ac，bc
1、如果a>b，ab交换赋值，a会变为较小值
2、如果a>c，ac交换赋值，a会变为最小值
3、这个时候bc作比较，b>c，bc交换赋值，c就是最大值，b是中间值
abc的输出顺序就一直都是从小到大的正序排列

"""


# def sort_3(a, b, c):
#     if not(isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
#         return '只有数字类型才能比较'
#     else:
#         if a > b:
#             a, b = b, a
#         if a > c:
#             a, c = c, a
#         if b > c:
#             b, c = c, b
#         return a, b, c
#
#
# print(sort_3(2, 6, 1))


"""
倒序排
1、a，b，c两两对比，ab，ac，bc
1、如果a<b，ab交换赋值，a会变为较大值
2、如果a<c，ac交换赋值，a会变为最大值
3、这个时候bc作比较，b<c，bc交换赋值，c就是最小值，b是中间值
abc的输出顺序就一直都是从大到小的倒序排列
"""


# def sort_4(a, b, c):
#     # print(n   ot(isinstance(a, (int, float)) and isinstance(b, (int, float)) or isinstance(c, (int, float))))
#     if not(isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
#         return '只有数字类型才能比较'
#     else:
#         if a < b:
#             a, b = b, a
#         if a < c:
#             a, c = c, a
#         if b < c:
#             b, c = c, b
#         return a, b, c
#
#
# print(sort_4(2, 'a', 1))


# 共计67行代码






