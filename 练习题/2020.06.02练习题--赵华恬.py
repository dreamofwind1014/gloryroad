# 练习91：使用必填参数、默认参数、可变元组参数、可变字典参数（value）计算一下单词的长度之和
# def func(a, b="abc", *args, **kwargs):
#     result = 0      # 总长度
#     result += len(a)
#     result += len(b)
#     for v in args:
#         result += len(v)
#     for v in kwargs.values():
#         result += len(v)
#     print("a: ", a)
#     print("b:", b)
#     print("args:", args)
#     print("kwargs: ", kwargs)
#     return result
#
#
# print("长度: ", func("i", "am", "good", "boy", name="hu", sex="f"))
# # print(func("i",c="am"))#b会默认取字符串"abc"


# 练习92：使用map把[1,2,3]变为[2,3,4]
# list(map(lambda x: x+1, [1, 2, 3]))


# 方式2：
# 自定义函数
#
# def func(x):
#     return x+1
#
#
# list(map(func, [1, 2, 3]))


# 练习93：使用map，大写变小写
# list(map(lambda x: x.lower(), "ABC"))
#
# list(map(lambda x: chr(ord(x)+32), "ABC"))


# 练习94：打印2000-3000之间被7整除但不被5整除的数，以，(逗号)分隔
# for i in range(2000, 3000):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=",")


# 练习95：输出9*9口诀表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(str(i) + "*" + str(j) + "=", i*j, " ", end="")
#     print()


# 练习96：计算1 - 1/2 + 1/3 - 1/4 + … + 1/99 - 1/100 + …
# 直到最后一项的绝对值小于10的-5次幂为止
# result = 0.0
# n = 1
# while True:
#     if abs(1/n) < pow(10, -5):
#         break
#     else:
#         if n % 2 == 1:
#             result += 1/n
#             n += 1
#         else:
#             result -= 1/n
#             n += 1
# print(result)


# 练习97：编程将类似“China”这样的明文译成密文，
# 密码规律是：用字母表中原来
# 的字母后面第4个字母代替原来的字母，不能改变其大小写，如果超出了字母
# 表最后一个字母则回退到字母表中第一个字母
# #a b c d e
# #v w x y z
# import sys
#
#
# def encode_password(s):
#     result = ""
#     if not isinstance(s, str):
#         print("请传入字符串")
#         sys.exit(1)
#     for c in s:
#         if ((c >= "a") and c <= "v") or ((c >= "A") and c <= "Z"):
#             result += chr(ord(c) + 4)
#         else:
#             result += chr(ord(c) - 22)
#     return result
#
#
# print(encode_password("China"))


# 练习98：输出以下如下规律的矩阵
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# for i in range(1, 5):
#     for j in range(1, 6):
#         if i == 1:
#             print(j, end=" ")
#         elif i == 2:
#             print(j*2, end=" ")
#         elif i == 3:
#             print(3*j, end=" ")
#         elif i == 4:
#             print(4*j, end=" ")
#     print()


# 练习99：对一个列表求和，如列表是[4, 3, 6]，求和结果是 [4, 7, 13]，
# 每一项的值都等与该项的值加上前一项的值
# 方式1：
# l = [4, 3, 6]
# result = []
#
# for i in range(len(l)):
#     result.append(sum(l[0:i+1]))
# print(result)
#
# # 方式2：
# from functools import reduce
# l = [4, 3, 6]
# result = []
# temp_list = []
# for v in l:
#     temp_list.append(v)
#     result.append(reduce(lambda x, y: x+y, temp_list))
# print(result)


# 练习100：一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip
# ip_list = ["168.1.1.1", "168.1.1.1", "168.1.1.2", "168.1.1.3"]
# ip_dict = {}
# for ip in ip_list:
#     ip_dict[ip] = ip_list.count(ip)
# for k, v in ip_dict.items():
#     if v == max(ip_dict.values()):
#         print("出现次数最多的ip：", k)

# 共计84行代码
