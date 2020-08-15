# 习题6：py2 ：声明str类型变量和unicode变量，
"""
paas
"""


# 习题7：判断一个输入的句子中有多少个字母
"""
1、接收输入内容
2、从0开始统计
3、遍例输入的内容，输入内容为字符串类型
4、比较输入内容中的每个字符是否是字母，('a'<=i<='z')or('A'<=i<='Z');
"""
# msg = input('请输入>>:')
# count = 0
# for i in msg:
#     if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
#         count += 1
# print('输入的句子中有%s个字母' % count)


# 习题8： 26个字母大小写成对打印，例如：Aa,Bb....
"""
1、循环range(26)
2、大小写字母拼写，放入list
3、用','链接list元素
"""
# letter_list = []
# for i in range(26):
#     letter_list.append(chr(ord('A') + i) + chr(ord('a') + i))
# result = ','.join(letter_list)
# print(result)


# 习题9、一个list包含10个数字，然后生成新的list，要求，新的list里面的数都比之前的数多1
"""
1、循环遍历list
2、遍历元素+1，存入新的list
"""
# old_list = list(range(10))
# new_list = []
# for i in old_list:
#     new_list.append(i+1)
# print(new_list)


# 习题10、倒序取出每个单词的第一个字母
"""
1、输入句子
2、空格切割
"""
# sentence = input(">>:")
# sentence_list = sentence.split(' ')
# sentence_list.reverse()
# print(sentence_list)
# for i in sentence_list:
#     print(i[0])


# 习题11：找出s=”aabbccddxxxxffff”中，出现次数最多的字母
# s = 'aabbccddxxxxffff'
# result = {}
# max_result = []
# for i in s:
#     if i not in result:
#         result[i] = 1
#     else:
#         result[i] += 1
# print(result)
# for i in result.keys():
#     if result[i] == max(result.values()):
#         max_result.append(i)
# print(max_result)

# 35行代码
