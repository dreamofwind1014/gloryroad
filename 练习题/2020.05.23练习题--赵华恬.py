# 练习35：长途旅行中，刚到一个加油站，距下一个加油站还有200km，
# 而且以后每个加油站之间距离都是200km。
# 编写一个程序确定是不是需要在这里加油，还是可以等到接下来的第几个加油站再加油
# - 程序询问以下几个问题：
# -  1）你车的油箱多大，单位升
# -  2）目前油箱还剩多少油，按百分比算，比如一半就是0.5
# -  3）你车每升油可以走多远（km）
# - 提示：
# - 油箱中包含5升的缓冲油，以防油表不准
# capacity = int(input("input the capacity: "))
# remain = float(input("input the remain: "))
# distance = int(input("input the distance:"))
#
# remain_distance = (capacity*remain-5)*distance
# if remain_distance < 200:
#     print("当前加油站加油")
# else:
#     print("第%d个加油站加油" % (remain_distance/200))


# 练习36：现有面包、热狗、番茄酱、芥末酱以及洋葱，
# 数字显示有多少种订购组合，其中面包必订，
# 0不订，1订，比如10000，表示只订购面包

# count = 0
# for b in "1":
#     for h in "01":
#         for t in "01":
#             for j in "01":
#                 for y in "01":
#                     print(b + h + t + j + y)
#                     count += 1
# print("共有%d种订购组合:" % count)
#
#
# # 推导列表
# [a+b+c+d for a in "01" for b in "01" for c in "01" for d in "01"]
#
# # eval实现
#
# eval("[" + '(a+b+c+d)' + ''.join(['for %s in "01"' % i for i in 'abcd']) + "]")


# 练习37：基于上题：给出每种食物的卡路里（自定义），再计算出每种组合总共的卡路里
# count = 0
# for b in "1":
#     for h in "01":
#         for t in "01":
#             for j in "01":
#                 for y in "01":
#                     print(b + h + t + j + y, int(b)*100 + int(h)*200 + int(t)*300 + int(j)*400 + int(y)*500)
#                     count += 1


# 练习38：输入5个名字，排序后输出
# names = input("please input the five name sep by , : ")
# names_list = names.split(",")
# print(sorted(names_list))


# 练习39：实现一个简单的单词本
# - 功能：
# - 可以添加单词和词义，当所添加的单词已存在，让用户知道；
# - 可以查找单词，当查找的单词不存在时，让用户知道；
# - 可以删除单词，当删除的单词不存在时，让用户知道；
# - 以上功能可以无限制操作，直到用户输入bye退出程序。
#
# info = """
# add: add the word and word mean
# find: find the word
# del : delete the word
# bye :quit the program
# """
# print(info)
# word_list_dict = {}
# while True:
#     command = input("please input the command:")
#     if command == "add":
#         word = input('input the word: ')
#         word_mean = input("input the word mean: ")
#         if word not in word_list_dict:
#             word_list_dict[word] = word_mean
#         else:
#             print("alreay exists")
#     elif command == "find":
#         word = input('input the find word: ')
#         if word in word_list_dict:
#             print(word_list_dict[word])
#         else:
#             print("not exists")
#     elif command == "del":
#         word = input('input the find word: ')
#         if word not in word_list_dict:
#             print("the delete not exists")
#         else:
#             del word_list_dict[word]
#     elif command == "bye":
#         break


# 练习40：输入一个正整数，输出其阶乘结果
# number = int(input("input the number: "))
# result = 1
# for i in range(1, number + 1):
#     result *= i
# print(result)


# 共65行代码





