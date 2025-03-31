#1
"""
Diferencia entre map, filter y reduce: map aplica una función a cada elemento de un iterable y devuelve los resultados, 
filter filtra los elementos según una condición (devuelve solo los que cumplen la condición), y reduceacumula los elementos 
de un iterable en un solo valor usando una función de dos argumentos.
"""
#2
"""
Diferencia entre función de orden superior, cierre y decorador: Una función de orden superior toma funciones como argumentos
 o devuelve funciones. Un cierre es una función que recuerda el contexto donde fue creado, accediendo a variables externas. 
 Un decorador es una función de orden superior que extiende el comportamiento de otra función sin modificar su código.
"""
#3
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
#4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)
#5
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)
#6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)