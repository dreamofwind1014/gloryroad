# 练习136：统计字符串的个数
# l = [1, 2, "s", [1, 23], {1: 2}, (1, 2), set([1, 2]), "b"]
#
# str_number = 0
# for v in l:
#     if isinstance(v, str):
#         str_number += 1
# print(str_number)

# 练习137: 统计列表中所有类型数据的个数
# l = [1, 2, "s", [1, 23], {1: 2}, (1, 2), set([1, 2]), "b"]
#
# d = {"str": 0, "list": 0, "tuple": 0, "int": 0, "set": 0}
# for v in l:
#     if isinstance(v, str):
#         d["str"] += 1
#     elif isinstance(v, list):
#         d["list"] += 1
#     elif isinstance(v, tuple):
#         d["tuple"] += 1
#     elif isinstance(v, set):
#         d["set"] += 1
#     # elif isinstance(v,int):
#     # d["int"] += 1
# print(d)

# 练习138：求列表中所有数字的和，包括数字字符串
# a = [1, 2, 3, [4, 5, 6], {1: 6, 2: 8, "a": "12", 3: 4}]
#
# result = 0
# for value in a:
#     if isinstance(value, int):
#         result += value
#     elif isinstance(value, list):
#         for v in value:
#             if isinstance(v, int):
#                 result += v
#     elif isinstance(value, dict):
#         for key in value.keys():
#             if isinstance(key, int):
#                 result += key
#         for v in value.values():
#             if isinstance(v, int):
#                 result += v
#
#             elif v.isdigit():
#                 result += int(v)
# print(result)

# 练习139：:将字符串："k:1|k1:2|k2:3|k3:4"，
# 处理成python字典：{'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}

# s = "k:1|k1:2|k2:3|k3:4"
# result_dict = {}
#
# s_list = s.split("|")
#
# for v in s_list:
#     key = v.split(":")[0]
#     value = v.split(":")[1]
#     result_dict[key] = value
#
# print(result_dict)

# 练习140：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""
1.
程序分析：在10万以内判断
方式1：

分析：
1
x
在10万里面，x是某个数，不知道是谁
2(x + 100)
开方 = y
y整数，
3(x + +100 + 168)
开方 = z
z
整数
4
开方：math.sqrt
5
怎么判断z
和y
是否整数？
y ** 2
是整数且是x + +100
z ** 2
是整数且是x + +100 + 168
"""

# import math
#
# result = []
# for i in range(100000):
#     x = math.sqrt(i + 100)
#     y = math.sqrt(i + 100 + 168)
#     if (int(x) ** 2 == i + 100) and (int(y) ** 2 == i + 100 + 168):
#         # print(i)
#         result.append(i)
#
# print(result)


# 共计53行代码

