# 练习151: 用推导列表求所有数字key的和
# d = {1: 'a', 2: "b", "a": 3}
# sum([k for k in d if isinstance(k, (int, float))])
# # 3
# 练习152："abcdefgh"里面挑出3个字母进行组合，一共有多少种组合，
# 要求三个字母中不能有任何重复的字母，三个字母的同时出现次数，
# 在所有组合中只能出现一次，例如出现abc了，不能出现cab和bca等
# s = "abcdefgh"
# result = []
# temp_list = []
# for k in s:
#     for v in s:
#         for j in s:
#             if k != v and k != j and v != j:
#                 # sorted("abc") ==》["a","b","c"]
#                 # [sorted(s) for s in result]每一个元素是一个包含三个字母的列表
#                 # if sorted(list(k+v+j))  not in [sorted(list(s)) for s in result]
#                 if sorted(list(k + v + j)) not in [sorted(s) for s in result]:
#                     result.append(k + v + j)
#                     # print(result)
# print("组合数:", len(result))

# 练习153：复制一个列表，不能使用切片和复制的函数进行赋值，尽可能使用少的内置函数
# 方式1:
# lst = ["a", "b", "c", "d", "e"]
#
# length = 0
# i = 0
# for v in lst:
#     length += 1
#
# result = [None] * length
#
# while i < length:
#     result[i] = lst[i]
#     i += 1
#
# print("复制后的列表为:", result)

# 方式2：
# a = ["a", "b", "c", "d", "e"]
#
# arr_length = 0
#
# for i in a:
#     arr_length += 1
#
#
# def iter_arr(n):
#     arr = []
#     i = 0
#     while i <= n - 1:
#         arr += [i]
#         i += 1
#     return arr
#
#
# result = [""] * arr_length
#
# for i in iter_arr(arr_length):
#     result[i] = a[i]
#
# print(result)

# 练习154：d = {-1: 100, -2: 200, 0: 300, -3: 200}
# 按照key的大小顺序升序进行输出，输出key = value - 3 = 200, -2 = 200, -1 = 100, 0 = 300
# 方法一：
# d = {-1: 100, -2: 200, 0: 300, -3: 200}
#
# for k in sorted(d.keys()):
#     print("%s=%s" % (k, d[k]), end=",")

# 方法二：
# d = {-1: 100, -2: 200, 0: 300, -3: 200}
#
# for k, v in sorted(d.items(), key=lambda x: x[0]):
#     print(str(k) + "=" + str(v), end="")


# 练习155：一个字符串排序，排序规则：小写 < 大写 < 奇数 < 偶数,
#  原理：先比较元组的第一个值，FALSE<TRUE，如果相等就比较元组的下一个值，以此类推。

s = '9a13C85c7B24A6b'  # 正确的顺序应该为：abcABC135792468
s = sorted(list(s))

lst = sorted(s, key=lambda x: (
x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isalpha() and x.isupper(), x.isalpha() and x.islower()))
print("".join(lst))
"""
小写 < 大写 < 奇数 < 偶数
偶数(True, True, False, False)
奇数(True, False, False, False)
大写(False, False, True, False)
小写(False, False, False, True)
"""


# 共计52行代码

