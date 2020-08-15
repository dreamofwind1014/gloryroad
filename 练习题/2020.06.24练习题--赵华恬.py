# 练习201：字母游戏
"""
“Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：
(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音
字母。其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。

(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。例如，“ask”变为“askhay”，“use”变为“usehay”。（同上）

(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。
(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。

(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。
输入格式:
一系列单词，单词之间使用空格分隔。
输出格式：
按照以上规则转化每个单词，单词之间使用空格分隔。
输入样例：
Welcome to the Python world Are you ready
输出样例：
elcomeway otay ethay ythonpay orldway arehay ouyay eadyray

"""


# s = "Welcome to the Python world Are you ready"
# result = []
# for v in s:
#     if v.isupper():
#         s = s.replace(v, v.lower())
# s = s.split()
# for word in s:
#     if word[0] in "aeiou":
#         temp1 = word + "hay"
#         result.append(temp1)
#     elif word[0:2] == "qu":
#         temp2 = word[2:] + word[:2] + "ay"
#         result.append(temp2)
#     elif word[0] not in "aeiou":
#         temp = ""
#         index = 0
#         temp += word[0]
#         for i in range(1, len(word)):
#             if word[i] not in "aeiouy":
#                 temp += word[i]
#                 index += 1
#             else:
#                 break
#         result.append(word[index+1:] + temp + "ay")
# print(result)
#
# # elcomeway otay ethay ythonpay orldway arehay ouyay eadyray


# 练习202：实现字符串的upper、lower以及swapcase方法


# uupaer
# def upper(s):
#     result = ""
#     for v in s:
#         if (v >= "a") and v <= "z":
#             v = chr(ord(v) - 32)
#         result += v
#
#     return result
#
#
# print(upper("abC"))
#
#
# def lower(s):
#     result = ""
#     for v in s:
#         if (v >= "A") and v <= "Z":
#             v = chr(ord(v) + 32)
#         result += v
#     return result
#
#
# print(lower("ABc"))
#
#
# def swapcase(s):
#     result = ""
#     for v in s:
#         if v >= "a" and (v <= "z"):
#             result += chr(ord(v) - 32)
#         elif (v >= "A") and v <= "Z":
#             result += chr(ord(v) + 32)
#     return result
#
#
# print(swapcase("ABxy"))


# 练习203：实现字符串的find方法


# def find(s, sub, start=None, end=None):
#     if start is None:
#         start = 0
#     if end is None:
#         end = len(s)
#     sub_length = len(sub)
#     for i in range(start, end):
#         if s[i:i + sub_length] == sub:
#             return i
#     return -1
#
#
# print(find("abcd", "bc"))
# print(find("abcd", "bc", 1))
# print(find("abcd", "bc", 1, 3))
# print(find("abcd", "b1"))


# 练习204：实现字符串的isalpha方法


# def isalpha(s):
#     for v in s:
#         if not (((v >= "a") and v <= "z") or ((v >= "A") and v <= "Z")):
#             return False
#     return True
#
#
# print(isalpha("ABCd"))
# print(isalpha("ABCd1"))
# print(isalpha("ABCd"))


# 练习205：实现字符串的isdigit方法

#
# def isdigit(s):
#     for v in s:
#         if v not in "0123456789":
#             return False
#     return True
#
#
# print(isdigit("8887"))
# print(isdigit("8887a"))


# 共计79行代码

