# Списки
empty_list = []

# можно объявить список и сразу заполнить его элементами
friends = ['Max', 'Leo', 'Kate']

# тип списка - дшые
print(type(friends))

# Как и в строке для списка доступны индексы (начинаются с 0)

print('Второй друг: ', friends[1])
print('Первый друг с конца', friends[-1])

# Также можно применить срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])