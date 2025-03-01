#variables individuales
nombre = "sergio"
apellido = "martinez"
nombre_completo = nombre + apellido + "castillo"
país = "mexico"
ciudad = "aguascalientes"
edad = 18
año = 2025
is_married = False
is_true = False
#variables en una sola linea
altura, peso, color_favorito = 180, 105, "morado"
#imprimir variables para verificar
print(nombre, apellido, nombre_completo, país, ciudad, edad, año, is_married, is_true)
print(altura, peso, color_favorito)
#comprobar el tipo de variables variables
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(país))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(altura))
print(type(peso))
print(type(color_favorito))
#Utiliza la función len() para averiguar la longitud
print(len(nombre))
print(len(apellido))
print(len(apellido)==(len(nombre)))
#declarar variables numericas
num_uno = 5
num_dos = 4
#operaciones con variables numericas
total = print(num_uno + num_dos )
diff = print(num_dos - num_uno)
producto = print(num_dos * num_uno)
division = print(num_uno / num_dos)
remainder = print(num_uno % num_dos)
exp = print(num_uno ** num_dos)
floor_division = print(num_uno // num_dos)
#radio de un circulo de 30 metros
radio = 30
pi = 3.1416
area_del_circulo = pi * (radio ** 2)
circunferencia_del_circulo = 2 * pi * radio
print("Área del círculo:", area_del_circulo)
print("Circunferencia del círculo:", circunferencia_del_circulo)
# Obtener datos de un usuario
nombre_usuario = input("Introduce tu nombre: ")
apellido_usuario = input("Introduce tu apellido: ")
país_usuario = input("Introduce tu país: ")
edad_usuario = int(input("Introduce tu edad: "))  # Convertimos la edad a entero
print("Nombre:", nombre_usuario)
print("Apellido:", apellido_usuario)
print("País:", país_usuario)
print("Edad:", edad_usuario)
# Ejecutar help('keywords') en la terminal de Python
help('keywords')