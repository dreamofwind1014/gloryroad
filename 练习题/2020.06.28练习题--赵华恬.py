# 练习221：文件中有两行内容，在中间再加入一行
# with open("e:\\python\\2.txt", "r+", encoding="utf8") as file_obj:
#     content = file_obj.readlines()
#     content.insert(1, "xyyyyyyyy\n")
# with open("e:\\python\\2.txt", "w", encoding="utf8") as file_obj:
#     file_obj.writelines(content)
#
# with open("e:\\python\\2.txt", "r+", encoding="utf8") as file_obj:
#     content = file_obj.readlines()
#     content.insert(1, "xyyyyyyyy\n")
#     file_obj.seek(0, 0)
# file_obj.writelines(content)

# 练习222: 读一个文件，包含英文句子，请统计共多少个不重复的单词，  # 并且在另外一个文件中打印每个单词以及它的出线次数

# import string
#
# words = ""
# words_dict = {}
# with open("e:\\python\\a.txt") as file_obj:
#     for line in file_obj:
#         for v in line:
#             if not v.isalpha():
#                 line = line.replace(v, " ")
#         words += line
#
# word_list = words.split()
# print("不重复的单词个数:", len(set(word_list)))
# for word in word_list:
#     if words_dict.get(word) is None:
#         words_dict[word] = 1
#     else:
#         words_dict[word] += 1
#
# with open("e:\\python\\101401.txt", "w") as file_obj:
#     for k, v in words_dict.items():
#         file_obj.write("%s出现%d次\n" % (str(k), v))

# 练习223：写个记账程序，每天收入多少，支出多少，总额剩多少，使用序列化方式保存信息

import pickle

fp = open("e:\\a.txt", "rb")
try:
    income = pickle.load(fp)
    spend = pickle.load(fp)
    deposit = pickle.load(fp)
except:
    income = []
    spend = []
    deposit = 0
fp.close()

# value|specification
while 1:
    content = input("请输入指令：")
    if content.find("exit") != -1:
        break

    if content.find("|") == -1:
        print("data format is value|specification")
        print("please input again!")
        continue

        value = content.split("|")[0]
        try:
            value = float(value)
        except:
            print("data format is value|specification")
            print("data format is value must be a number")

        if value > 0:
            income.append(content)
            deposit += value
        elif value == 0:
            print("空间有限，不存0")
        else:
            spend.append(content[1:])
            deposit += value

print(income)
print(spend)
print(deposit)

fp = open("e:\\a.txt", "wb")
pickle.dump(income, fp)
pickle.dump(spend, fp)
pickle.dump(deposit, fp)
fp.close()

# 方式2:

import pickle

income = []
spend = []
deposit = 0.0

while 1:
    command = input("请输入收入、支出和金额，如: 支出>50,输入q退出: ")
    if command.lower() == "q":
        break
    try:
        amount = float(command.split(">")[1])
    except Exception as e:
        print("输入错误，请重新输入")
        continue
    else:
        type = command.split(">")[0]
        if type == "收入":
            income.append(amount)
            deposit += amount
        elif type == "支出":
            if deposit - abs(amount) >= 0:
                spend.append(abs(amount))
                deposit -= amount
            else:
                print("余额不足！")

print("收入:", income)
print("支出:", spend)
print("余额:", deposit)

file_obj = open("e:\\in_out.txt", "wb")

pickle.dump(income, file_obj)
pickle.dump(spend, file_obj)
pickle.dump(spend, file_obj)
file_obj.close()

# 练习224：数据分析需求：每行内容需要生成以每行首年月日为名称的文件，文件内容写入 | 0 | 后的所有行内容（也包括 | 0 | ）
"""
20160215000148 | 0 | collect
info
job
start | success |
20160215000153 | 0 | collect
info
jobend | success | resultcode = 0000
20160216000120 | 0 | collect
info
job
start | success |
20160216000121 | 0 | collect
info
jobend | success | resultcode = 0000
20160217000139 | 0 | collect
info
job
start | success |
20160217000143 | 0 | collect
info
jobend | success | resultcode = 0000
"""


with open("e:\\python\\a.txt") as file_obj:
    for line in file_obj:
        with open(line[:14] + ".txt", "w") as fp:
            fp.write(line[14:])

# 练习225：删除目录下所有的.txt文件

import os

os.chdir("e:\\python1")
for file in os.listdir():
    if ".txt" in file:
        os.remove(file)
