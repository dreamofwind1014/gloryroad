# 练习106：画直角三角形（实心、空心）
# 实心
# for i in range(1, 7):
#     print()
#     for k in range(i):
#         print("* ", end="")

# 空心
# for i in range(7):
#     print()
#     for k in range(i):
#         if (i >= 3) and i <= 5:
#             if k == 0 or k == i - 1:
#                 print("* ", end="")
#             else:
#                 print("   ", end="")
#         else:
#             print("*  ", end="")


# 练习107：要求实现一函数，该函数用于求两个集合的差集，
# 结果集合中包含所有属于第一个集合但不属于第二个集合的元素
# def diff_set(s1, s2):
#     diff_set = []
#     for v in s1:
#         if v not in s2:
#             diff_set.append(v)
#     return set(diff_set)
#
#
# set_1 = {1, 2, 3, 4, 9}
# set_2 = {1, 2, 3, 5, 6, 7}
# print(diff_set(set_1, set_2))


# 练习108：找出一段句子中最长的单词及其索引位置，以list返回

# def find_max_length(ss):
#     import string
#     for c in ss:
#         if c in string.punctuation:
#             ss =ss.replace(c, " ")
#     print(ss)
#     max_length_word = sorted(ss.split(), key=len, reverse=True)[0]
#
#     max_length_word_index = 0
#     max_length = len(max_length_word)
#     for i in range(len(ss)):
#         if ss[i:i+max_length] == max_length_word:
#             max_length_word_index = i
#     return max_length_word, max_length_word_index
#
#
# s = "i am a good boy,huhongqiang!"
# print("最长的单词是%s,索引位置是%d" % find_max_length(s))


# 练习109：返回序列中的最大数


# def max_number(seq):
#     import sys
#
#     if not isinstance(seq, (list, tuple, str)):
#         print("参数传入错误。")
#         sys.exit(1)
#     max_number = 0.0
#     if isinstance(seq, str):
#         for v in seq:
#             if float(v) > max_number:
#                 max_number = float(v)
#     else:
#         for v in seq:
#             if v > max_number:
#                 max_number = v
#     return max_number
#
#
# print(max_number("123456"))
# print(max_number([1, 2, 3, 4, 5, 50]))
# print(max_number((1, 2, 3, 4, 5, 50)))


# 练习110：把一个字典的 key,value互换

# dict1 = {"a": 1, "b": 2}
# dict2 = {}
# for key, value in dict1.items():
#     dict2[value] = key
# print(dict2)


# 共计61行代码
