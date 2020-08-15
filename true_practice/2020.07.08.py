# 习题1：一个列表，排重，不能用set，也不能用字典
"""
1、原列表、空列表
2、循环遍例原列表
3、原列表中的数据在新列表中没有，写入新列表
4、原列表中的数据在新列表中有，不写入新列表
"""
# old_list = list(input('>>英文逗号分割:').split(','))
# new_list = []
# for i in old_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# 习题2：输出大写字母、小写字母、大小写字母、数字、大小写字母和数字

# 大写字母
# 方法一：
"""
1、大写字母：A-Z，循环反查ASCII码+26
2、ASCII转成字符，循环字符相加组成字符串
"""
# upper_letter_result = ''
# for i in range(ord('A'), ord('A')+26):
#     upper_letter_result += chr(i)
# print(upper_letter_result)

# 方法二：
"""
1、26个字母，循环range(26)
2、循环过程中大写字母=chr(ord('A')+i)
3、字符串累加
"""
# upper_letter_result = ''
# for i in range(26):
#     upper_letter_result += chr(ord('A')+i)
# print(upper_letter_result)

# 小写字母
# 方法一：
"""
1、小写字母：a-z，循环反查ASCII码+26
2、ASCII转成字符，循环字符相加组成字符串
"""
# lower_letter_result = ''
# for i in range(ord('a'), ord('a')+26):
#     lower_letter_result += chr(i)
# print(lower_letter_result)

# 方法二：
"""
1、26个字母，循环range(26)
2、循环过程中小写字母=chr(ord('a')+i)
3、字符串累加
"""
# lower_letter_result = ''
# for i in range(26):
#     lower_letter_result += chr(ord('a') + i)
# print(lower_letter_result)

# 大小写字母
# 方法一：
"""
1、大小写字母差值；
2、大写字母：A-Z，循环反查ASCII码+26
3、循环中ASCII转成大写字符，ASCII+差值绝对值，转成小写字母
4、累加（大写字母+小写字母）--得到字符串
"""
# upper_lower_letter_result = ''
# for i in range(ord('A'), ord('A')+26):
#     upper_lower_letter_result += chr(i)+chr(i+(ord('a')-ord('A')))
# print(upper_lower_letter_result)

# 方法二：
"""
1、26个字母，循环range(26)
2、循环过程中大写字母=chr(ord('A')+i)
3、循环过程中小写字母=chr(ord('a')+i)
4、字符串累加
"""
# upper_lower_letter_result = ''
# for i in range(26):
#     upper_lower_letter_result += chr(ord('A') + i)
#     upper_lower_letter_result += chr(ord('a') + i)
# print(upper_lower_letter_result)

# 数字
# 方法一：
"""
1、循环0-9，
2、int转为str，字符相加得字符串
"""
# num_result = ''
# for i in range(10):
#     num_result += str(i)
# print(num_result)

# 方法二：
"""
生成字符串数字的list，然后拼接
"""
# num_list = []
# for i in range(10):
#     num_list.append(str(i))
# result = ''.join(num_list)
# print(result)

# 大小写字母和数字
"""
11、大小写字母差值；
12、大写字母：A-Z，循环反查ASCII码+26
13、循环中ASCII转成大写字符，ASCII+差值绝对值，转成小写字母
14、累加（大写字母+小写字母）--得到字符串
15、循环0-9，
16、int转为str，字符相加得字符串
"""
# # 先拼大小写字母
# upper_lower_letter_result = ''
# for i in range(ord('A'), ord('A')+26):
#     upper_lower_letter_result += chr(i)+chr(i+(ord('a')-ord('A')))
# # 拼数字
# num_result = ''
# for i in range(10):
#     num_result += str(i)
# print(upper_lower_letter_result + num_result)


# 习题3：生成字符串a1b2c3d4e5f6g7h8i9j10
"""
1、循环range(1,11)
2、字母：ord('a')+i-1，数字：str(i)，拼
3、累加拼接
"""
# result = ''
# for i in range(1, 11):
#     res = chr(ord('a') + i - 1) + str(i)
#     result += res
# print(result)


# 习题4：生成字符串a1B2c3D4e5F6g7H8i9J10
"""
1、循环range(1,11)
2、判断 i 取余为1（奇数），字母为小写chr(ord('a')+i-1)
3、判断 i 取余为0（偶数），字母为大写chr(ord('A')+i-1)
4、结果累加 result += 字母+str(i)
# """
# result = ''
# for i in range(1, 11):
#     if i % 2 == 1:
#         letter = chr(ord('a')+i-1)
#     else:
#         letter = chr(ord('A')+i-1)
#     result += letter+str(i)
# print(result)


# 习题5：输出奇数字母和偶数字母到两个列表中：
# 方法一：
"""
1、奇数odd_letter_list，偶数even_letter_list
2、字母：range(ord('a'),ord('a')+26)；range(ord('A'),ord('A')+26)
3、判断 i 为奇数，chr(i)加入到odd_letter_list
4、判断 i 为偶数，chr(i)加入到even_letter_list
"""
# odd_letter_list = []
# even_letter_list = []
# list_range = list(range(ord('a'), ord('a')+26))+list(range(ord('A'), ord('A')+26))
# list_range.sort()
# for i in list_range:
#     if i % 2 == 0:
#         even_letter_list.append(chr(i))
#     else:
#         odd_letter_list.append(chr(i))
# print('奇数字母为：', odd_letter_list, '\n偶数字母为：', even_letter_list)

# 方法二：
# odd_letter_list = []
# even_letter_list = []
# for i in range(26):
#     if (ord('A')+i) % 2 == 1:
#         odd_letter_list.append(chr(ord('A') + i))
#     else:
#         even_letter_list.append(chr(ord('A') + i))
#     if (ord('a')+i) % 2 == 1:
#         odd_letter_list.append(chr(ord('a') + i))
#     else:
#         even_letter_list.append(chr(ord('a') + i))
# print("奇数字母为：", odd_letter_list, "\n偶数字母为：", even_letter_list)


# 共计82行代码
