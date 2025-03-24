#1
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())  
#2
def user_id_gen_by_user():
    num_chars = int(input("Ingrese el número de caracteres por ID: "))
    num_ids = int(input("Ingrese la cantidad de IDs a generar: "))
    
    ids = [''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)) for _ in range(num_ids)]
    
    return '\n'.join(ids)

print(user_id_gen_by_user())
#3
def rgb_color_gen():
    return f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"

print(rgb_color_gen())  