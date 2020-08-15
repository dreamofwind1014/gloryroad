# 练习171：不区分大小写对包含多个字符串对象的列表进行排序，显示排序后的结果还需要显示大小写不变的原字符串
# l = ["Abc", "zhangsan", "gloryroad", "nanjing"]
# print(sorted(l))


# 练习172：一个数如果恰好等于它的因子之和，这个数就称为完数，
# 例如6的因子为1, 2, 3，而6 = 1 + 2 + 3，因此6是完数，
# 编程找出1000之内的所有完数，并按6 its factors are 1, 2, 3 这样的格式输出
# 遍历1000以内的数#用数自身遍历除以小于数自身的数，求约数，所有约数和等于数自身
# for i in range(1, 1000):
#     result = []
# for value in range(1, i):
#     if i % value == 0:
#         result.append(value)
# if i == sum(result):
#     print(i, "its factors are ", end="")
#     for v in result:
#         print(v, end=",")
#     print()


# # 练习173：使用二分法实现在一个有序列表中查找指定的元素
# lst = list(range(100))  # print(lst)
#
#
# def binary_search(arr, item):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == item:
#             return "%d 索引位置是： %d " % (item, mid)
#         elif arr[mid] > item:
#             high = mid - 1
#         elif arr[mid] < item:
#             low = mid + 1
#             print(binary_search(lst, 88))


# 练习174：分离list1与list2中相同部分与不同部分
# list1 = [1, 2, 3, 4, 5, 0]
# list2 = [1, 2, 5, 6, 7, 8, 9]
# same_list = []
# diff_list = []
# for v in list1:
#     if v in list2:
#         same_list.append(v)
#
#     else:
#         diff_list.append(v)
# for v in list2:
#     if v not in list1:
#         diff_list.append(v)
#         print("相同部分:%s" % same_list)
#         print("不同部分:%s" % diff_list)


# 练习175：找出一个多维数组的鞍点，即该位置上的元素在该行上最大，在该列上最小，也可能没有鞍点
# 首先找出每行的最大值，每列的最小值存入两个列表，个数和函数和列数对应#遍历列表的每个元素，
# 如果等于最大值列表和最小值列表对应位置上的值，则是鞍点，否则打印没有鞍点
# l = [
#     [13, 2, 6, 4],
#     [14, 3, 5, 6],
#     [16, 8, 9, 0],
#     [19, 2, 3, 4]
#     ]
#
# row_max_item_list = []
# col_min_item_list = []
# for i in range(len(l)):
#     row_max_item_list.append(max(l[i]))
# print(row_max_item_list)
# for i in range(len(l)):
#     # 存储每列的元素
#     temp_list = []
# for j in range(len(l[i])):
#     temp_list.append(l[j][i])
# col_min_item_list.append(min(temp_list))
# print(col_min_item_list)
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if l[i][j] == row_max_item_list[i] and l[i][j] == col_min_item_list[j]:
#             print("%d 行 %d 列 鞍点是 %d" % (i, j, l[i][j]))
#         else:
#             print("%d 行 %d 列 没有鞍点" % (i, j))


# 共计62行代码
