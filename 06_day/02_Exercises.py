#tupla con los nombres de mis hermanas y hermano
hermanas = ('Isabel', 'Laura', 'Mariana')
hermano = ('Miguel',)
#Unir tuplas de hermano y hermanas y asignarlas a hermanos
hermanos = hermanas + hermano
#Modificar la tupla de hermanos y agrega el nombre de mi padre y madre y asígnarlo a family_members
padre = 'Miguel Angel'
madre = 'Maríana'
family_members = hermanos + (padre, madre)
print(family_members)
#Desempaquetar hermanos y padres de family_members
hermanos, padre, madre = family_members[:-2], family_members[-2], family_members[-1]
print(hermanos)  
print(padre)  
print(madre)  
#Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp
frutas = ('manzana', 'plátano', 'naranja')
verduras = ('zanahoria', 'espinaca', 'brócoli')
productos_animales = ('huevo', 'leche', 'queso')
food_stuff_tp = frutas + verduras + productos_animales
print(food_stuff_tp)
#Cambiar la tupla food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
#Extraer el elemento o los elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt
medio_tupla = food_stuff_tp[len(food_stuff_tp) // 2]
print(medio_tupla)  
medio_lista = food_stuff_lt[len(food_stuff_lt) // 2]
print(medio_lista)  
#Separar los primeros tres elementos y los últimos tres elementos de la lista food_stuff_lt
primeros_tres = food_stuff_lt[:3]
ultimos_tres = food_stuff_lt[-3:]
print(primeros_tres)  
print(ultimos_tres)  
#Eliminar la tupla food_stuff_tp por completo
del food_stuff_tp
#Comprobar si un elemento existe en una tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  
print('Iceland' in nordic_countries)  