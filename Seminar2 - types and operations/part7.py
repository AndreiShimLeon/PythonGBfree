# программа Winners, интерактивное награждение победителей соревнований по Python
# Пользователь вводит количество участников и их места в зависимости
# от количества
# 1. Вывод имен участников по алфавиту
# 2. Получить 3-х победителей и поздравить их
# 3. Победители: ... Поздравляем!

print('Соревнования по Python')
count = int(input('Введите количество участников: '))
i = count
members = []
while i>0:
    name = input('Кто занял {} место? '.format(i))
    members.append(name)
    i-=1

# кто участвовал в соревновании (по алфавиту)

print('В соревнованиях участвовали: ', members)

# мы записали людей с конца
members.reverse() # переворачиваем список

# берем первые три места
result = members[:3]
result = 'Победители: {}. Поздравляем!'.format(result)

print(result)