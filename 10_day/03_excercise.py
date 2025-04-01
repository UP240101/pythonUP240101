from countries import countries
from countries_data import countries_data
# 1
land_countries = [country for country in countries if "land" in country.lower()]
print(land_countries)
# 2
fruity_list = ['banana', 'orange', 'mango', 'lemon']
rev = []
for i in range(3, -1, -1):
    rev.append(fruity_list[i])
print(rev)
# 3
languages = set()
for country in countries_data:
    languages.update(country["languages"])  
total_languages = len(languages)
print(total_languages)
# Contar la frecuencia de cada idioma
language_counts = {}
for country in countries_data:
    for language in country["languages"]:
        language_counts[language] = language_counts.get(language, 0) + country["population"]
print(language_counts)
# Ordenar los idiomas por número de hablantes y obtener los 10 más hablados
most_spoken_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print(most_spoken_languages)
# Ordenar los países por población y obtener los 10 más poblados
most_populated_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)[:10]
print(most_populated_countries)