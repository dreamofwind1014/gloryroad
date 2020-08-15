# 练习111：统计列表中列表的数量
# 方式1：
# a = [1, [2], [3], ""]
# count = 0
# for value in a:
#     if isinstance(value, list):
#         count += 1
# print(count)


# 方式2：
# len(list(filter(lambda x: isinstance(x, list), [1, [2], [3], "a"])))


# 练习112：删除一个列表里面所有的4
# 方式1：
# list(filter(lambda x: x != 4, [1, 2, 3, 4, 4, 4, 5]))

# 方式2：
# a = [1, 1, 1, 2, 3, 4, 4, 4, 5]
# for i in range(a.count(4)):
#     a.remove(4)
# print(a)


# 练习113：删除列表重复元素
# a = [1, 1, 1, 2, 3, 4, 4, 4, 5]
#
# for v in a:
#     for i in range(a.count(v)-1):
#         a.remove(v)
# print(a)


# 练习114：找出boy是第几个单词？
# s = "i am a boy"
#
# print(s.split().index("boy")+1)

# 练习115、求出s中长度最长的字符串
# s = "i am a good boy iii"
#
# # 方式1：
#
#
# def len_2(s):
#     return len(s)
#
#
# s_list = s.split()
#
# sorted_s = sorted(s_list, key=len_2, reverse=True)
# print(sorted_s[0])


# 方式2：
# s = "i am a good boy iii"
# print(sorted(s.split(), key=len, reverse=True)[0])


# 共计26行代码
