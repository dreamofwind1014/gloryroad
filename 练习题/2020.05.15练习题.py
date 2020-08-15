# 习题1：一个列表，排重，不能用set，也不能用字典

"""
1、空列表
2、循环原列表
3、如果空列表中没有，则添加，如果有则跳过
"""
# start_list = list(input('请输入list元素，以英文逗号","分割>>').split(','))
# result = []
# for i in start_list:
#     if i not in result:
#         result.append(i)
# print(result)

# 习题2：输出大写字母、小写字母、大小写字母、数字、大小写字母和数字
"""
1、A:65;a:97;
"""
# upper = ''
# for i in range(26):
#     upper += chr(65+i)
# print(upper)
#
# lower = ''
# for i in range(26):
#     lower += chr(97+i)
# print(lower)
#
# upper_lower = ''
# for i in range(26):
#     upper_lower += chr(65+i)
#     upper_lower += chr(97+i)
#
# print(upper_lower)
# print(upper+lower)
#
# number = ''
# for i in range(10):
#     number += str(i)
# print(number)
#
# print(upper+lower+number)
# print(upper_lower+number)

# 习题3：生成字符串a1b2c3d4e5f6g7h8i9j10
"""
1-10，a-j，10个数字，
range(1,11),或者range(10)运行时+1
a：97
"""
# letter = ''
# for i in range(10):
#     letter += chr(97+i)
#     letter += str(i+1)
# print(letter)
#
#
# letter1 = ''
# for i in range(1,11):
#     letter1 += chr(97+i-1)
#     letter1 += str(i)
# print(letter)
#
# letter_list = []
# for i in range(10):
#     letter_list.append(chr(97+i))
#     letter_list.append(str(i+1))
# print(''.join(letter_list))
#
# first_letter_ASCII = ord('a')
# letter3 = ''
# for i in range(10):
#     letter3 += chr(first_letter_ASCII+i)
#     letter3 += str(i+1)
# print(letter3)

# 习题4：生成字符串a1B2c3D4e5F6g7H8i9J10
"""
1、奇数前面跟的是小写字母
2、偶数前面跟的是大写字母
3、%判断奇偶数
"""
# 方法一：
# right = 'a1B2c3D4e5F6g7H8i9J10'
# letter = ''
# upper_letter_ASCII = ord('A')
# lower_letter_ASCII = ord('a')
# for i in range(1, 11):
#     if i % 2 == 1:
#         letter += chr(lower_letter_ASCII+i-1)
#         letter += str(i)
#     else:
#         letter += chr(upper_letter_ASCII+i-1)
#         letter += str(i)
# print(letter)
# if letter == right:
#     print('程序正确，棒棒的！！')
# else:
#     print('程序有误！！请修改！！')


# 方法二：
# right = 'a1B2c3D4e5F6g7H8i9J10'
# letter = ''
# lower_letter_ASCII = ord('a')
# for i in range(10):
#     if i % 2 == 0:
#         letter += chr(lower_letter_ASCII+i)
#         letter += str(i+1)
#     else:
#         letter += chr(lower_letter_ASCII+i).upper()
#         letter += str(i+1)
# print(letter)
# if letter == right:
#     print('程序正确，棒棒的！！')
# else:
#     print('程序有误！！请修改！！')

# 方法三：
# right = 'a1B2c3D4e5F6g7H8i9J10'
# letter_list = []
# lower_letter_ASCII = ord('a')
# upper_letter_ASCII = ord('A')
# difference = lower_letter_ASCII - upper_letter_ASCII
# for i in range(lower_letter_ASCII, lower_letter_ASCII+10):
#     if i % 2 ==1:
#         letter_list.append(chr(i))
#         letter_list.append(str(i-lower_letter_ASCII+1))
#     else:
#         letter_list.append((chr(i-difference)))
#         letter_list.append(str(i-lower_letter_ASCII+1))
# letter = ''.join(letter_list)
# print(letter)
# if letter == right:
#     print('程序正确，棒棒的！！')
# else:
#     print('程序有误！！请修改！！')

# 习题5：输出奇数字母和偶数字母到两个列表中：
"""
奇数字母列表:odd_letter_list
偶数字母列表:even_letter_list
range(ord('a'),ord('a')+26)
range(ord('A'),ord('a')+26)
循环判断奇偶数，分别放在响应的列表
"""
odd_letter_list = []
even_letter_list = []
for i in range(ord('A'), ord('A')+26):
    if i % 2 == 1:
        odd_letter_list.append(chr(i))
    else:
        even_letter_list.append(chr(i))

for i in range(ord('a'), ord('a')+26):
    if i % 2 == 1:
        odd_letter_list.append(chr(i))
    else:
        even_letter_list.append(chr(i))

print("""a 的ASCII码为：%s
A 的ASCII码为：%s""" % (ord('a'), ord('A')), end='')

print('''
奇数字母列表为：%s
偶数字母列表为：%s
''' % (odd_letter_list, even_letter_list), end='')





