# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка
# # дробным числом
s = input('Введите строку ')

try:
    float(s)
    if '.' in s:
        print('Дробное число')
except ValueError:
    print('Не дробное число')
