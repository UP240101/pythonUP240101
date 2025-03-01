import math
#Declarar variables
edad = 18  
altura = 1.79 
numero_complejo = 3 + 4j  
# 2. Calcular el área de un triángulo
base = float(input("ingresar base: "))
altura_tri = float(input("ingresar altura: "))
area = 0.5 * base * altura_tri
print(f"El area del triangulo es {area}")
#Calcular el perímetro de un triángulo
a = float(input("ingresar lado a: "))
b = float(input("ingresar lado b: "))
c = float(input("ingresar lado c: "))
perimetro = a + b + c
print(f"el perimetro del triangulo es {perimetro}")
#Calcular área y perímetro de un rectángulo
longitud = float(input("Introduzca la longitud: "))
ancho = float(input("Introduzca el ancho: "))
area_rect = longitud * ancho
perimetro_rect = 2 * (longitud + ancho)
print(f"area del rectangulo: {area_rect}, Perimetro: {perimetro_rect}")
#Calcular área y circunferencia de un círculo
radio = float(input("Introduzca el radio: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print(f"area del circulo: {area_circulo}, Circunferencia: {circunferencia}")
#Cálculo de pendiente e intersecciones de y = 2x - 2
m = 2
interseccion_y = -2
interseccion_x = 2 / 2  
print(f"pendiente: {m}, x-interseccion: {interseccion_x}, y-interseccion: {interseccion_y}")
#Pendiente y distancia euclidiana entre (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"pendiente: {pendiente}, distancia eucladeania: {distancia}")
#Comparar pendientes
print(f"Comparar pendientes: {m == pendiente}")
#Resolver y = x^2 + 6x + 9 para x donde y = 0
for x in range(-10, 10):
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y es 0 cuando x = {x}")
#Comparar longitudes de 'python' y 'dragon'
print(len("python") != len("dragon"))
#Verificar si 'on' está en 'python' y 'dragon'
print("on" in "python" and "on" in "dragon")
#Verificar si 'jargon' está en la oración
sentence = "Espero que este curso no esté lleno de jerga"
print("jargon" in sentence)
#Verificar si 'on' no está en 'dragon' y 'python'
print("on" not in "dragon" and "on" not in "python")
#Longitud de 'Python', convertir a flotante y luego a cadena
length_python = len("Python")
float_length = float(length_python)
string_length = str(float_length)
print(string_length)
#Verificar si un número es par
num = int(input("ingresa un numero: "))
print(f"{num} es par: {num % 2 == 0}")
#Verificar si la división entera de 7/3 es igual a int(2.7)
print(7 // 3 == int(2.7))
#Verificar si '10' es del mismo tipo que 10
print(type("10") == type(10))
#Verificar si int('9.8') es igual a 10
print(int(float("9.8")) == 10)
#Calcular salario semanal
horas = float(input("ingresar horas : "))
tarifa = float(input("Introduzca la tarifa por hora: "))
salario = horas * tarifa
print(f"tu salario semanal es {salario}")
#Calcular segundos vividos en n años
años = int(input("ingresar los años que has vivido: "))
segundos_vividos = años * 365 * 24 * 60 * 60
print(f"tu has vivido por {segundos_vividos} segundos.")
#Mostrar tabla
for i in range(1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")