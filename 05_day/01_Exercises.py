#Declarar una lista vacía
lista_vacia = []
#Declarar una lista con más de 5 elementos
mi_lista = [1, 2, 3, 4, 5, 6]
#Encontrar la longitud de la lista
print(len(mi_lista))
#Obtener el primer, medio y último elemento
primero = mi_lista[0]
medio = mi_lista[len(mi_lista) // 2]
ultimo = mi_lista[-1]
print(primero, medio, ultimo)
#Lista mixed_data_types con nombre, edad, altura, estado civil, dirección
mixed_data_types = ["sergio", 18, 1.80, "Soltero", "aguascalientes"]
#Lista it_companies con empresas de tecnología
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
#Número de empresas en la lista
print(len(it_companies))
#Primera, segunda y última empresa
print(it_companies[0], it_companies[1], it_companies[-1])
#Modificar una empresa y mostrar el listado
it_companies[2] = "Tesla"
print(it_companies)
#Añadir una empresa de TI a la lista
it_companies.append("Intel")
print(it_companies)
#Insertar una empresa en el medio de la lista
it_companies.insert(len(it_companies) // 2, "Spotify")
print(it_companies)
#Cambiar uno de los nombres a mayúsculas (excepto IBM)
it_companies[1] = it_companies[1].upper()
print(it_companies)
#Unir it_companies con "#; "
print("#; ".join(it_companies))
#Comprobar si una empresa existe en la lista
print("Google" in it_companies)
#Ordenar la lista
it_companies.sort()
print(it_companies)
#Invertir la lista en orden descendente
it_companies.reverse()
print(it_companies)
#Separar las primeras 3 empresas
print(it_companies[:3])
#Eliminar las últimas 3 empresas
print(it_companies[:-3])
#Eliminar las empresas intermedias
del it_companies[len(it_companies) // 2]
print(it_companies)
#Eliminar la primera empresa
del it_companies[0]
print(it_companies)
#Eliminar la última empresa
del it_companies[-1]
print(it_companies)
#Eliminar todas las empresas
it_companies.clear()
print(it_companies)
#Destruir la lista de empresas
del it_companies
#Unir front_end y back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#Copiar full_stack e insertar Python y SQL después de Redux
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Redux") + 2, "SQL")
print(full_stack)