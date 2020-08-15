# 练习101：打印100以内的素数
# import math
#
#
# def is_prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(n) + 1)):
#             if n % i == 0:
#                 return False
#         return True
#
#
# for i in range(1, 101):
#     if is_prime(i):
#         print(i, end=" ")


# 练习102：实现一个简易版的计算器，功能要求：加、减、乘、除，支持多数同时进行计算
# def calc(*args):
#     help_info = \
#         """
#     1:加法
#     2:减法
#     3:乘法
#     4:除法
#         """
#     print(help_info)
#     result = 0.0
#     command = int(input("请输入: "))
#     if command == 1:
#         for v in args:
#             result += v
#     elif command == 2:
#         for v in args:
#             result -= v
#     elif command == 3:
#         for v in args:
#             result = 1.0
#             result *= v
#     elif command == 4:
#         for v in args:
#             result = 1.0
#             result /= v
#     return result
#
#
# print(calc(1, 2, 3))


# 练习103：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
# result = 0.0
# a = 2
# b = 1
# for i in range(20):
#     print(a, b)
#     result += a/b
#     temp = b
#     b = a
#     a = temp + b
# print(result)


# 练习104：画等（腰）边三角形（实心、空心）
# 等边三角形，实心
# for i in range(1, 7):
#     print("\n")
#     for k in range(i, 7):
#         print(" ", end="")
#     for j in range(i):
#         print("*  ", end="")

# 空心

# for i in range(1, 7):
#     print("\n")
#     for k in range(i, 7):
#         print(" ", end="")
#     for j in range(i):
#         if (i >= 3) and i < 6:
#             if j == 0 or j == i-1:
#                 print("*   ", end="")
#             else:
#                 print("    ", end="")
#         else:
#             print("*   ", end="")


# 练习105：画倒等边三角形
# for i in range(1, 7):
#     print()
#     for k in range(i):
#         print(" ", end="")
#     for j in range(i, 7):
#         print(" *", end="")


# 共计69行代码











