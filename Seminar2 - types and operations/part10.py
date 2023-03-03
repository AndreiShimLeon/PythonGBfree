# как добавить возраст другу?
friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))

print(friend['age']) # по ключу получаем значение

friend['has_car'] = True # добавляем пару ключ-значение в словарь
print(friend)

friend['has_car'] = False
print(friend)

del(friend['age'])
print(friend)

if 'age' in friend:
    print('Age exists')
else:
    print('Age does not exist')

if 'has_car' in friend:
    print('car exists')
else:
    print('car does not exist')