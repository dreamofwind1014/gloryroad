# 练习61：使用尽可能多的方法实现list去重
# 方法1：利用两个列表，遍历一个列表元素，如果不在另外一个列表，添加进另外一个列表
# orinal_list = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6]
# result_list = []
# for value in orinal_list:
#     if value not in result_list:
#         result_list.append(value)
# print(result_list)
#
# # 方法2：利用set
# orinal_list = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6]
# list(set(orinal_list))

# 方法3：利用字典
# orinal_list = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6]
# result_dict = {}
# for value in orinal_list:
#     result_dict[value] = "a"
# print(list(result_dict.keys()))
#
# # 方法4：#遍历每一个元素，如果当前元素列表包含个数大于1，删除掉
# orinal_list = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6]
# for i in orinal_list:
#     for j in range(orinal_list.count(i)-1):
#         orinal_list.remove(i)
# print(orinal_list)


# 练习62：成绩等级判断 利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示， 60-89分之间的用B表示，60分以下的用C表示
# while 1:
#     try:
#         score = float(input("请输入学生的成绩： "))
#     except:
#         print("成绩输入错误,请重新输入。")
#     else:
#         break
# if score >= 90:
#     print("A")
# elif (score >= 60) and (score <= 89):
#     print("B")
# else:
#     print("C")


# 练习63：实现数学中多项式求和公式的打印
# 比如：a6x^6 + a5x^5 + a4x^4 + a3x^3 + a2x^2 + a1x^1 + a0
# string = ""
# for i in range(6, -1, -1):
#     if i >= 1:
#         string += ("a" + str(i) + "x" + "^" + str(i) + "+")
#     else:
#         string += ("a" + str(i))
# print(string)


# 练习64：统计名字列表中，各名字的首字母在名字列表中出现的次数
# names = ["huhongqiang", "zhangsan", "lisi", "wangwu", "wuda", "ziliao"]
#
# first_letter = []
# first_letter_dict = {}
# for name in names:
#     first_letter.append(name[0])
# # print(first_letter)
#
# for c in first_letter:
#     first_letter_dict[c] = first_letter.count(c)
# print(first_letter_dict)


# 练习65：输入三个数，判断是否能构成三角形 能构成三角形三边关系： 三边都大于零 两边之和大于第三边，两边之差小于第三边
a = int(input("请输入第1条边: "))
b = int(input("请输入第2条边: "))
c = int(input("请输入第3条边: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a - b < c and a - c < b and b - c < a:
            print("可以构成三角形。")
        else:
            print("不可以构成三角形。")
    else:
        print("不可以构成三角形。")
else:
    print("不可以构成三角形。")


# 共计59行代码

