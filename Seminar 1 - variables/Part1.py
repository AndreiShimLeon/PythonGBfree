# Функция type определяет тип данных
age = 30
person = None
period = 3.2
is_good = True
person_name = 'Max'
print(type(person))
print(type(is_good))
print(type(age))
print(type(period))
print(type(person_name))

#Перевести текст в число и наоборот:

birthday_year = '1988'
print (type(birthday_year))
period = 20
print(type(period))
age_int = int(birthday_year)+period
age_str = birthday_year + str(period)
print(age_int)
print(age_str)

#Ввод и вывод данных. Варианты: GUI, WEB, мобильное приложение, хранилище и консоль. На данном курсе рассматриваем только консоль.
# Функция Print: вывод одного слова, нескольких слов, вывод любого набора символов, вывод целых чисел, чисел с плавающей точкой, вывод истины/лжи,
# вывод объекта None:
print("hello")
print('Hello, world')
print('asdafasd & asdasfas sd')
print(100)
print(23.23)
print(True)
print(False)
print(None)
#Дополнительные функции print
# строка целиком
print("Hello, my name is Kesha, I am 2 years old")
# у нас есть  переменные
name = "Kesha"
age = 2
# как вывести строку вместе с переменными в терминал?
print(name, age)

# как сделать так, чтобы вывести эти две строки через другой символ?
print(name, age, sep='/') # вывод Kesha/2

#как сделать перенос строки?
print(name, end=';')
print(age, 'hello', end=';')
print('bye') # Получим результат в консоли - Kesha;2 hello;bye

# функция input() всегда будет STR
name = input('Введите свое имя: ')
print('Имя пользователя', name)

# результатом функции input() всегда будет STR
age = int(input('How old are you? '))
period = 20
age_period = age + period
print('Через ', period, 'вам будет ', age_period)