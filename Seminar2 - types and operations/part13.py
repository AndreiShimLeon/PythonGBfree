cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)

cities.add('Burma')
print(cities)
cities.add('Moscow') # дубль не добавляется
print(cities)
cities.remove('Moscow') # удалили Москву
print(cities)
print(len(cities)) # 3
print('Paris' in cities) # True

for city in cities:
    print(city)