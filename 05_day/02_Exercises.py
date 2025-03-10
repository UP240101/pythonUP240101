#Ordenar ages y encontrar edad mínima y máxima
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
edad_minima = edades[0]
edad_maxima = edades[-1]
print(edad_minima, edad_maxima)
#Agregar la edad mínima y máxima nuevamente
edades.append(edad_minima)
edades.append(edad_maxima)
print(edades)
#Encontrar la edad media
media = len(edades) // 2
edad_media = (edades[media] + edades[media - 1]) / 2 if len(edades) % 2 == 0 else edades[media]
print(edad_media)
#Encontrar la edad promedio
edad_promedio = sum(edades) / len(edades)
print(edad_promedio)
#Encontrar el rango de edades
edad_rango = edad_maxima - edad_minima
print(edad_rango)
#Comparar min - promedio y máx - promedio con abs()
print(abs(edad_minima - edad_promedio), abs(edad_maxima - edad_promedio))
#Encontrar el país o países intermedios
paises = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
intermedio = len(paises) // 2
print(paises[intermedio] if len(paises) % 2 != 0 else paises[intermedio - 1: intermedio + 1])
#Dividir la lista de países en dos partes iguales
primer_mitad = paises[:len(paises) // 2 + len(paises) % 2]
segunda_mitad = paises[len(paises) // 2 + len(paises) % 2:]
print(primer_mitad, segunda_mitad)
#Separar los primeros tres países y los escandinavos
primeros_tres = paises[:3]
escandinavos = paises[3:]
print(primeros_tres, escandinavos)
