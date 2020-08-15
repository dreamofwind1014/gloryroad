# 练习141：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""
1 考英语
s = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
2 输入一个字符，判断是否在s的所有单词的
第一个字母是否存在
3 有，第一种只有唯一首字母匹配到了，
第二种2个单词的首字母匹配到了。
遍历：判断首字母相同的单词有几个，存个list
如果list长度是1，说明没有重复的天，直接输出
如果List长度是2，说明有2个。再让用户输入一个字母
判断在list的所有单词的第二个是否相等，相等就可以输出
结果了。
"""


# def get_week_day():
#     s = ["Monday", "Tuesday", "Wednesday",
#             "Thursday", "Friday", "Saturday", "Sunday"]
#     result = []
#     first_letter = input("请输入第一个字母: ")
#     for day in s:
#         if day[0] == first_letter.upper():
#             result.append(day)
#     if len(result) == 0:
#         print("你输入的不正确")
#
#     if len(result) == 1:
#         return result[0]
#
#     if len(result) == 2:
#         second_letter = input("请输入第二个字母: ")
#         for day in s:
#             if day[1] == second_letter.lower():
#                 return day
#
#
# if __name__ == "__main__":
#     print(get_week_day())


# 练习142：{'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}拼回："k:1|k1:2|k2:3|k3:4"
# 字典的key取出来，然后用sort或者sorted均可
"""
算法：
1 先把字典的key排序
2 然后按照排序后的key，依次取value，然后使用:,
把key和value做拼接，然后把拼接后的结果存到一个列表里面
3 使用join，使用|将列表的所有元素做拼接

"""

# 方式1:
# 遍历字典的key，把key、”:”、value 拼接成字符串，然后加入列表，最后列表转换为字符串
# d = {'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
# result = []
# for key in sorted(d.keys()):
#     s = key+":"+d[key]
#     result.append(s)
#
# print(result)
# print("|".join(result))

# 方式2：
# 遍历字典的key、value把key\value加入一个临时列表，临时列表用”:”拼接成字符串，加入列表，最后把列表转为为字符串
# d = {'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
#
# result = []
# for k, v in d.items():
#     lst = []
#     lst.append(k)
#     lst.append(v)
#     item = ":".join(lst)
#     result.append(item)
# print("|".join(result))
#
#
# d = {'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
#
# result = ""
# for k, v in d.items():
#     result += (k + ":" + v + "|")
# print(result[:len(result)-1])


# 练习143:生成一个新列表，-1的左边都是小于它的，右边都是大于它的。a= [-1,2,3,-3,0,-5,5]
# a = [-1, 2, 3, -3, 0, -5, 5]
# base = a[0]
# list1 = []
# list2 = []
# for num in a:
#     if num < base:
#         list1.append(num)
#     else:
#         list2.append(num)
# print(list1 + [base] + list2)

# # 练习144：在列表[100, 2, 3, -3, 0, -5, 5]中实现每个元素+1，需要在原列表实现
# a = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(len(a)):
#     a[i] += 1
# print(a)
#
# [x+1 for x in a]
# [101, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# list(map(lambda x: x+1, a))
# [101, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#

# 练习145： 在列表中插入一个新的元素[100, 2, 3, -3, 0, -5, 5]在0的前面插入一个元素10000
# 方式1：
"""
算法：
1 遍历，判断是否0，不是0，把元素插入新列表
2 是0，则把带插入元素插入新列表，然后再插入
0
"""
# result = []
# a = [100, 2, 3, -3, 0, -5, 5]
# target_num = 10000
# for i in a:
#     if i == 0:
#         result.append(target_num)
#         result.append(i)
#     else:
#         result.append(i)
# print(result)

# 方式2:
# 按索引遍历列表，找到0的位置，插入1000，结束遍历
# l = [100, 2, 3, -3, 0, -5, 5]
#
# for i in range(len(l)):
#     if l[i] == 0:
#         l.insert(i, 1000)
#         break
# print(l)


# 共计72行代码

