# 2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

number = 0
while number > 9 or number < 1:
    number = int(input('Введите число от 1 до 9 '))
    if number > 9 or number < 1:
        print('Неверное число, повторите ввод.')
else:
    number = number**2
    print('квадрат вашего числа ', number)


