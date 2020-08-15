# 练习206：实现字符串的isalnum方法


# def isalnum(s):
#     for v in s:
#         if not (((v >= "a") and v <= "z") or ((v >= "A") and v <= "Z") or (v in "0123456789")):
#             return False
#     return True
#
#
# print(isalnum("abC13"))
# print(isalnum("abC13!"))
# print(isalnum("abC"))


# 练习207：实现字符串的join方法


# def join(seq, join_str=None):
#     if join_str is None:
#         join_str = ""
#
#     result = ""
#     for v in seq:
#         result += (v + join_str)
#     if join_str == "":
#         return result
#     return result[:-1]
#
#
# print(join(["1", "2", "3"]))
# print(join(["1", "2", "3"], "*"))


# 练习208：实现字符串的replace方法
"""
字符串转换为列表
1、首先找出需要替换子串的索引位置，存入一个里列表
2、遍历索引位置列表，替换对应位置的子串
需注意替换索引位置的变化

"""


# def replace(s, sub, dest, times=None):
#     if times is None:
#         times = s.count(sub)
#     sub_index = []  # sub的索引位置
#     sub_length = len(sub)
#     dest_length = len(dest)
#     s = list(s)
#     for i in range(len(s)):
#         if s[i:i + sub_length] == list(sub):
#             sub_index.append(i)
#
#     n = 0  # 记录替换次数
#
#     for index in sub_index:
#         if times > 0:
#             # 每次替换后子串往后移动的位数
#             offset = n * (dest_length - sub_length)
#             # 更新需要替换的index位置
#             index = index + offset
#             s[index: index + sub_length] = list(dest)
#             n += 1
#             times -= 1
#     return "".join(s)
#
#
# print(replace("abca1a", "a", "xy"))
# print(replace("abca1a", "a", "xy", 2))
# print(replace("ab1ab2ab3ab", "ab", "x"))


# 练习209：实现字符串的split方法
"""
1、用一个变量记录遍历字符的位置 index
2、每次遍历字符串，如果从当前字符串开始加上分割符长度不能等于分割符，则当前字符拼接到一个字符串，更新index+=1，直到
碰到分割字符串，index+=拼接字符串长度
3、把拼接的字符串价格一个列表
4、重复以上过程，直到分割次数为0
"""


# def split(s, split_str=None, times=None):
#     if split_str is None:
#         split_str = " "
#     if times is None:
#         times = s.count(split_str)
#
#     index = 0
#     split_str_length = len(split_str)
#     result = []
#     while times > 0:
#         temp = ""
#         for i in range(index, len(s)):
#
#             if s[i:i + split_str_length] != split_str:
#                 temp += s[i]
#                 index += 1
#             else:
#                 index += split_str_length
#                 break
#         result.append(temp)
#         times -= 1
#     result.append(s[index:])
#     return result
#
#
# print(split("a1*b*c*d", "*"))
# print(split("a1*b*c*d", "*", 2))
# print(split("a1 b c d"))
# print(split("a1**b**c**d", "**"))


# 练习210：实现字符串的strip方法


# 分别从开头和结尾开始遍历字符是否是要分割的字符

# 是的话，删除，利用 列表副本删除
# def strip(s, strip_str=None):
#     if strip_str is None:
#         strip_str = "\n\r\t\f "
#
#     lst = list(s)
#     lst_copy = lst[:]
#     for v in lst:
#         if v in strip_str:
#             lst_copy.remove(v)
#         else:
#             break
#     for v in lst[::-1]:
#         if v in strip_str:
#             lst_copy.remove(v)
#         else:
#             break
#     return "".join(lst_copy)
#
#
# print(strip(" \t\r\n\fabc\t\r\n\f"))
# print(strip("####**abc########*", "#*"))

# 共计 84 行代码
