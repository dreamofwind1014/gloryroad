# 练习196：有一个已经排好序的列表。现输入一个数，要求按原来的规律将它插入列表中
# num_list = list(range(10))
# num = int(input(">>"))
# for i in range(len(num_list)):
#     if (num > num_list[i]) and num <= num_list[i+1]:
#         num_list.insert(i+1, num)
# print("插入后:", num_list)


# 练习197:统计名字列表中，各名字的首字母在名字列表中出现的次数
# name_list = ["hhq", "rob", "hu", "roni", "zhangsan", "lisi"]
# name_first_letter = []
# for name in name_list:
#     name_first_letter.append(name[0])
# name_first_dict = {}
# for c in name_first_letter:
#     name_first_dict[c] = name_first_letter.count(c)
# print(name_first_dict)

# 方式2：
# name_list = ["hhq", "rob", "hu", "roni", "zhangsan", "lisi"]
# name_first_letter = []
# for name in name_list:
#     name_first_letter.append(name[0])
# name_first_dict = {}
# for c in name_first_letter:
#     if name_first_dict.get(c) is None:
#         name_first_dict[c] = 1
#     else:
#         name_first_dict[c] += 1
# print(name_first_dict)


# 练习198:字符替换
"""
1）读入一个字符串
2）去掉字符串的前后空格
3）如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此类推
4）将字符串使用空格进行切分，存到一个列表，然后使用*号连接，并输出
5）把这些功能封装到一个函数里面，把执行结果作为返回值
"""


# def parse_str():
#     import string
#     s = input(">>")
#     s = s.strip()
#     for v in s:
#         if v == "1":
#             s = s.replace(v, "a")
#         if v == "2":
#             s = s.replace(v, "b")
#         if v == 3:
#             s = s.replace(v, "c")
#     for v in s:
#         if v in string.punctuation:
#             s = s.replace(v, " ")
#     s_list = s.split()
#     return "*".join(s_list)
#
#
# print(parse_str())


# 练习199：找出字符串中出现次数最多的字符，并输出其出现的位置
# str_dict = {}
# result = []
# s = "adsfdsfasadsafasfddssf"
# letter = ""
# for v in s:
#     str_dict[v] = s.count(v)
# for k, v in str_dict.items():
#     if str_dict[k] == max(str_dict.values()):
#         letter = k
# for i in range(len(s)):
#     if s[i] == letter:
#         result.append(i)
# print("出现次数最多的字符:%s,出现位置：%s" %(letter, result))


# 练习200：找出一段句子中最长的单词及其索引位置，以字典返回字符串的练习题
# import string
#
# s = "the pepople republic of china! hhhhhhhh"
# for v in s:
#     if v in string.punctuation:
#         s = s.replace(v, " ")
# result_dict = {}
# max_length_list = []    # 存放最长的字符串
# length = len(sorted(s.split(), key=len)[-1])
# for word in s.split():
#     if len(word) == length:
#         max_length_list.append(word)
# for word in max_length_list:
#     result_dict[word] = s.index(word)
# print(result_dict)


# 共计69行代码

