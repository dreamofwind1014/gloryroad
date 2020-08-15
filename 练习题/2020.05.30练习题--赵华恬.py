# 练习76：求1000以内的所有水仙花数
# （水仙花数：它的每个位上的数字的 n 次幂 之和等于它本身，
# 例如：1^3 + 5^3+ 3^3 = 153）
# num_list = []
# for num in range(1, 1000):
#     n = len(str(num))
#     if n == 2:
#         if int(str(num)[0]) ** 2 + int(str(num)[1]) ** 2 == num:
#             num_list.append(num)
#     elif n == 3:
#         if int(str(num)[0]) ** 3 + int(str(num)[1])**3 + int(str(num)[2]) ** 3 == num:
#             num_list.append(num)
# print(num_list)


# 练习77：编程求s=1!+2!+3!+…..+n!
# n = 5
# s = 0
# t = 1
# for i in range(1, n+1):
#     t *= i
#     s += t
# print(s)


# 练习78：钞票换硬币 把一元钞票换成一分、二分、五分硬币（每种至少一枚），有多种换法，分别有哪些
# remain = 100 - 1 - 2 - 5
# result_list = []
# count = 0
# for i in range(int(remain/1)):
#     for j in range(int(remain/2)):
#         for k in range(int(remain/5)):
#             if(i + 2*j + k*5) == 92:
#                 count += 1
#                 result_list.append((i, j, k))
# print(count)
# print(result_list)


# 练习79：自己实现在一句话中查找某个单词的算法，存在返回索引号，否则返回False
# s = "you are a beautiful girl good"
#
#
# def find_word(s, word):
#     length = len(word)
#     for i in range(len(s)):
#         if s[i:i+length] == word:
#             return i
#     return False
#
#
# print(find_word(s, "girl"))


# 练习80：读入一个十进制整数，实现十进制转二进制算法将其转成二进制数
# 要求：不能使用现成进制转换函数，自己写代码实现


# def dec_to_bin(num):
#     remainder_list = []
#
#     while True:
#         temp = num % 2
#         num = num // 2
#         remainder_list.append(str(temp))
#         if num == 0:
#             break
#     return remainder_list[::-1]
#
#
# print("".join(dec_to_bin(789)))

# 共计46行代码

