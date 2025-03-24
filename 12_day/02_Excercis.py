#1
def list_of_hexa_colors(n):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]

print(list_of_hexa_colors(3))  
#2
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print(list_of_rgb_colors(3))  
#3
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Tipo de color no válido"

print(generate_colors('hexa', 3))  
print(generate_colors('rgb', 3))   