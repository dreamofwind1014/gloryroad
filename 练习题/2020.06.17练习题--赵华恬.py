# 练习166：检测密码强度
"""
c1: 长度 >= 8
c2: 包含数字和字母
c3: 其他可见的特殊字符
强：满足c1, c2, c3
中: 只满足任一2个条件
弱：只满足任一1个或0个条件
"""
#
# import operator
# import string
#
#
# def check_len(s):
#     if len(s) >= 8:
#         return True
#     else:
#         return False
#
#
# def check_digit_letter(s):
#     digit_flag = False
#     letter_flag = False
#     for v in s:
#         #         print(v)
#         if v in string.ascii_letters:
#             letter_flag = True
#         if v in string.digits:
#             digit_flag = True
#         #     print(digit_flag,letter_flag)
#     if digit_flag and letter_flag:
#         return True
#     else:
#         return False
#
#
# def check_other(s):
#     for v in s:
#         if v in string.punctuation:
#             return True
#
#     return False
#
#
# passwd_1 = "Hhq123456!"
# passwd_2 = "Hhq123456"
#
# passwd_3 = "Hhq!"
#
# passwd_4 = "Hhq"
#
#
# def check_password(s):
#     if check_len(s) and check_digit_letter(s) and check_other(s):
#         return "强"
#     elif check_len(s) and check_digit_letter(s):
#         return "中"
#     elif check_len(s) and check_other(s):
#         return "中"
#     elif check_digit_letter(s) and check_other(s):
#         return "中"
#     elif check_len(s) or check_digit_letter(s) or check_other(s):
#         return "弱"
#     else:
#         return "弱"
#
#
# print(check_password(passwd_1))
# print(check_password(passwd_2))
# print(check_password(passwd_3))
# print(check_password(passwd_4))
# # print(check_len(passwd_4))
# # print(check_digit_letter(passwd_4))
# # print(check_other(passwd_4))

# 练习167：求两个集合的交集和并集
# lst_1 = [1, 2, 3, 4]
# lst_2 = [1, 4, 2, 6]
# in_list = []
# u_list = []
# for v in lst_1:
#     if v in lst_2:
#         in_list.append(v)
#
# for v in lst_1:
#     if v not in u_list:
#         u_list.append(v)
# for v in lst_2:
#     if v not in u_list:
#         u_list.append(v)
# print("交集: ", in_list)
# print("并集:", u_list)


# 练习168：一个包含多个数字的列表，请使用随机的方式，将每个数字 + 1后，生成新列表
# import random
#
# lst = [1, 4, 2, 6]
# rand_list = []
# while 1:
#     rand_index = random.randint(0, 3)
#     if rand_index not in rand_list:
#         lst[rand_index] += 1
#         rand_list.append(rand_index)
#     if len(rand_list) == 4:
#         break
# print(lst)


# 练习169：判断一个字符串是否为回文字符串，所谓回文字符串，就是一个字符串，
# 从左到右读和从右到左读是完全一样的。比如"level" 、 “aaabbaaa”

# def func(s):
#     if len(s) % 2 == 1:
#         #         print(s[:len(s)//2],s[-1:-len(s)//2:-1])
#         if s[:len(s) // 2] == s[-1:-len(s) // 2:-1]:
#             return True
#         else:
#             return False
#     if len(s) % 2 == 0:
#         if s[:len(s) // 2 - 1] == s[-1:-len(s) // 2:-1]:
#             return True
#         else:
#             return False
#
#
# s = "level"
# s2 = "aaabbaaa"
# print("%s是回文:%s " % (s, func(s)))
# print("%s是回文:%s " % (s2, func(s2)))
#
#
# def f(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False
#
#
# s = "level"
# s2 = "aaabbaaa"
# print("%s是回文:%s " % (s, f(s)))
# print("%s是回文:%s " % (s2, f(s2)))
# print(f("1"))


# 练习170：实现合并同类型的有序列表算法，要求不能有重复元素
# 方式1：
# lst1 = [1, 1, 2, 3, 4]
# lst2 = [2, 3, 4, 5, 5, 8]
# lst = set(sorted(lst1 + lst2))
# print(lst)

# 方式2：
# 写算法
# lst1 = [1, 1, 2, 3, 4]
# lst2 = [2, 3, 4, 5, 5, 8]
# result = []
# while lst1 and lst2:
#     if lst1[0] < lst2[0]:
#         item = lst1.pop(0)
#         if item not in result:
#             result.append(item)
#     else:
#         item = lst2.pop(0)
#         if item not in result:
#             result.append(item)
#
# if lst1:
#     result.extend(lst1)
# elif lst2:
#     result.extend(lst2)
# print(result)


# 共计123行代码

