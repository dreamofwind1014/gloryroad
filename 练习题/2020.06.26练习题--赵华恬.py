# 练习211：报数问题：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位
"""
用一个变量count_num记录总报数次数，每次从头遍历整个列表(位置遍历)，当列表元素不为0的时候（用0标记删除的人）
count_num += 1,每次判断count_num ,如果能被3除尽就把对应位置赋值0
重复以上过程，直到列表包含0的个数等于列表长度-1

最后找出不是0的那个位置就是留下的位置

"""
# lst = [1, 2, 3, 4, 5, 6, 7]
# count_num = 0
# while lst.count(0) < len(lst) - 1:
#     for i in range(len(lst)):
#         if lst[i] != 0:
#             count_num += 1
#         if count_num % 3 == 0:
#             lst[i] = 0
#
# for v in lst:
#     if v != 0:
#         print("最后留下的是原来第 %d 号的人" % v)


# 练习212：由单个字母组成的list，从键盘读入两个整数m、n（n>m），打印出list[m,n]之间的字母能组成的所有n-m+1位不同的字符串
# 能组成的子字符串的个数是字符串长度的阶乘
# 定义一个列表存在子字符串，每次打乱ist[m:],如果其对应的字符串不在结果列表中加入
# 重复上述过程，知道列表长度等于阶乘值
# import random
# import string
# import math
# result = []
# lst = random.sample(string.ascii_letters, 15)
# print(lst)
# while 1:
#     try:
#         m = int(input(">>m: "))
#         n = int(input(">>n: "))
#     except:
#         print("请重新输入:")
#     else:
#         break
# if m > n:
#     m, n = n, m
# print(m, n)
# lst_sub = lst[m:n]
# print(lst_sub)
# max_num = math.factorial(len(lst_sub))
# while len(result) < max_num:
#     random.shuffle(lst_sub)
#     if "".join(lst_sub) not in result:
#         result.append("".join(lst_sub))
# print(result)


# 练习213：：有四个数字：1,2,3,4 ，能组成多少个互不相同且无重复数字的三位数
# result = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and i !=k and j != k:
#                  result.append(str(i)+str(j)+str(k))
# # print result
# print(len(result))

# 练习214：判断 一个文件中有几行含英文单词
# 方式1：
# import string
# count = 0
# with open("e:\\python\\a.txt", "r", encoding="utf-8") as file_obj:
#     contents = file_obj.readlines()
#
# for line in contents:
#     for character in line:
#         if character in string.ascii_letters:
#             # (character >= "a" and character <= "z")or (character >= "A" and character <= "Z")
#             # character.isalpha()
#             count += 1
#             break
# print(count)


# 方式2：

# import string
# count = 0
# with open("e:\\python\\a.txt", "r") as file_obj:
#     for value in file_obj:
#         for c in value:
#             if c in string.ascii_letters:
#                 count += 1
#                 break
#
# print(count)


# 练习215：以r+方式，把一句话追加到文件末尾，然后读出所有文件
# with open("e:\\python\\a.txt", "r+") as file_obj:
#     file_obj.seek(0, 2)#定位到末尾
#     file_obj.write("huhongqiang")
#     file_obj.seek(0, 0)
# print(file_obj.read())

# 共计 70 行代码

