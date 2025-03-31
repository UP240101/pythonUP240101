#1
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
numeros_filtrados = [i for i in numeros if i < 0 or i == 0]
print(numeros_filtrados)
#2
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_lista = [ number for row in lista_de_listas for number in row]
print(flattened_lista)    
#3
tuplas = [(i, *[i**j for j in range(7)]) for i in range(11)]
print(tuplas)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
aplanada = [[pais.upper(), pais[:3].upper(), capital.upper()] for sublista in countries for pais, capital in sublista]
print(aplanada)
#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': pais.upper(), 'city': capital.upper()} for sublista in countries for pais, capital in sublista]
print(dict_list)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_list = [' '.join(nombre) for sublista in names for nombre in sublista]
print(names_list)
#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else None
y_intercept = lambda x, y, m: y - m * x if m is not None else None
# Ejemplo de uso
m = slope(1, 2, 3, 6)
b = y_intercept(1, 2, m)
print(f"Pendiente: {m}, Intersección con el eje y: {b}")