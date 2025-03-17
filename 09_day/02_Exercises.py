# Clasificación de estudiantes según su puntuación
puntuacion = int(input("Ingrese la puntuación del estudiante: "))
if 80 <= puntuacion <= 100:
    print("calificacion: A")
elif 70 <= puntuacion <= 79:
    print("calificacion: B")
elif 60 <= puntuacion <= 69:
    print("calificacion: C")
elif 50 <= puntuacion <= 59:
    print("calificacion: D")
elif 0 <= puntuacion <= 49:
    print("calificacion: F")
else:
    print("Puntuación no válida. Debe estar entre 0 y 100.")
# Verificar la temporada según el mes ingresado
month = input("Ingrese un mes: ").lower()

if month in ["septiembre", "octubre", "noviembre"]:
    print("La temporada es otoño.")
elif month in ["diciembre", "enero", "febrero"]:
    print("La temporada es invierno.")
elif month in ["marzo", "abril", "mayo"]:
    print("La temporada es primavera.")
elif month in ["junio", "julio", "agosto"]:
    print("La temporada es verano.")
else:
    print("Mes no válido.")
# Lista de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
# Solicitar una fruta al usuario
new_fruit = input("Ingrese el nombre de una fruta: ").lower()

if new_fruit in fruits:
    print("esa fruta ya existe en la lista")
else:
    fruits.append(new_fruit)
    print("Fruta añadida. Lista actualizada:", fruits)
