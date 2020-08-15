# 练习181：自定义实现str.center(numbe)


# def center(s, n, fill_char=" "):
#     if (not n >= 1) or (not isinstance(n, int)):
#         return s
#     print_lenght = n - len(s)
#     if print_lenght <= 0:
#         return s
#     else:
#         return (print_lenght // 2 * fill_char) + s + (print_lenght - print_lenght // 2) * fill_char
#
#
# print(center("abc", 10, "*"))

# 练习182：自定义实现zfill

#
# def zfill(s, n):
#     if (not n >= 1) or (not isinstance(n, int)):
#         return s
#     print_length = n - len(s)
#     if print_length <= 0:
#         return s
#     else:
#         return print_length * "0" + s
#
#
# print(zfill("abc", 10))


# 练习183：自定义实现rfind


# def rfind(s, target_str, pos=None, end=None):
#     if pos == None:
#         pos = 0
#     if end == None:
#         end = len(s) - 1
#     target_str_length = len(target_str)
#     for i in range(len(s) - 1, -1, -1):
#         if （i >= pos） and i <= end:
#             if (s[i:i + target_str_length] == target_str) and (i + target_str_length <= end + 1):
#                 return i
#     return -1


# print(rfind("abcabe", "ab"))

# 练习184：替换abc中的b为1

# s = "abc"
#
# # 1利用列表
#
# s = list(s)
#
# s[1] = "1"
# print("".join(s))
#
# # 2直接拼接
#
# s = s[0] + "1" + s[2]
#
# print(s)
#
# # 3 replace替换
# s = s.replace("b", "1")
# print(s)
#
# # 4利用b分割再拼接
#
# print("1".join(s.split("b")))
#
# # 5 正则sub替换
# import re
#
# print(re.sub(r"b", "1", s))
#
# # 6删除再插入
#
# s = list(s)
#
# s.pop(1)
# s.insert(1, "1")
#
# print("".join(s))


# 练习185：删除一句英文中的所有英文标点。

# import string
# s = "abd`1><>?"
# for v in s:
#     if v in string.punctuation:
#         s = s.replace(v, "")
# print(s)


# 共计51行代码