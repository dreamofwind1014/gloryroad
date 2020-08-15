# 练习131:非递归实现生成斐波那契数列


# def fib(n):
#     result = []
#     if n <= 0 or not isinstance(n, int):
#         return result
#     for i in range(n):
#         if i < 2:
#             result.append(1)
#         else:
#             result.append(result[i-1] + result[i-2])
#     return result
#
#
# print("斐波那契数列: ", fib(5))
# print("斐波那契数列: ", fib(-2))

# 练习132：递归求两个数的最大公约数
# 方式1：
"""
算法：
找出两个数的较小数（第一次）
如果两个数除以较小数余数都等于0的话，添加到一个列表中
不然的话继续调用函数自身，并且num - 1
传入到num参数中。
"""


# def max_common_divisor(a, b, num=0, result = []):
#     if num == 0:
#         if a < b:
#             num = a
#         else:
#             num = b
#
#     if a % num == 0 and b % num == 0:
#         print(result)
#         result.append(num)
#     else:
#
#         max_common_divisor(a, b, num - 1)
#
#     return result  # 函数递归调用结束后才会执行此代码
#
#
# print(max_common_divisor(24, 120))

# 方式2：更相减损法


# def get(small, big):
#     if small > big:
#         small, big = big, small
#
#     if small == big:
#         return small
#
#     return get(small, big - small)
#
#
# print(get(30, 24))

# 方式3: 辗转相除法
#
#
# def gain(small, big):
#     if small > big:
#         small, big = big, small
#     if small == 0:
#         return big
#     return gain(small, big % small)

# gain1(10,12)
# 练习133：非递归实现求第n项斐波那契数列值
'''
算法：遍历n，如果n等于0或1直接返回1
如果n >= 2, 记录前面两个项的和，并重新记录新的第1个，第2个数；
'''


# coding=utf-8
# def fib(n):
#     a, b = 1, 1
#     sum = 0
#     if n <= 0 or not isinstance(n, int):
#         return -1
#     for i in range(n):
#         if i < 2:
#             sum = 1
#         else:
#             sum = a + b
#             a = b
#             b = sum
#     return sum
#
#
# print(fib(5))

# 练习134：利用递归，处理嵌套列表，生成列表[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# 定义全局变量：（尽量不使用全局变量）
# l = [1, 2, [3, 4, [5, 6, 7, [8, 9, [10, 11]]]]]
# result = []
#
#
# def func(p):
#     global result
#     for v in p:
#         if not isinstance(v, list):
#             result.append(v)
#         else:
#             func(v)
#     return result
#
#
# print(func(l))

# 练习135：[1, 2, 3, 4, 5]变成[2, 3, 4, 5, 1]
# # 方法1：
# a = [1, 2, 3, 4, 5]
#
# result = []
# result.append(a[-1])
# result.extend(a[0:4])
# print(result)
#
# # 方法2：
#
# result = []
# result.append(a[-1])
# for v in a[0:4]:
#     result.append(v)
# print(result)
#
# # 方法3：
# a = [1, 2, 3, 4, 5]
#
# result = []
#
# for v in a[0:4]:
#     result.append(v)
#
# result.insert(0, a[-1])
# print(result)


# 共计81行代码

