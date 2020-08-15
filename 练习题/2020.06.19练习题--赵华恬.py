# 练习176：写一个函数，识别输入字符串是否是符合 python 语法的变量名
# （不能数字开头、只能使用数字和字母以及‘_’）
import string

#
# def check_var(var):
#     if var[0] in "0123456789":  # isdigit()
#         return False
#     for v in var:
#         if not (v in string.ascii_letters or v in string.digits or v == "_"):  # not( v.isalnum() or v == "_"):
#             return False
#         return True
#     print("%s 是合法变量：%s" % ("_abA122", check_var("_abA122")))
#
#
# print("%s 是合法变量：%s" % ("13abc", check_var("13abc")))


# 练习177：一个句子中的所有数字和标点符号删除
# import string
# import re
#
# s = "i am a boy, my age is 19 years ."
# res = ""
# for letter in s:
#     if not letter.isdigit() and letter not in string.punctuation:
#         res += letter
# print(res)
#
# s = "i am a boy, my age is 19 years."
# r = ""
# for letter in s:
#     if letter in string.ascii_letters or letter == " ":
#         r += letter
#
# print("333", r)
#
# for letter in s:
#     if letter in "0123456789":
#         s = s.replace(letter, "")
#     if letter in string.punctuation:
#         s = s.replace(letter, "")
# print(s)
#
# print(" ".join(re.findall(r"\b[a-z]+\b", s)))
#
# print("".join(list(filter(lambda x: re.match(r"\b[a-z]+\b", x), s.split(",.")))))


# 练习178：自定义实现str.capitalize()


# def capitalize(s):
#     first_letter = s[0]
#     if (first_letter >= "a") and first_letter <= "z":
#         first_letter = chr(ord(first_letter) - 32)
#     return first_letter + s[1:]
#
#
# print(capitalize("abc"))


# 练习179：自定义实现str.title()
# 方式1：

# def title(string):
#     temp_str1 = ""
#     temp_str2 = ""
#     for value in string.split():
#         if (value[0] >= "a") and value[0] <= "z":
#             temp_str1 = chr(ord(value[0]) - 32) + value[1:]
#             temp_str2 += temp_str1
#     return temp_str2
#
#
# print(title("hu hong qiang"))

# 方式2：

# def title(s):
#     result_list = []
#     for word in s.split():
#         word_first_letter = word[0]
#         if (word_first_letter >= "a") and word_first_letter <= "z":
#             word_first_letter = chr(ord(word_first_letter) - 32)
#         result_list.append(word_first_letter + word[1:])
#     return "".join(result_list)
#
#
# print(title("hu hong qiang"))

# 练习180：自定义实现str.ljust(numbe)
# def ljust(s, n, fill_char=" "):
#     if (not n >= 1) or (not isinstance(n, int)):
#         return s
#     print_length = n - len(s)
#     if print_length <= 0:
#         return s
#     else:
#         return s + print_length * fill_char
#
#
# print(ljust("abc", 10, "*"))


# 共计64行代码
