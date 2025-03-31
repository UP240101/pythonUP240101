import countries_data
from countries_data import countries_data
#1
countries_sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
for country in countries_sorted_by_name:
    print(country['name'])
#2
countries_sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
for country in countries_sorted_by_capital:
    print(country['capital'])
#3
countries_sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
for country in countries_sorted_by_population:
    print(country['name'], country['population'])