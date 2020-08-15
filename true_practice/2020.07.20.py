# 习题15、三个数排序

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


# 习题16、求一个列表中的最大值
"""
1、判断列表中的元素都是数字类型，不全部是数字类型的无法计算
2、预设最大值为list[0]
3、循环列表中的所有元素，与最大值进行比较，如果小于预设最大值，预设最大值不变
4、如果大于预设最大值，赋值给预设最大值
5、列表循环完成，最大值求出
"""


# def max_num(list_a):
#     result = ''
#     max_1 = list_a[0]
#     for i in list_a:
#         if not isinstance(i, (int, float)):
#             result = '列表里含有不是数字类型的元素'
#             break
#     else:
#         for i in list_a:
#             if i > max_1:
#                 max_1 = i
#         result = max_1
#     return result
#
#
# print(max_num([3, 5, 'a', 15, 2, 22, 6]))


# 习题17：生成9位数字的密码
"""
1、随机模块导入
2、9位数字，循环9次随机生成单数字进行拼接
"""
# import random
# number_password = ''
# for i in range(9):
#     number_password += str(random.randint(0, 9))
# print(number_password)

# 习题18、生成9位字母的密码
"""
1、随机模块和string模块导入
2、生成所有的大写字母：string.ascii_uppercase
3、生成所有的小写字母：string.ascii_lowercase
4、生成所有的字母：string.ascii_letters
2、9位字母，循环9次随机生成单字母进行拼接
随机生成单字母，区分大小写：

"""
# import random
# import string
# letter_password = ''
# string_random = string.ascii_letters
# for i in range(9):
#     letter_password += random.choice(string_random)
# print(letter_password)


# 习题19、生成9位数字和字母的密码
"""
1、随机模块和string模块导入
2、string模块生成所有的大小写字母
3、随机范围：大小写字母+'0123456789'
4、9位字母，循环9次随机从范围内取出一个作为一位密码
5、随机取出的一位拼接成一串9位的密码
"""
# import random
# import string
# random_range = string.ascii_letters + '0123456789'
# random_password = ''
# for i in range(9):
#     random_password += random.choice(random_range)
# print(random_password)


# 习题20、10进制数转换成2进制
"""
10进制转2进制
一直出2，余数做为每位额数字，从右往左
得到一位数字后，用商再除以2，循环，直到商为0
"""
# num = 3
# result = []
# while True:
#     result.insert(0, str(num % 2))
#     if num == 0:
#         break
#     # result.append(str(num % 2))
#     num = num // 2
#     # print(result)
#
# # print(result)
# print(int(''.join(result)))


# def bin_2(num):
#     result = []
#     while True:
#         result.insert(0, str(num % 2))
#         if num == 0:
#             break
#         num = num//2
#     return int(''.join(result))
#
#
# print(bin_2(8))

# 共计53+46行代码：3

