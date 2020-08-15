# 习题16、求一个列表中的最大值
# def max(a):
#     max_num = a[0]
#
#     for i in a:
#         if i > max_num:
#             max_num = i
#     return max_num
#
#
# a = [1, 2, 3, 4, 5]
# print(max(a))

# 习题17：生成9位数字的密码
# 方式1：
# import random
# numbers_password = ""
# for i in range(9):
#     numbers_password += str(random.randint(0, 9))
# print(numbers_password)


# 方式2：
# import random
# numbers_password = ""
# for i in range(9):
#     numbers_password += "0123456789"[random.randint(0, 9)]
# print(numbers_password)

# 习题18、生成9位字母的密码
# import random
# import string
# letters_password = ""
# for i in range(9):
#     letters_password += string.ascii_letters[random.randint(0, 52)]
# print(letters_password)

# 习题19、生成9位数字和字母的密码
# import random
# import string
# number_letter_password = ""
# for i in range(9):
#     # 如果是随机生成的1生成一个字母密码元素
#     if random.randint(0, 1):
#         number_letter_password += string.ascii_letters[random.randint(0, 52)]
#     # 否则生成数字密码元素
#     else:
#         number_letter_password += str(random.randint(0, 9))
#
# print(number_letter_password)

# 习题20、10进制数转换成2进制
# def devTobin(num):
#     result = []
#     while True:
#         result.append(str(num % 2))
#         num = num//2
#         if num == 0:
#             break
#     return "".join(result[::-1])
#
#
# print(devTobin(789))




