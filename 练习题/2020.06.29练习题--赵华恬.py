# 练习226: 在当前目录下，找到1小时内新建的所有文件。
"""
算法：
取出某个目录内，1
小时内新建的所有文件名。

算法：遍历这个目录，取到所有的文件每个文件用stat取到创建时间用创建时间和当前时间去比对，是否小于3600放到一个列表里面
"""
# import os
# import time
#
# os.chdir("e:\\python")
# result = []
# for file in os.listdir():
#     if os.path.isfile(file):
#         c_time = os.stat(file).st_ctime
#         if time.time() - c_time < 3600:
#             result.append(file)
#
# print(result)


# 练习227:小练习，把所有的txt文件干掉。新建一个空的子目录xxx，放在某个层级下，,把它删掉
# 方式1:


# import os
# dirs = 0
# files = 0
# for root, dirs, files in os.walk("e:\\testdemo"):
#     os.chdir(root)
#     for dir in dirs:
#         if dir == "xxx":
#             os.rmdir(dir)
#     for file in files:
#         if ".txt" in file:
#             os.remove(file)


# 方式2：

# import os
# import os.path
#
# dir_count = 0
# file_count = 0
# for root, dirs, files in os.walk("e:\\testdemo", topdown=True):
#     print(u"当前目录:", root)   # 打印目录绝对路径
#     for name in files:
#         print(u'文件名：', os.path.join(root, name))    # 打印文件绝对路径
#         if name[-4:] == ".txt":
#             os.remove(os.path.join(root, name))
#         file_count += 1
#     for name in dirs:
#         print(u'目录名：', name)    # 打印目录绝对路径
#         if name == "xxx":
#             os.rmdir(os.path.join(root, name))
#         dir_count += 1
#
# print("目录个数%s" % dir_count)
# print("文件个数%s" % file_count)

# 练习228:统计一个文件夹下所有文件类型

# import os
#
# result = []
# for root, dirs, files in os.walk("e:\\python\\python2"):
#     os.chdir(root)
#     for file in files:
#         post_name = os.path.splitext(file)[1]
#         if post_name != "":
#             result.append(post_name)
#
# print(list(set(result)))
# print(len(list(set(result))))


# 练习229：基础题：
"""
检验给出的路径是否是一个文件：
检验给出的路径是否是一个目录：
判断是否是绝对路径：
检验给出的路径是否真地存:
"""

# import os
#
# print(os.path.isfile("e:\\python\\1.txt"))
# print(os.path.isdir("e:\\python"))
# print(os.path.isabs("e:\\python"))
# print(os.path.exists("e:\\python"))

# 练习230：返回一个路径的目录名和文件名

# import os
#
# print(os.path.dirname("e:\\python\\1.txt"))
# print(os.path.basename("e:\\python\\1.txt"))
#
# print(os.path.split("e:\\python\\1.txt"))


# 共计57行代码

