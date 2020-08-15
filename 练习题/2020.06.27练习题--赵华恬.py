# 练习216：把一个文件内容中的boy替换成xxx
# 方式1：

# with open("e:\\python\\a.txt", "r") as fp:
#     contents = fp.readlines()
#
# with open("e:\\python\\1.txt", "w") as fp2:
#     for line in contents:
#         fp2.write(line.replace("boy", "xxx"))

# 方式2：
#
# with open("e:\\python\\a.txt", "r+") as fp:
#     content = fp.read()
#     content = content.replace("xxx", "boy")
#     fp.seek(0, 0)
# fp.write(content)

# # 方式3:
# with open("e:\\python\\a.txt", "r+") as fp:
#     contents = fp.readlines()
#     print(contents)
#     fp.seek(0, 0)
#     for line in contents:
#         fp.write(line.replace("boy", "xxx"))

# 练习217:一个文件拆分成5个文件

# file_obj1 = open("e:\\python\\a.txt", "r", encoding="utf-8")
# file_no = 1
# file_line = 0
# backup_content = ""
# for line in file_obj1:
#     file_line += 1
#     backup_content += line
#     if file_line % 2 == 0:
#         with open("e:\\python\\new"+str(file_no)+".txt", "w", encoding="utf-8") as file_obj2:
#             file_obj2.write(backup_content)
#         file_no += 1
#         backup_content = ""


# 练习218:过滤掉一个文件中空行
# with open("e:\\python\\1.txt", "r", encoding="utf-8") as file_obj1:
#     for line in file_obj1:
#         if line.strip() == "":
#             continue
#         with open("e:\\python\\0521.txt", "a", encoding="utf-8") as file_obj2:
#             file_obj2.write(line)


# 练习219:处理数据文件
"""
数据文件：data.log
20160215000148|0|collect info job pos|success|
20160215000153|0|collect info job end|success|resultcode = 0000
20160216000120|0|collect info job pos|success|
20160216000121|0|collect info job end|success|resultcode = 0000
20160217000139|0|collect info job pos|success|
20160217000143|0|collect info job end|success|resultcode = 0000


数据分析需求：
每行内容需要生成以每行首年月日为名称的文件，文件内容写入|0|后的所有行内容（也包括|0| ）
算法分析：
遍历每一行，每行取头8个字母
新建文件，文件名为首8个字母，然后把第15字符后的所有字
符拷贝到文件中
关闭文件
"""

#
# with open("e:\\python\\a.txt", "r", encoding="utf-8") as file_obj:
#     for line in file_obj:
#         with open("e:\\python\\"+str(line[:14])+".txt", "w", encoding="utf-8") as file_obj2:
#             file_obj2.write(line[14:])

# 练习220:删除一个目录下文件

# import os
# import os.path
# os.chdir("e:\\python2")
# list1 = os.listdir("e:\\python2")
#
# for content in list1:
#     if os.path.isfile(content):
#         os.remove(content)


# 共计 45 行代码

