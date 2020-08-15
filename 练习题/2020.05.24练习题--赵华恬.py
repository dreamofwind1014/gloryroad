# 练习41：计算存款利息
# - 4种方法可选：
# - 活期，年利率为r1；
# - 一年期定息，年利率为r2；
# - 存两次半年期定期，年利率为r3
# - 两年期定息，年利率为r4
# - 现有本金1000元，请分别计算出一年后按4种方法所得到的本息和。
# - 提示：本息= 本金+ 本金* 年利率* 存款期

# r1 = 0.02
# r2 = 0.05
# r3 = 0.35
# r4 = 0.65
# print("活期：", 1000*r1 + 1000)
# print("一年定期：", 1000*r2 + 1000)
# print("两次半年定息:", 1000*r3 + 1000)
# print("两年定期: ", 1000*r4/2 + 1000)


# 练习42：输入3个数字，以逗号隔开，输出其中最大的数
# numbers = input("please input the three number sep by ',': ")
# num_list = numbers.split(",")
# max_num = int(num_list[0])
# for num in num_list:
#     if max_num < int(num):
#         max_num = int(num)
# print(max_num)


# 练习43：输入一个年份，输出是否为闰年
# 是闰年的条件：
# 能被4整数但不能被100整除，或者能被400整除的年份都是闰年

# year = int(input("please input the year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("是闰年.")
# else:
#     print("不是闰年.")


# 练习44：求两个正整数m和n的最大公约数
# 方式1：
# m = 100
# n = 24
# common_divisor_both = []
# for i in range(2, m+1):
#     if (m % i == 0) and (n % i == 0):
#         common_divisor_both.append(i)
# for j in range(2, n+1):
#     if (m % i == 0) and (n % i == 0):
#         common_divisor_both.append(i)
# print(max(common_divisor_both))


# 方式2：

# m = 100
# n = 24
# common_divisor_both = []
# for i in range(2, m+1):
#     if (m % i == 0) and (n % i == 0):
#         common_divisor_both.append(i)
# for j in range(2, n+1):
#     if (m % i == 0) and (n % i == 0):
#         common_divisor_both.append(i)
# max_common_divisor = 0
# for num in common_divisor_both:
#     if max_common_divisor < num:
#         max_common_divisor = num
# print(max_common_divisor)


# 练习45：设定一个用户名和密码，用户输入正确的用户名和密码，则显示登录成功，
# 否则提示登录失败，用户最多失败3次，否则退出程序。
# 提示：使用while或者for来限定重试的次数，
# 使用input获取用户输入使用 ==判断用户的用户名和密码。
# 方式1：
# username = "hhq"
# password = "123456"
#
# for i in range(3):
#     user = input("please input the username: ")
#     password_1 = input("please input the password: ")
#     if user == username and password_1 == password:
#         print("guess ok")
#         break
#     else:
#         print("guess error")
#
#     if i == 2:  # 输错3次退出
#         print("input times is used out! bye!!")


# 方式2：
# username = "hhq"
# password = "123456"
#
# for i in range(3):
#     user = input("please input the username: ")
#     password_1 = input("please input the password: ")
#     if user == username and password_1 == password:
#         print("guess ok")
#         break
#     else:
#         print("guess error")
#
# else:
#     print("input times is used out! bye!!")

# 共计68行


