# 习题21、二进制转换为十进制
# 101 = 1*2^0 + 0*2^1 + 1*2^2 = 5


# def binTodev(binNum):
#     result = 0
#     number_length = len(binNum)
#     for i in range(number_length):
#         # print("i:",i)
#         # print(binNum[i])
#         result += int(binNum[-(i+1)])*pow(2, i)     # 二进制的数要从右边开始取，从-1开始
#     return result
#
#
# print(binTodev("1100010101"))


# 习题22：输入1-127的ascii码并输出对应字符
# for i in range(1, 128):
#     print(chr(i))


# 习题23：输入a，b，c，d4个整数，计算a+b-c*d的结果
# a = int(input("input number a: "))
# b = int(input("input number b: "))
# c = int(input("input number c: "))
# d = int(input("input number d: "))
# print(a + b - c * d)


# 习题24：计算一周有多少分钟、多少秒钟
# print(7*24*60)
# print(7*24*60*60)


# 习题25：3个人在餐厅吃饭，想分摊饭费。
# 总共花费35.27美元，他们还想给15%的小费。
# 每个人该怎么付钱，编程实现
# print(round(35.27*1.15/3, 2))

# 习题26：计算一个12.5m X 16.7m的矩形房间的面积和周长
# print("面积：", 12.5*16.7)
# print("周长：", 2*(12.5+16.7))

# 习题27：怎么得到9 / 2的小数结果
# print((9.0/2))


# 习题28：python计算中7 * 7 *7 * 7，可以有多少种写法
# print(7*7*7*7)
# print(7**4)
# print(pow(7, 4))

# 习题29：写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)
# print(5.0/9*(100 - 32))


# 习题30：一家商场在降价促销。如果购买金额50-100元（包含50元和100元）之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，
# 再显示出折扣（10%或20%）和最终价格
# amount = float(input("input the amount: "))
# if (amount >= 50) and (amount <= 100):
#     print("the sale 0.9.")
#     print("the final price is :", amount*0.9)
# elif amount > 100:
#     print("the sale 0.8.")
#     print("the final price is :", amount*0.8)



# 习题31：求1 + 2 + 3 +….+100
# number_sum = 0
# for i in range(1, 101):
#     number_sum += i
# print(number_sum)


# 习题32：判断一个数n能否同时被3和5整除
# n = 12
# if n % 3 == 0 and n % 5 == 0:
#     print("可以同时被3和5整除")
# else:
#     print("不可以同时被3和5整除")


# 习题33：交换两个变量的值
# a, b = 10, 20
# a, b = b, a
# print(a, b)

# 习题34：一个足球队在寻找年龄在10到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性， f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数
# count = 0
# for i in range(10):
#     age = int(input("please input the age: "))
#     sex = input("please input the sex: m or f ?")
#     if (age >= 10) and (age <= 12) and sex == "f":
#         count += 1
#         print("can join the game.")
#     else:
#         print("can not join the game.")
# print(count)


"""
合计55行
"""

