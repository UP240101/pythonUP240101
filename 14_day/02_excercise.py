countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1
countries_upper = list(map(lambda country: country.upper(), countries))
print(countries_upper)
#2
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
#3
names_upper = list(map(lambda name: name.upper(), names))
print(names_upper)
#4
countries_land = list(filter(lambda country: "land" in country.lower(), countries))
print(countries_land)
#5
countries_six = list(filter(lambda country: len(country) == 6, countries))
print(countries_six)
#6
countries_six_or_more = list(filter(lambda country: len(country) >= 6, countries))
print(countries_six_or_more)
#7
countries_E = list(filter(lambda country: country.startswith('E'), countries))
print(countries_E)
#8
result = list(map(lambda x: x ** 2, numbers))
result = list(filter(lambda x: x % 2 == 0, result))
print(result)
#9
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))
mixed_list = [1, 'Estonia', 3, 'Finland', 'Sweden']
print(get_string_lists(mixed_list))
#10
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
#11
countries_sentence = reduce(lambda x, y: x + ", " + y, countries)
print(countries_sentence + " son países del norte de Europa.")
#12
def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country.lower(), countries))
print(categorize_countries('land'))
#13
def country_initials(countries):
    result = {}
    for country in countries:
        initial = country[0].upper()
        if initial in result:
            result[initial] += 1
        else:
            result[initial] = 1
    return result
print(country_initials(countries))
#14
def get_first_ten_countries(countries):
    return countries[:10]
#15
def get_last_ten_countries(countries):
    return countries[-10:]