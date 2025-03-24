#Iterar de 0 a 10 usando for loop
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for number in numeros:
    print(number)
#El mismo usando while loop
conteo = 0
while conteo < 11:
    print(conteo)
    conteo = conteo + 1
#Iterar de 10 a 0 usando for loop
numeros = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
for number in numeros:
    print(number)
#El mismo usando while loop
count = 9
while count > -1:
    print(count)
    count = count + 1
    if count == 10:
        break
