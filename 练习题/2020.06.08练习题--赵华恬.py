# 练习121：二维矩阵转置
# a = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [10, 11, 12]
#   ]
#
# result_list = []
# for i in range(3):
#     list_inner = []
#     # 定义一个list存放新二维数组的每行元素，存放原列表的每列元素
#     for l in a:
#         list_inner.append(l[i])
#     result_list.append(list_inner)
# print(result_list)


# 练习122:删除二维矩阵的第1列

# a = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [10, 11, 12]
#   ]
#
#
# result_list = []
# for l in a:
#     temp_list = []
#     for i in [1, 2]:
#         temp_list.append(l[i])
#     result_list.append(temp_list)
#
# print(result_list)


# 练习123:把一个列表偶数位作为key，奇数位作为value，转换成字典
# 方式1：

# a = [1, 2, 3, 4, 5, 6]
# b = {}
# for i in range(0, len(a), 2):
#     k = a[i]
#     v = a[i+1]
#     b[k] = v
# print(b)
#
# # 方式2：
# a = [1, 2, 3, 4, 5, 6]
# b = {}
#
# for i in range(len(a)-1):
#     if i % 2 == 0:
#         b[a[i]] = a[i+1]
# print(b)


# 练习124：有一个长度为101的数组，存在1-100的数字，有一个是重复的，找出这个重复的数字
# 方式1：
# a = [1, 2, 3, 2]
# temp = 200
# for value in a:
#     if temp == value:
#         print(value)
#     else:
#         temp = value
#
# print(temp)

# 方式2：
# import random
# a = list(range(100))
# random_num = random.randint(0, 99)
# a.insert(random_num, random_num)
# number = [i for i in a if a.count(i) == 2]
# print(number[0])


# 练习125：两个长度相同的list，一个里面的做字典的key，一个里面做字典的value，请写个函数实现。

# def make_dict(list1, list2):
#     result_dict = {}
#     for i in range(len(list1)):
#         if isinstance(list1[i], (list, dict)):#字典的key必须是不可变的对象，list,dict不可以
#             continue
#         else:
#             result_dict[list1[i]] = list2[i]
#     return result_dict
#
#
# a = [1, 2.3, (2, 3), {2: 2}, [1, 2, 3], 2+3j, 3, "aaaa"]
# b = [1, 2, 3, 4, 5, 6, 7, 8]
# print(make_dict(a, b))


# 共计54行代码

