# 练习186：将"gloryroad"按照如下规则进行加密：字母对应的asscii码值进行加密，
# 并且在码值前面加上码值长度，如g对应的码值为ord("g") = 103，
# 则字母g加密结果为31033是ascii的长度。“gloryroad”正确输出加密结果为：
# "31033108311131143121311431112973100"


# def encode_str(s):
#     result = []
#     for v in s:
#         item = str(len(str(ord(v)))) + str(ord(v))
#         result.append(item)
#     return "".join(result)
#
#
# s = "gloryroad"
# print("%s 加密后: %s" % (s, encode_str(s)))

# 练习187：、将上题中的加密字符串进行解密
# 方法1:
# 从头遍历每个字符串，当长度为3、2
# 分别取到后面的ascii码，加入列表，最后把列表拼接成字符串


# def decode_str(s):
#     result = []
#     index = 0
#     length = len(s)
#     while index < length:
#         if s[index] == "3":
#             # 索引位置加上1后才是下一个要的长度值
#             item = s[index + 1: index + 3 + 1]
#             result.append(chr(int(item)))
#             index += 4
#         else:
#             item = s[index + 1: index + 2 + 1]
#             result.append(chr(int(item)))
#             index += 3
#     return "".join(result)
#
#
# s = "31033108311131143121311431112973100"
# print("%s 解密后: %s" % (s, decode_str(s)))

# 方法2：把上述方法合并成步骤

#
# def decode_str(s):
#     result = []
#     index = 0
#     length = len(s)
#     while index < length:
#         item = s[index + 1:index + int(s[index]) + 1]
#         result.append(chr(int(item)))
#         index += (int(s[index]) + 1)
#     return "".join(result)
#
#
# s = "31033108311131143121311431112973100"
# print("%s 解密后: %s" % (s, decode_str(s)))


# 练习188：递归


# def decode_str(s, result=[]):
#     if len(s) == 0:
#         pass
#     else:
#
#         length = int(s[0])
#         item = chr(int(s[1:length + 1]))
#         result.append(item)
#         print(result)
#         decode_str(s[length + 1:])
#
#     return "".join(result)
#
#
# s = "31033108311131143121311431112973100"
# print("%s 解密后: %s" % (s, decode_str(s)))


# 练习189：统计首字母是“a”的单词的个数

#
# s = "akk alklk bkk aaddd"
# count = 0
# for v in s.split():
#     if v[0] == "a":
#         count += 1
# print(count)


# 练习190：单词顺序翻转
# s = "i am a  boy"
# " ".join(s.split()[::-1])
# 'boy a am i'


# 共计56行代码