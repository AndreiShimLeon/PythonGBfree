# дополнительные математические операции
a = 5//2 #целая часть от деления
print(a)

b = 5%2 # остаток от деления
print(b)

c = 2**3 # возведение в степень
print(c)

# Условный оператор if

age = int(input('How old are you? '))
if age < 18:
    print('Доступ разрешен')
elif age == 18:
    print('Вам ровно 18 лет, поздравляем с совершеннолетием!')
elif age > 18 and age < 25:
    print('Вы в другой категории пользователей')
else:
    print('Долступ разрешен')
        if age % 5 == 0:
            print('У вас юбилей')
print('Какие-то действия')
print('end')