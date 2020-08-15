# 练习66：实现字典的fromkeys方法
# 例如：
# seq = ('name', 'age', 'sex')
# dict = dict.fromkeys(seq, 10)
# print "New Dictionary : %s" % str(dict)
# 结果：New Dictionary : {'age': 10, 'name': 10, 'sex': 10}


# def fromkeys_2(seq,value):
#     keys_dict = {}
#     for val in seq:
#         keys_dict[val] = value
#     return keys_dict
#
#
# seq = ('name', 'age', 'sex')
# print(fromkeys_2(seq, 10))


# 练习67：键盘读入一字符串，逆序输出
# 方式1：
# string = input("请输入字符串: ")
# print(string[::-1])


# 方式2：
# string = input("请输入字符串: ")
# for i in range(len(string)-1, -1, -1):
#     print(string[i], end="")    # end=""抑制换行

# 练习68：读入一个整数n，输出n的阶乘
# n = int(input("请输入一个整数: "))
# result = 1
# for i in range(1, n+1):
#     result *= i
# print(result)
#
#
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n-1)
#
#
# n = int(input("请输入一个整数: "))
# print(fac(n))

# 练习69：打印1/2, 1/3, 1/4,….1/10
# for i in range(2, 11):
#     if i <= 9:
#         print("1" + "/" + str(i), end=",")
#     else:
#         print("1" + "/" + str(i))

# 练习70：写一个函数实现一个数学公式
# import math
#
#
# def circle_area(r):
#     return math.pi*r*r
#
#
# print(circle_area(2))


# 练习71：输入数字a，n，如a，4，则打印a+aa+aaa+aaaa之和
# a = int(input("请输入数字: "))
# times = int(input("请输入项数: "))
# result = 0
# for i in range(1, times+1):
#     print(int(str(a)*i))
#     result += int(str(a)*i)
# print(result)


# 练习72：求100个随机数之和，随机数要求为0—9的整数
# import random
# result = 0
# for i in range(100):
#     result += random.randint(0, 9)
# print(result)


# 练习73：要求在屏幕上分别显求1到100之间奇数之和与偶数之和
# result_odd = 0      # 奇数
# result_even = 0     # 偶数
# for i in range(1, 101):
#     if i % 2 == 0:
#         result_even += i
#     else:
#         result_odd += i
# print("奇数和: ", result_odd)
# print("偶数和: ", result_even)


# 练习74：输入10个数，并显示最大的数与最小的数
# l = list(range(10))
#
#
# def func(l):
#     max_item = l[0]
#     min_item = l[0]
#     for val in l:
#         if val > max_item:
#             max_item = val
#         elif val < min_item:
#             min_item = val
#     return max_item, min_item
#
#
# max_number, min_number = func(l)
# print("最大数: ", max_number)
# print("最小数: ", min_number)

# 练习75：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出 各位数字。
# number = input("请输入正整数: ")
# print("位数: ", len(number))
# print(number[::-1])


# 共计70行代码













