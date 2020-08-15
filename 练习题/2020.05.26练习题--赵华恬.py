# 练习51：判断一个数是否是素数
# import math
#
#
# def is_prime(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(num))+1):
#             if num % i == 0:
#                 return False
#         return True
#
#
# print(is_prime(13))
# print(is_prime(12))
# print(is_prime(2))


# 练习51：求100以内的素数和
# import math
#
#
# def is_prime(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(num))+1):
#             if num % i == 0:
#                 return False
#         return True
#
#
# result = 0
# for i in range(100):
#     if is_prime(i):
#         result += i
# print(result)


# 练习52：使用 for 的方式，求一下100以内奇数之和

# result = 0
# for i in range(101):
#     if i % 2 == 1:
#         result += i
# print(result)


# 练习53：用户输入多个数字，当输入偶数的时候求和，
# 输入奇数，不求和，输入.（一个点）的时候结束求和，打印求和结果
sum = 0
while True:
    number = input("please input the number: ")
    if number == ".":
        break
    else:
        number = int(number)
        if number % 2 == 0:
            sum += number
print(sum)


# 练习54：嵌套循环输出10-50中个位带有1-5的所有数字:
# 方法1：数字和10取余，判断是否大于0并且小于等于5
# 方法2：将数字转换为str，取各位的字符判断字符是否在1-5内。
# 方法3：拼接数字

# 方法1：
for i in range(10, 51):
    if (i % 10 >= 1) and (i % 10 <= 5):
        print(i)

# 方法2：
for i in range(10, 51):
    if str(i)[1] in "12345":
        print(i)

# 方法3：
for i in "1234":
    for j in "12345":
        print(int(i+j))

# 练习55：输入3个数字，达到3个数字求和，结束程序
result = 0
for i in range(3):
    number = input("please input number: ")
    result += int(number)
print(result)


# 共计62行

