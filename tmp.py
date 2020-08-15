# my_dict = {"ccc":24, 'c':24,'lilee':25, 'age':24, 'phone':12,"xzxx":25,"ccc":24}
# t = sorted(my_dict.items(),key=lambda item:item[1],reverse=True)
# print(t)
# tk = None
# tmp = None
# tmpList = []
# for i,j in t:
#     if not tmp or tmp < j:
#         tmp = j
#         tk = i
#     elif tmp > j:
#         continue
#     else:
#         tmpList.append(i)
# tmpList.append(tk)
# print(tmpList)

# 题目1：读入一个字符串，如果数字的个数>2 且字母个数大于3，打印条件成立，否则打印不成立
# msg = input('请输入字符串>>')
# int_num = 0
# letter_num = 0
# for i in msg:
#     if i.isdigit():
#         int_num += 1
#     elif i.isalpha():
#         letter_num += 1
# if int_num > 2 and letter_num > 3:
#     print('条件成立')
# else:
#     print('条件不成立')
"""
算法：

"""
# while True:
#     msg = input('请输入字符串>>')
#     int_num = 0
#     letter_num = 0
#     for i in msg:
#         if not(int_num > 2 and letter_num > 3):
#             if i.isdigit():
#                 int_num += 1
#             elif i.isalpha():
#                 letter_num += 1
#         else:
#             print('条件成立')
#             break
#     else:
#         print('条件不成立')


# n = [1, 2, [3, 4, 5, [6, 7, 8], [9, 10, 11], [12, 13, 14]], [15, 16, 17, 18]]
# for i in range(len(n)):
#     print(n[i])
#     if isinstance(n[i], list):
#         print("*88888888")
#
continue_or_not = 'yes'
while continue_or_not == 'yes':
    # msg =
    msg = """
| -7772652821245681003 | 1594307400000 | 1                |
| 1484671144734857896  | 1594307400000 | 1                |
| -6078572490661060213 | 1594307400000 | 1                |
| -4419104754376872558 | 1594307400000 | 1                |
| -6027672056142663413 | 1594307400000 | 1                |
    """
    # msg_standard = input("标准文案>>>")
    msg_standard = """
| -4419104754376872558 | 1594307400000 | 1                |
| -7772652821245681003 | 1594307400000 | 1                |
| 1484671144734857896  | 1594307400000 | 1                |
| -6078572490661060213 | 1594307400000 | 1                |
| -6027672056142663413 | 1594307400000 | 1                |
    """

    if msg == msg_standard:
        print('ok哇，木问题')
    else:
        for i in range(len(msg)):
            if msg[i] != msg_standard[i]:
                if msg[i] in (',', '，', '.', '。', ':', '：'):
                    continue
                else:
                    print("msg:", msg[i:])
                    print("msg_standard:", msg_standard[i:])
                    break
        else:
            print("一样了")
    continue_or_not = input('>>yes?or no?')




