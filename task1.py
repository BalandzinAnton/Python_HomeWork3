# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в
# шестнадцатиричную систему счисления.
number = int(input())

n = ''
s = '0123456789ABCDEF'
while number > 0:
    n = s[number % 16] + n
    number = number // 16
print(n)