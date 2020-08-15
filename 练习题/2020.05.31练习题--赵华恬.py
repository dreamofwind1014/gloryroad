# 练习81：读入一组数字，然后把每组数字加1后输出，比如 123，输出234
# 方式1：
# number = input("please input the number: ")
# list2 = []
# for value in number:
#     list2.append(str(int(value)+1))
#
# print("".join(list2))
#
# # 方式2：
# int("".join(map(lambda x: str(int(x)+1), "123")))
#
#
# # 方式3：
# "".join([str(int(x)+1) for x in "123"])     # 列表解析


# 练习82：随机生成10位密码 包含大小写、数字
# import string
# import random
#
#
# def get_random_elements(s, length):
#     a = list(s)
#     random.shuffle(a)
#     return a[:length]
#
#
# def get_random_password():
#     return "".join(get_random_elements(string.ascii_uppercase, 4)+get_random_elements(string.ascii_lowercase, 4) + get_random_elements(string.digits, 3))
#
#
# print(get_random_password())


# 练习83：删除一个字符串中的小写字母（map）
# 方式1:
# import string
#
#
# def del_lowercase(x):
#     if x in string.ascii_uppercase:
#         return x
#     else:
#         return ""
#
#
# print("".join(map(del_lowercase, "abDfDDDflll")))
# # 方式2：
#
#
# def del_lowercase(s):
#     str = ""
#     for x in s:
#         if x in string.ascii_uppercase:
#             str += x
#     return str
#
#
# print(del_lowercase("abDfDDDflll"))


# 练习84：大于5的数字输出（filter）
# 方式1：
# list(filter(lambda x: x > 5, [1, 2, 5, 6, 7, 8]))
#
# # 方式2：
#
#
# def greate_five(x):
#     if x >= 5:
#         return x
#     # else:
#         # return None
#
#
# print(list(filter(greate_five, [4, 5, 6, 7, 8])))


# 练习85：找到列表中第二大的数，可以用多种方法解决
# 思路1：
# 找到最大的，删除掉，再找最大的
# list2 = [2, 3, 4, 5, 6, 7]
# max_number = max(list2)
# list2.remove(max_number)
# # list2.remove(max(list2))
# print("第二大的数:", max(list2))
#
# # 思路2：
# # 排好序找倒数第二个
# list2 = [2, 3, 4, 5, 6, 7]
#
# print("第二大的数:", sorted(list2)[-2])
#
#
# # 思路3：
# # 遍历，声明两个变量，一个存最大的
# # 一个存第二大的，然后逐一比对。
#
# list2 = [2, 3, 4, 5, 6, 7]
#
# max_number = list2[0]
# second_max_number = list2[0]
#
# for n in list2:
#     if n > max_number:
#         second_max_number = max_number
#         max_number = n
#
# print("第二大的数:", second_max_number)

# 共计52行代码