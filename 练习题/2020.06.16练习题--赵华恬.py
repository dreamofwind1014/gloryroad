# 练习161：将一个多重嵌套的列表的元素进行互换，存到另一个同等维度的嵌套列表中，例如：[[1, 2, 3], [4, 5, 6]]
# 互换后变成[[1, 4], [2, 5], [3, 6]]
# 方式1：
# lst_1 = [[1, 2, 3], [4, 5, 6]]
# lst_2 = [[1, 4], [2, 5], [3, 6]]
# result_lst = zip([1, 2, 3], [4, 5, 6])
# print(list(result_lst))

# 方式2：
# lst_1 = [[1, 2, 3], [4, 5, 6]]
# result = []
# for i in range(3):
#     temp = []
#     for lst in lst_1:
#         temp.append(lst[i])
#     result.append(temp)
# print(result)


# 练习162：有一个3x4的矩阵，要求编程求出其中值最大的那个元素的值，
# 以及其所在的行号和列号，矩阵可以通过嵌套列表来模拟
# lst = [
#     [1, 2, 3, 4],
#     [4, 5, 1, 3],
#     [8, 4, 9, 0]
# ]
# max_item = lst[0][0]
# for i in range(3):
#     for j in range(4):
#         if lst[i][j] > max_item:
#             max_item = lst[i][j]
#             m, n = i, j
# print("%d 行%d列 元素最大 = %d" % (m + 1, n + 1, max_item))


# 练习163：递归实现嵌套列表求和
# 利用列表
# def list_sum(lst, result=[]):
#     for value in lst:
#         if not isinstance(value, list):
#             result.append(value)
#         else:
#             list_sum(value)
#     return sum(result)
#
#
# lst = [
#     [1, 2, 3, 4],
#     [4, 5, 1, 3],
#     [8, 4, 9, 0]
# ]
# print(list_sum(lst))


# 练习164：打印斐波拉契数列前n项


# def fab(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fab(n - 1) + fab(n - 2)
#
#
# for i in range(10):
#     print(fab(i))
#

# 练习165：检查ipV4的有效性，有效则返回True，否则返回False，（提示使用split函数进行分割）


# def is_ip(ip):
#     for ipNum in ip.split("."):
#         #     print(type(ipNum))
#         if not (ipNum.isdigit() and (int(ipNum) >= 0) and int(ipNum) <= 255):
#
#             print("无效IP")
#             return "无效IP"
#     return "有效IP"
#
#
# ip = "168.2.52.68"
# print(is_ip(ip))


# 共计52行代码

