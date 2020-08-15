# 练习126：统计一个字符串中每一个字母累计出现的次数
# 方式1：

# s = "aabbcccddddeeeeffffffff"
# dict_count = {}
# for value in s:
#     dict_count[value] = s.count(value)
# print(dict_count)

# 方式2：

# s = "aabbcccddddeeeeffffffff"
# d2 = {}
# for value in s:
#     if d2.get(value, None) is not None:
#         d2[value] += 1
#     else:
#         d2[value] = 1
# print(d2)


# 练习127：统计一个字符串中每个单词出现的次数
# s = "I am a boy a good boy a bad boy"
# d = {}
# for value in s.split():
#     d[value] = s.count(value)
# print(d)


# 练习128:习题1：生成[“z1”,”y2”,”x3”,”w4”,”v5”]

# result = []
# for i in range(1, 6):
#     result.append(chr(122-i+1)+str(i))
# print(result)
# 练习129：习题2：拼接一个字符串的首字母、末尾字母、中间字母为一个字符串
# 要考虑奇数偶数长度，如果只有1个2个字母的字符串

# # 方式1：直接拼字符串
# s = "abcdefghig"
#
# result_str = ""
# result_str += s[0]
#
#
# if len(s) % 2 == 1:
#     middle_letter = s[len(s)//2]
# else:
#     middle_letter = s[len(s)//2-1]
#     middle_letter += s[len(s)//2]
#
# print(middle_letter)
# result_str += middle_letter
#
# result_str += s[-1]
#
# print("拼接后的字符串: ", result_str)


# 方式2：利用列表


# def join_str(s):
#     result = []
#     result.append(s[0])
#
#     if len(s) % 2 == 1:
#         result.append(s[len(s)//2])
#     else:
#         result.append(s[len(s)//2-1])
#         result.append(s[len(s)//2])
#
#     result.append(s[-1])
#     return "".join(result)
#
#
# s = "abcdefghig"
# s2 = "abcdefghi"
# print("拼接后的字符串: ", join_str(s))
# print("拼接后的字符串: ", join_str(s2))


# 练习130：S = “i am, a    boy ”把boy替换为m
# 利用切片赋值特性

# 算法：先把字符串转换为列表
#       遍历列表，找到boy字符串
#       替换boy字符串为m


# s = "i am, a    boy!!"
#
# list_s = list(s)
# sub_length = len("boy")
#
# for i in range(len(list_s)):
#     if "".join(list_s[i:i+sub_length]) == "boy":
#         list_s[i:i+sub_length] = "m"    # 可以用切片直接替换
# print("".join(list_s))


# 共计55行代码


