# 习题12、自定义count函数，只统计单个字符出现次数情况
# def count_letters(a, letter):
#     times = 0
#     if not isinstance(a, str) or not isinstance(letter, str):
#         return 0
#     else:
#         for i in a:
#             if i == letter:
#                 times += 1
#     return times
#
#
# s = input("请输入要统计的内容>>")
# print(count_letters(s, 'd'))

"""
兼容统计多个字符出现次数的情况
1、首先求出需要查找字符串的长度
2、遍历源字符串，如果当前索引加上子串长度对应的字符串等于要查找字符串的话次数加1
"""

# def count_letters(s, letter):
#     times = 0
#     letter_length = len(letter)
#     if not isinstance(s, str) or not isinstance(letter, str):
#         return 0
#     if letter not in s:
#         return 0
#     else:
#         for i in range(len(s)):
#             if s[i:i + letter_length] == letter:
#                 times += 1
#         return times
#
#
# s = "abcabdab1"
# print(count_letters(s, "ab"))


# 习题13：自定义divmod
# def divmod_2(a, b):
#     c = a//b
#     d = a % b
#     return c, d
#
#
# print(divmod_2(5.5, 2.1))


# 习题14、把字符串中的所有数字去掉
# s = "a1b2c3b4d5dddddd"
# letters_list = []
# for v in s:
#     if v not in "0123456789":
#         letters_list.append(v)
# print("".join(letters_list))
# print("".join([v for v in s if v.isalpha()]))
# print("".join(filter(lambda x: x not in "0123456789", s)))
# print("".join(filter(lambda x: x.isalpha(), s)))

# 习题15、三个数排序
# def sort_2(a, b, c):
#     if a > b:
#         a, b = b, a
#     if a > c:
#         a, c = c, a
#     if b > c:
#         b, c = c, b
#     return a, b, c
#
#
# print(sort_2(3, 1, 9))



