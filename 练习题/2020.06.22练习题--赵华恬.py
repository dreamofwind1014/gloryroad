# 练习191：单词顺序翻转且单词本身翻转

s = "i am a boy"

print(" ".join([word[::-1] for word in s.split()[::-1]]))

# 方式2：
print(s[::-1])


# 练习192:判断一下这句话，有几个数字和几个空白，和几个字母其他字符有几个
"I am a 12 years old boy! hi,me!"

s = "I am a 12 years old boy! hi,me"

d_num =0
letter_num = 0
space_num = 0
other_num = 0

for v in s:
    if v.isalpha():
        letter_num += 1
    elif v.isdigit():
        d_num += 1
    elif v.isspace():
        space_num += 1
    else:
        other_num += 1

print(d_num)
print(letter_num)
print(space_num)
print(other_num)


# 练习193：将一个正整数分解质因数
# 算法：
# n从2开始除，如果能被2整除，继续从2开始除，如果不能被2整除，除数依次加1，继续判断能否整除，如果能整除再从2开始除
# 能整除就加入结果列表，更新n的值，且重置除数为2
def prime_num(n):
    result = []
    divisor = 2
    while n != 1:
        if n%divisor == 0:
            result.append(divisor)
            n = n//divisor
            divisor = 2
        else:
            divisor += 1
    return result
print(prime_num(24))
print(prime_num(30))
print(prime_num(100))


# 练习194：一个字符串中，分别输出奇数坐标字符或偶数坐标字符，奇数坐标的一行，偶数坐标的一行
odd_list = []
even_list = []
s = "alkjjjsdfs"
for i in range(len(s)):
    if i%2 == 0:
        even_list.append(s[i])
    else:
        odd_list.append(s[i])
print("奇数:"," ".join(odd_list))
print("偶数:"," ".join(even_list))


# 练习195：统计字符串中的字母、数字、其他字符个数
s = "alkjjjsdfs111! @#A"
letter_num =0
digit_num = 0
other_num = 0
for v in s:
    if v.isalpha():
        letter_num += 1
    elif v.isdigit():
        digit_num += 1
    else:
        other_num += 1
print("字母:",letter_num)
print("数字:",digit_num)
print("其他:",other_num)



