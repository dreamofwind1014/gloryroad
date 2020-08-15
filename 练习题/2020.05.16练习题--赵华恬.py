# coding=utf-8

# 习题6：py2 ：声明str类型变量和unicode变量，
# 将unicode变量变为2个str变量（gbk，utf-8各一次）将utf-8编码的str类型，转换为gbk
# str1 = "水电费了会计师福建省来访接待室浪费空间"
# str2 = u"中国了空间乱收费的健康"
# print(str2.encode("utf-8"))     # 这个编码成utf-8会展示乱码，因为终端是gbk编码
# print(str2.encode("gbk"))
# print(str1.decode("utf-8").encode("gbk"))

# unicode变量可以进行encode，变成str变量
# str类型变量可以decode

# 习题7：判断一个输入的句子中有多少个字母
# 方法一:
"""
1、输入句子
2、循环句子并判断是否为字母计数
3、输出统计数字
"""
# sentence = input('请输入语句>>')
# count = 0
# for i in sentence:
#     if i.isalpha():
#         count += 1
# print(f"输入的句子{sentence}中有{count}个字母")

# 方法二：
"""
1、输入句子
2、循环句子中的每个字符
3、判断句子中的字符是否为字母，在a-z和A-Z中间的为字母
4、输出统计
"""
# sentence = input('请输入语句>>')
# count_j = 0
# for j in sentence:
#     if ((j >= 'a') and (j <= 'z')) or ((j >= 'A') and (j <= 'Z')):
#         count_j += 1
# print(count_j)

# 习题8： 26个字母大小写成对打印，例如：Aa,Bb....
# 方法一
"""
1、循环range(26)
2、记录大写字母和小写字母
3、将大小写字母拼接作为一个值存到list中
4、用','拼接打印list中所有值
"""
# letter_list = []
# upper_first_letter_ASCII = ord('A')
# lower_first_letter_ASCII = ord('a')
# for i in range(26):
#     upper = chr(upper_first_letter_ASCII+i)
#     lower = chr(lower_first_letter_ASCII+i)
#     letter_list.append(upper+lower)
# print(','.join(letter_list))

# 方法二：
# upper_first_letter_ASCII = ord('A')
# lower_first_letter_ASCII = ord('a')
# difference = lower_first_letter_ASCII - upper_first_letter_ASCII
# for i in range(upper_first_letter_ASCII, upper_first_letter_ASCII+26):
#     if i == upper_first_letter_ASCII+25:
#         print(chr(i)+chr(i+difference), end='')
#     else:
#         print(chr(i) + chr(i + difference)+',', end='')

# 习题9、一个list包含10个数字，然后生成新的list，要求，新的list里面的数都比之前的数多1
# old_list = list(range(10))
# new_list = []
# for i in old_list:
#     new_list.append(i+1)
# print(f"{old_list}\n{new_list}")

# 方法二：
"""
1、生成原列表
2、列表生成方法[i(元素进行简单处理) for i in 原列表]的方式生新列表
3、打印列表
"""
# old_list = list(range(10))
# print([num+1 for num in old_list])


# 习题10、倒序取出每个单词的第一个字母
# 方法一:
"""
1、将句子切割成单词列表
2、倒序取列表中的值，用步长
3、取单词的第一个字母打印
"""
# sentence = 'I am a good girl'
# sentence_list = sentence.split(' ')
# for i in sentence_list[::-1]:
#     print(i[0])

# 方法二
'''
1、将原句子切割成单个单词
2、通过索引倒序取出列表中每个单词，取第一个字母
打印
'''
# sentence = "I am a good boy"
# sentence_list = sentence.split(' ')
# for i in range(len(sentence_list)-1, -1, -1):
#     print(sentence_list[i][0])

# 方法三：
"""
1、将句子切割成单词列表
2、倒序排
3、循环倒序后的列表，打印第一个字母
"""
# sentence = 'I am a good boy'
# sentence_list = sentence.split(' ')
# sentence_list.reverse()
# for i in sentence_list:
#     print(i[0])

# 方法四：
"""
1、将句子切割成单词列表
2、倒序排
3、循环倒序后的列表，将每个单词的第一个字母存入结果列表
4、打印结果列表
"""
# sentence = 'I am a good boy'
# sentence_list = sentence.split(' ')
# result = []
# sentence_list.reverse()
# for i in sentence_list:
#     result.append(i[0])
# print(result)

# 习题11：找出s=”aabbccddxxxxffff”中，出现次数最多的字母
# 方法一：
"""
1、将s的每个字母进行数量统计存入字典
2、循环字典，将字典中的value存入list
3、list排序，找到最大值
4、字典循环，value=最大值的，存入list
5、最后最大值value的所有key
"""
# s = 'aabbccddxxxxffff'
# result_dict = {}
# value_list = []
# max_value = None
# result_list = []
# # 统计数量存入字典
# for i in s:
#     if i not in result_dict:
#         result_dict[i] = 1
#     else:
#         result_dict[i] += 1
# print(result_dict)
# # 将字典中所有的value存入list
# for k in result_dict:
#     value_list.append(result_dict[k])
# print(value_list)
# # list排序，找到最大值
# value_list.sort()
# print(value_list)
# max_value = value_list[-1]
# # 字典中value==max_value的key存入list
# for k in result_dict:
#     if result_dict[k] == max_value:
#         result_list.append(k)
# print(result_list)

# 方法二：
"""
1、统计s中字母数量存入字典====可以是用哪个字符串的统计方法和字典的增加dict[key]=value
2、找最大值
3、找最大值的key
"""
s = "aabbccddxxxxffff"
count_dict = {}
# 将字母统计存入字典
for i in s:
    count_dict[i] = s.count(i)
# letter_numbers.values()是取字典的value
# max()是去list中的最大值
# 找到value的最大值
max_times = max(count_dict.values())
# 循环遍历字母统计的字典，找出value==最大值的key
for k, v in count_dict.items():
    if v == max_times:
        print(k)



