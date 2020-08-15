# 练习156：生成一个字典，key 是26个小写字母a-z，value是她的acsii码
# 方式1:

# d = {}
#
# for k in range(97, 123):
#     d[chr(k)] = k
#
# print(d)
#
# {chr(i): i for i in range(97, 123)}


# 练习157：从键盘输入两个数，并比较其大小，直到输入e/E退出程序
# while 1:
#     first = input('请输入第一个数或e退出程序: ')
#     if first.lower() == "e":
#         break
#     second = input("请输入第二个数或e退出程序: ")
#     if second.lower() == "e":
#         break
#     if first > second:
#         print("%s 大" % first)
#     elif first < second:
#         print("%s 大" % second)
#     else:
#         print("等于")


# 练习158：将列表元素交替地作为建和值来创建字典
# lst = list(range(10))
# d = {}
# for i in range(0, len(lst), 2):
#     d[lst[i]] = lst[i+1]
# print(d)


# 练习159：分别输出字符串中奇数坐标和偶数坐标的字符
# s = "abcljlsjfljl"
# for i in range(0, len(s), 2):
#     print("偶数坐标字符:", s[i])
#     print("奇数数坐标字符:", s[i+1])


# 练习160：将一个字典的 key和value 互换
# dit = dict(name="hhq", sex="M")
# dit1 = dict([("a", 1), ("b", 2), ("c", 3)])
# dit2 = dict(zip([1, 2, 3], [3, 4, 5]))
# print(dit, dit1, dit2)
# result = {}
# for k, v in dit1.items():
#     result[v] = k
# print("key和value交换后:", result)


# 共计35行代码


