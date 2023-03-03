friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# перебор словаря по ключам
for key in friend.keys():
    print(key)
    print(friend[key])

# for key in friend:
#     print(key)
#     print(friend[key])

# перебор словаря по значениям
for val in friend.values():
    print(val)

# перебор словаря по парам ключ-значение

for item in friend.items():
    print(item) # получаем на печати кортежи

for key, val in friend.items():
    print(key)
    print(val)