# Как сделать c циклом while
name = None

while name != 'Гвидо':
    name = input('Кто создатель Python?')
    if name == 'Гвидо':
        break
    print('Неверно')
print('Верно!')

# Использование Continue - переход на следующую итерацию цикла без выполнения
# оставшихся команд текущаего цикла.
# Вывод четных чисел от 0 до n, n вводит пользователь.

n = int(input('Программа выводит четные числа от 0 до n, введите n: '))
i = 0
while i <= n:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i+=1
# добавил блок else после while
else: #если мы выйдем из цикла с помощью break, то блок else выполняться не будет
    print('end')