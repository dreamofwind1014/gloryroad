# 练习231：分离文件名与扩展名
# import os
# print(os.path.splitext("e:\\python\\1.txt"))

# 练习232：找出某个目录下所有的文件，并在每个文件中写入“gloryroad”
# import os
# for file_or_dir in os.listdir("e:\\python"):
#     os.chdir("e:\\python")
#     if os.path.isfile(file_or_dir):
#         with open(file_or_dir, "w", encoding="utf8") as file_obj:
#             file_obj.write("gloryroad")

# 练习233：如果某个目录下文件名包含txt后缀名，则把文件后面追加写一行“被我找到了！”
# import os
# for file_or_path in os.listdir("e:\\python"):
#     os.chdir("e:\\python")
#     if "txt" in file_or_path:
#         with open(file_or_path, "a", encoding="utf8") as file_obj:
#             file_obj.write("\n被我找到了！")


# 练习234：命题练习:
"""
1） 一个目录下只有文件（自己构造），拷贝几个文件（手工完成）
2 ）用listdir函数获取所有文件，如果文件的创建时间是今天，那么就在文件里面写上文件的路径、
文件名和文件扩展名
3） 如果不是今天创建（获取文件的创建时间，并转化为时间格式，判断是否今天），请删除
4 ）计算一下这个程序的执行耗时
"""


# import os
# import time
# start_time = time.time()
# for file in os.listdir("e:\\test"):
#     os.chdir("e:\\test")
#     # time.localtime(os.path.getctime(file))把文件的创建时间转换为时间元组
#     if time.strftime("%Y-%m-%d") == time.strftime("%Y-%m-%d", time.localtime(os.path.getctime(file))):
#         with open(file, "w", encoding="utf8") as file_obj:
#             file_obj.write(os.path.abspath(file))
#     else:
#         os.remove(file)
# elapse_time = time.time() - start_time
# print("耗时:", elapse_time)


# 练习235：删除某个目录下的全部文件
# import os
# for file_or_dir in os.listdir("e:\\test"):
#     os.chdir("e:\\test")
#     if os.path.isfile(file_or_dir):
#         os.remove(file_or_dir)


# 练习236：统计某个目录下文件数和目录个数
# import os
# file_num = 0
# dir_num = 0
# for file_or_dir in os.listdir("e:\\python"):
#     os.chdir("e:\\python")
#     if os.path.isfile(file_or_dir):
#         file_num += 1
#     elif os.path.isdir(file_or_dir):
#         dir_num += 1
# print("文件数:", file_num)
# print("目录数:", dir_num)

# 共计43行代码

