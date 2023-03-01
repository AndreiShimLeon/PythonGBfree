friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

# Типы данных
print(type(friend_name)) # <class 'str'>
print(type(friends)) # <class 'list'>
print(type(roles))# <class 'tuple'>

# Индексация
print(friend_name[1]) # a - второй символ в строке Max
print(friends[1]) # Leo - второй элемент в списке friends
print(roles[1])# guest - второй элемент в кортеже roles

# Срезы
print(friend_name[1:]) # ax - срез, начиная со 2-го символа в строке Max
print(friends[1:]) # ['Leo', 'Kate'] - срез, начиная со 2-го элемента в списке friends
print(roles[1:]) # ('guest', 'user') срез, начиная со 2-го элемента в кортеже roles

# Длина
print(len(friend_name)) # 3 - длина строки Max
print(len(friends)) # 3 - длина списка friends
print(len(roles)) # 3 - длина кортежа roles

if 'Max' in friends:
    print('У меня есть этот друг')

if 'M' in friend_name:
    print('Буква М есть в имени друга')

# while
print('цикл while')
i = 0
while i < len(friends):
    print(friends[i])
    i += 1

# цикл for в списке, строке и кортеже
print('цикл for в списке')
for friend in friends: # здесь friend - переменная цикла
    print(friend)

print('цикл for в строке')
for symbol in friend_name: # здесь symbol - переменная цикла
    print(symbol)

print('цикл for в кортеже')
for element in roles: # здесь element - переменная цикла
    print(element)