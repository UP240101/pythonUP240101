#Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Longitud de la lista:", len(age))
print("Longitud del conjunto:", len(age_set))
"""
Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto
Una cadena ( str) es una secuencia inmutable de caracteres utilizada para representar texto y se define entre
combinaciones simples o dobles. Una lista ( list) es una colección ordenada y mutable de elementos, lo que 
significa que se pueden modificar, agregar o eliminar elementos después de su creación. En contraste, una tupla
( tuple) es similar a una lista, pero inmutable, lo que significa que sus elementos no pueden cambiar una vez definida. 
Por otro lado, un conjunto ( set) es una colección desordenada de elementos únicos, lo que implica que no permite
duplicados y no garantiza un orden.
"""
#I am a teacher and I love to inspire and teach people. ¿Cuántas palabras únicas se han utilizado en la oración?
oracion = "I am a teacher and I love to inspire and teach people."
palabras = oracion.lower().replace(".", "").split() 
palabras_unicas = set(palabras) 
print(len(palabras_unicas))
