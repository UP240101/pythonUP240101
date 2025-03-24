#1
def add_two_numbers(a, b):
    return a + b
#2  
import math
def area_del_circulo(r):
    return math.pi * r * r
#3
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los elementos deben ser numéricos"
#4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#5
def check_season(mes):
    estaciones = {
        "invierno": ["diciembre", "enero", "febrero"],
        "primavera": ["marzo", "abril", "mayo"],
        "verano": ["junio", "julio", "agosto"],
        "otoño": ["septiembre", "octubre", "noviembre"]
    }
    
    for estacion, meses in estaciones.items():
        if mes.lower() in meses:
            return estacion.capitalize()
    return "Mes inválido"
#6
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1) if x1 != x2 else "Pendiente indefinida"
#7
import math

def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        return -b / (2*a)
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
#8
def print_list(lista):
    for elemento in lista:
        print(elemento)
#9
def reverse_list(lista):
    return lista[::-1]
#10
def capitalize_list_items(lista):
    return [item.capitalize() for item in lista]
#11
def add_item(lista, item):
    lista.append(item)
    return lista
#12
def remove_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista
#13
def sum_of_numbers(n):
    return sum(range(n+1))
#14
def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)
#15
def sum_of_even_numbers(n):
    return sum(i for i in range(n+1) if i % 2 == 0)