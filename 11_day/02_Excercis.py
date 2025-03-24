#1
def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = sum(1 for i in range(n+1) if i % 2 != 0)
    return f"The number of evens are {evens}.\nThe number of odds are {odds}."
#2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
#3
def is_empty(value):
    return not bool(value)
#4
import statistics
def calcular_media(lista):
    return statistics.mean(lista)
def calcular_mediana(lista):
    return statistics.median(lista)
def calcular_moda(lista):
    return statistics.mode(lista)
def calcular_rango(lista):
    return max(lista) - min(lista)
def calcular_varianza(lista):
    return statistics.variance(lista)
def calcular_desviacion_estandar(lista):
    return statistics.stdev(lista)