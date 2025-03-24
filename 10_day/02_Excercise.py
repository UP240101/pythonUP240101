#Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números
sum_nums = 0
for i in range(0, 101):
    sum_nums += i
print("la suma de todos los numeros es", sum_nums)
#Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todos los impares
even_sum = 0
odd_sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("la suma de todos los pares es", even_sum)
print("la suma de tos los impares es", odd_sum)
