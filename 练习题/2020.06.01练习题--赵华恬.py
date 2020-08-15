# 练习86：python代码得到2个列表的交集与差集 不许用set
# 交集思路：遍历list1，判断是否在list2中，在的话，则存入一个列表中。
# 差集思路：分别遍历list1和2，如果不在对方的list中，则存入一个列表中
# list1 = [1, 2, 3, 4]
# list2 = [2, 3, 4, 5, 6, 7]
#
# in_list = []
#
# u_list = []
#
# for v in list1:
#     if v in list2:
#         in_list.append(v)
#
#     elif v not in list2:
#         u_list.append(v)
#
# print("交集: ", in_list)
# print("差集:", u_list)
#
# # 差集2的实现方法：集合本身减去交集
#
# list1 = [1, 2, 3, 4]
# list2 = [2, 3, 4, 5, 6, 7]
#
# in_list = []
#
# diff_list = []
#
# # union_list = list(set(list1 + list2))
#
# for n in list1:
#     if n in list2:
#         in_list.append(n)
#
# for n in list1:
#     if n not in in_list:
#         diff_list.append(n)
# print("差集", diff_list)


# 练习87：求一个字符串中的字母个数函数需判断传入参数的类型。必须使用ascii来判断是否字母
# s = "abcddz122"
#
#
# def letter_number(s):
#     """ 统计一个字符串中字母的个数"""
#     count_letter = 0
#     if not isinstance(s, str):
#         print("参数错误，请重新输入.")
#         return -1
#     else:
#         for c in s:
#             # (ord(c)>=ord("a") and ord(c) <=ord("z") )or (ord(c) >= ord("A") and ord(c) <= ord("Z"))
#             if ((ord(c) >= 97) and ord(c) <= 122) or ((ord(c) >= 65) and ord(c) <= 90):
#                 count_letter += 1
#     return count_letter
#
#
# print(letter_number(s))
# print(letter_number(222))


# 练习88：写一个函数，这个函数要计算浮点数乘法的一万次相乘后的时间耗时，浮点数可以使用随机小数
# def func(n):
#     import time
#     import random
#     start = time.time()
#
#     for i in range(n):
#         random.random() * random.random()
#     print(time.time() - start)
#
#
# func(10000000)

# 练习89:定义函数add(a,b)要求有个值是result来存结果
#
# 1 a,b 数字，相加
# 2 a,b 字符串，就当做字符串相加
# 3 a,b 如果list就当list相加
# import sys
#
#
# def add(a, b):
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         result = 0.0
#     elif isinstance(a, str) and isinstance(b, str):
#         result = ""
#     elif isinstance(a, list) and isinstance(b, list):
#         result = []
#     else:
#         print("参数错误！")
#         sys.exit(1)
#     result = a + b
#     return result
#
#
# print(add(4, 5))
# print(add(4, 5.0))
# print(add("ab", "cd"))
# print(add([1, 2], [3, 4]))
# print(add(4, "a"))


# 练习90：函数参数传入5个字母，声明一个可变参数的函数，拼成一个单词
# def func(a, *args):
#     result = ""
#
#     result += a
#     for v in args:
#         result += v
#     return result
#
#
# print(func("a", "b", "c", "d", "e"))


# 共计67行代码

























