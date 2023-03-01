print('Список друзей')
friends = ['Max', 'Leo', 'Kate']
print(friends)

# длина списка через функцию len
print('длина списка')
print(len(friends))

# добавление нового элемента через функцию append
print('Добавляем Рона в друзья')
friends.append('Ron')
print(friends)

# удаление последнего элемента через функцию pop
print('Удаляем последнего друга (Рона) из друзей')
friends.pop()
print(friends)

# очищение всего списка через функцию clear
print('Удаляем всех друзей')
friends.clear()
print(friends)
# удаление элемента списка через функцию remove
print('Возвращаем всех друзей')
friends = ['Max', 'Leo', 'Kate']
print(friends)

print('Удаляем друга по имени Лео')
friends.remove('Leo')
print(friends)
# удаление элемента по индексу через del

print('Удаляем первого друга')
del friends[0]
print(friends)