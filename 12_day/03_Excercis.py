import random
#1
def shuffle_list(lista):
    random.shuffle(lista)
    return lista

print(shuffle_list([1, 2, 3, 4, 5]))  # Ejemplo de salida: [3, 1, 5, 4, 2]
#2
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())  
