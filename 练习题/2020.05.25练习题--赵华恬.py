# 练习46：自己实现一个函数，在一句话中查找某个单词的算法，存在返回索引号，否则返回False
# 提示：使用句子中的坐标遍历句子的每一个位置，使用查找单词的长度结合使用切片来查找单词。
# 例如：s[i:i+len(单词)]


# def findWord(s, word):
#     length = len(word)
#     for i in range(len(s)-length+1):
#         if s[i:i+length] == word:
#             return i
#     return -1
#
#
# print(findWord("I am a good boy", "good"))
# print(findWord("I am good", "good"))



# 练习47：随机生成一个整数，1-100之间你最多猜5次，如果猜大了，提示大了；
# 小了，提示小了，猜对了，提示猜中。5次都没猜中，就猜没猜中。

# import random
# target_num = random.randint(1, 100)
# for i in range(5):
#     user_input_num = int(input("请输入你猜的数字: "))
#     if target_num == user_input_num:
#         print("你猜中了，数字是：", user_input_num)
#         print("你猜了%d 次" %i+1)
#         break
#     elif target_num > user_input_num:
#         print("你猜小了")
#     else:
#         print("你猜大了")
#     if i == 4:
#         print("5次机会用光了 Bye")



# 练习48：使用while,计算随机数之和，超过100的时候，停止程序。
# 随机数1-20的范围产生，要求记录一下产生的随机数，以及最后的和，以及随机数的个数。

# 方式1：
# import random
#
# result = 0
# random_num_list = []
# while 1:
#     random_num = random.randint(1, 20)
#     random_num_list.append(random_num)
#     result += random_num
#     if result > 100:
#         break
#
# print("一共产生了 %s 个随机数：" % len(random_num_list))
# print("产生随机数如下：", random_num_list)
# print("最后的随机数之和：", result)

# 方式2：
# # encoding=utf-8
# import random
#
# result = 0
# number_list = []
# while result <= 100:
#     num = random.randint(1, 20)
#     number_list.append(num)
#     result += num
#
# print("产生的随机数:", number_list)
# print("随机数的和:", result)
# print("随机数的个数:", len(number_list))


# 练习49：遍历字符串、列表，分别基于位置和和基于字符遍历
# # encoding=utf-8
#
# s = "abc"
# for i in s:
#     print(i)
# for i in range(len(s)):
#     print(s[i])
#
# l = [1, 2, 3]
# for i in l:
#     print(i)
#
# for i in range(len(l)):
#     print(l[i])


# 练习50：遍历一个列表中的嵌套列表和元组的所有元素,将1-12的数字进行输出！
# [[[1,2,3],4,5],7,8,(9,10,(11,12))]
l = [[[1, 2, 3], 4, 5], 7, 8, (9, 10, (11, 12))]

for value in l:
    if isinstance(value, (list, tuple)):
        for v in value:
            if isinstance(v, (list, tuple)):
                for j in v:
                    print(j)
            else:
                print(v)
    else:
        print(value)

# 共计64行


