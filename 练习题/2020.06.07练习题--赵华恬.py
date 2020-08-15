# 练习116：L中分别按照学生姓名和学生成绩排序

#
# def by_name(t):
#     return t[0]
#
#
# def by_score(t):
#     return t[1]
#
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L, key=by_name))
# print(sorted(L, key=by_score))

# 练习117：按照句子中每个单词的首字母进行排序，不区分大小写


# def first_letter(s):
#     return s[0].lower()
#
#
# s = "I am A boy iii huhongqiang"
# list1 = s.split()
# list1.sort(key=first_letter)
# print(list1)


# 练习118：按照字符串每个数字的和进行排序
# 方式1：


# def sum(s):
#     result = 0
#     for i in s:
#        result += int(i)
#     return result
#
#
# s = "11 22  33 44 394 55"
# list1 = s.split()
# list1.sort(key=sum, reverse=True)
# print(list1)


# 方式2：

#
# def sum1(s):
#     return sum(map(lambda x: int(x), s))
#
#
# s = "11 22  33 44 394 55"
# list1 = s.split()
# list1.sort(key=sum1, reverse=True)
# print(list1)


# 练习119：将两个list ，连接成[(1,4),(2,5),(3,6)]
# 方式1：
# a = [1, 2, 3]
# b = [4, 5, 6]
# result_list = []
# for i in range(len(a)):
#     result_list.append((a[i], b[i]))
# print(result_list)


# 方式2：
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(list(map(lambda x, y: (x, y), a, b)))


# 方式3：

# print(list(zip(a, b)))

# 练习120:生成二维数组[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# num = 0
# result = []
# for i in range(3):
#     x = []
#     for j in range(3):
#         x.append(num)
#         num += 1
#
#     result.append(x)
#
# print(result)




# 共计47行代码