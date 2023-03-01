friend = 'Максим'
# при использовании двойных кавычек поведение не изменится

print(friend)
# тип данных str
print(type(friend))

say = 'say "Hello"'
print(say)
say = "say 'Hello'"
print(say)

# Можем получать символы по индексу
friend = 'Максим'
first_letter = friend[0]
print('Первая буква имени друга', first_letter)
print('Тип 1-го символа тоже строка: ', type(first_letter))
print('Последняя буква имени друга', friend[-1])

# Срезы
friend = 'Максим'
first_three_letter = friend[0:3]
first_three_letter_2 = friend[:3]
last_three_letter = friend[-3:]
last_three_letter_2 = friend[3:6]
print(first_three_letter)
print(first_three_letter_2)
print(last_three_letter)
print(last_three_letter_2)

# Len функция
friends = 'Максим Леонид'
print(friends)
print(len(friends)) #13 символов

print(friends.find('Лео'))  # результат "7", это индекс,
                            # на котором метод .find
                            # нашел подстроку "Лео"
print(friends.find('123Лео'))   # Результат "-1" - искомой подстроки
                                #нет в строке friends
print(friends.split()) # В результате получим список ['Максим', 'Леонид']
print(friends.isdigit()) # Вернет False - str не состоит из цифр
numbers = '12345'
print(numbers.isdigit()) # Вернет True - str состоит только из цифр
print(friends.upper()) # Вернет МАКСИМ ЛЕОНИД из Максим Леонид
print(friends.lower()) # Вернет максим леонид из Максим Леонид
