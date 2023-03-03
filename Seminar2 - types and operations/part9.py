# Когда нам может помочь range

winners = ['Max', 'Leo', 'Kate']
# Простой перебор
for winner in winners:
    print(winner)

# что делать, если нам нужно вывести место победителя?
# использовать while?
# или есть способ лучше?

# вывести нечетные цифры от 1 до 5
numbers = [1, 3, 5]
for number in numbers:
    print(number)

# как это сделать, если цифр будет 100 и больше?
numbers = range(10)
print(numbers) # печатаем наш range
print(type(numbers)) # печатаем тип, и видим class 'range'
print(list(numbers)) # превращаем range в list и получаем список от 0 до 9

for i in range(len(winners)):
    print(i+1, ')', winners[i])

print(list(range(1,1000,2))) # печатаем нечетные числа от 1 до 1000

for number in range(1,12,2):
    print(number)
