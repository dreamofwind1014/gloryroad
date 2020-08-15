# 练习56：用户输入不同的数据，当输入的数据达到3个数字的时候，求和结束程序。（数字可以是整数）
# 提示：判断是否整数的方法，isdigit()
# 遍历所有的输入数据，判断是否在0-9的字符串范围内
# 方式1：

# result = 0
# count = 0
# while True:
#     s = input("please input the number: ")
#     for v in s:
#         if v not in "0123456789":   # 如果不是数字跳出当前循环
#             break
#     else:
#         count += 1
#         result += int(s)
#     if count == 3:
#         break
# print(result)

# 方式2：先定义一个判断数字的函数


# def is_int(num):
#     for n in num:
#         if n not in "0123456789":
#             return False
#     return True
#
#
# result = 0
# number_count = 0
# while True:
#     s = input("please input the number: ")
#     if is_int(s):
#         result += int(s)
#         number_count += 1
#     if number_count == 3:
#         break
# print(result)

# 方式3：利用isdigit()函数
# result1 = 0
# count1 = 0
# while True:
#     s = input("please input the number: ")
#     if s.isdigit():
#         count1 += 1
#         result1 += int(s)
#     if count1 == 3:
#         break
# print(result1)


# 练习57：用嵌套列表的方式，遍历输出一个矩阵
# 方式1：
# l = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
# ]
# for i in l:
#     for j in i:
#         print(j, end=" ")
#     print()

# 方式2：
# l = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
# ]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j], end=" ")
#     print()

# 练习58：嵌套列表的正、反对角线之和

# 正对角线之和
# l = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
#     ]
# rusult = 0
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if i == j:
#             rusult += l[i][j]
# print(rusult)

# 反对角线之和
# rusult = 0
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if (i+j) == 2:
#             rusult += l[i][j]
# print(rusult)


# 练习59：求以下矩阵四边元素之和
# l = [
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5]
# ]
#
# # 方法1：
# #
# # 1、第1行和第5行所有元素求和
# # 2、其他行
# # 只要第1列和第5列求和
#
# rusult = 0
#
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if i == 0 or i == 4:
#             rusult += l[i][j]
#         else:
#             if j == 0 or j == 4:
#                 rusult += l[i][j]
# print(rusult)
#
# # 方法2：所有元素之和，减去中间矩阵之和
#
# l = [
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5]
# ]
#
# matrix_element_sum = 0
# sub_matrix_element_sum = 0
#
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         matrix_element_sum += l[i][j]
#
# result_mid = 0
#
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if i == 0 or i == 4:
#             continue
#         else:
#             if j != 0 and j != 4:
#                 sub_matrix_element_sum += l[i][j]
# print(matrix_element_sum - sub_matrix_element_sum)


# 练习60：统计单词中包含字母a的单词个数：
s = "i am a boy!"
count = 0
list1 = s.split()
for value in list1:
    if "a" in value:
        count += 1
print(count)

# :if value.count("a")>0,if value.__contains__("a"), if value.find("a")!=-1,

93
