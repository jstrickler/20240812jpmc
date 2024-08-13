cities = ['Portland', 'Pittsburg', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # for city in more cities: cities.append(city)
print(f"cities: {cities}\n")

#  LIST.append(obj)  LIST.insert(index, obj)  LIST.extend(iterable)

del cities[3]
print(f"cities: {cities}\n")

print("Buffalo" in cities)
print('Buffalo' in cities)

cities.remove('Buffalo')
print(f"cities: {cities}\n")
# this will not work now: cities.remove('Buffalo')

city = cities.pop()  # remove last item
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

#  del LIST[index]   LIST.remove(value)   LIST.pop()   LIST.pop(index)