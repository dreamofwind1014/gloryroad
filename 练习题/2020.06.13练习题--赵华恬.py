# 练习146：在列表中的第三个位置插入10000
# 算法：使用切片把第三个位置前的取到使用切片把位置三后的取到把10000存到一个列表，三个列表相加

# result = []
# a = [100, 2, 3, -3, 0, -5, 5]
# target_num = 10000
# result = a[:2]+[target_num]+a[2:]
# print(result)

# 练习147：[1,-1,2,-2,3,-3] 利用max()排序
# 按长度遍历列表，每次把最大值添加到一个列表，把最大值插入到另一个列表的0位置
# l = [1, -1, 2, -2, 3, -3]
#
# result_asc = []
# result_desc = []
# for i in range(len(l)):
#     result_desc.append(max(l))
#     result_asc.insert(0, max(l))
#     l.remove(max(l))
# print("升序:", result_asc)
# print("降序:", result_desc)
#
# # 利用min()函数升序
# result_2 = []
# l = [1, -1, 2, -2, 3, -3]
# for i in range(len(l)):
#     result_2.append(min(l))
#     l.remove(min(l))
# print(result_2)

# 练习148：a = "abcdefghi"把开头、结尾、中间位置的字母变为1其他字母不变
# s = "abcdefghij"
# l = list(s)
# if len(l) % 2 == 1:
#     l[0], l[-1], l[len(l)//2]= "1", "1", "1"
# else:
#     l[0], l[-1], l[len(l)//2-1:len(l)//2+1] = "1", "1", "1"
# print("".join(l))


# 练习149：找到英文句子中最长的单词
# 方式1：
# 利用sort函数，按照单词长度排序
#
# s = "I am a boyboy! hi,glory road"
#
# for v in s:
#     if not v.isalpha():
#         s = s.replace(v, " ")
# l = s.split()
#
# l.sort(key=len, reverse=True)
# # l.sort(key=lambda x:len(x))
#
# print(l[0])
#
# # 直接找最大值
# s = "I am a boyboy! hi,glory road"
#
# for v in s:
#     if not v.isalpha():
#         s = s.replace(v, " ")
# l = s.split()
# max_length = 0
#
# result = []
# for v in l:
#     if max_length < len(v):
#         max_length = len(v)
# for v in l:
#     if len(v) == max_length:
#         result.append(v)
# print(result[0])


# 练习150:利用推导列表生成10 - 30

# [int(x+y) for x in "123" for y in "0123456789" if int(x+y) <= 30]
# # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# [int(x+y) for x in "123" for y in map(str,range(10)) if int(x+y) <= 30]
# # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


# 共计50行代码

