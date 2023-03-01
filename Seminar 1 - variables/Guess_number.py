number = 43
value = int(input('Угадайте число от 1 до 100 '))

if value == number:
    print('Вы угадали')
elif value > number:
    print('Неверно, ваше число больше загаданного')
else:
    print('Неверно, ваше число меньше загаданного')