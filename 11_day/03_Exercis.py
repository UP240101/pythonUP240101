#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#2
def all_unique(lista):
    return len(lista) == len(set(lista))
#3
def all_same_type(lista):
    return all(isinstance(i, type(lista[0])) for i in lista)
#4
import keyword
import string

def is_valid_variable(var):
    if not var or var[0] not in string.ascii_letters + "_":
        return False
    if keyword.iskeyword(var):
        return False
    return all(c in string.ascii_letters + string.digits + "_" for c in var)
#5
def most_spoken_languages(countries_data, top_n=10):
    language_counts = {}
    for country in countries_data:
        for language in country["languages"]:
            language_counts[language] = language_counts.get(language, 0) + 1

    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]
#6
def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:top_n]
