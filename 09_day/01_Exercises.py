"""
Obtener la información del usuario mediante input(“Ingrese su edad:”). Si el usuario tiene 18 años o más,
indique: Tiene edad suficiente para conducir. Si es menor de 18 años, indique que espere los años que faltan"
"""
edad = int(input("Ingrese su edad: "))
# Verificar si tiene edad suficiente para conducir
if edad >= 18:
    print("tu puedes aprender a manejar.")
else:
    print(f"tu necesitas {18 - edad} años mas para aprender a manejar.")
"""
Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad:”)
para obtener la edad como entrada. Puedes usar una condición anidada para imprimir "año" 
si hay una diferencia de edad de 1 año, "años" si la diferencia es mayor y un texto personalizado si my_age = your_age. 
"""
mi_edad = 18  
tu_edad = int(input("Ingresa tu edad: "))

if mi_edad > tu_edad :
    diferencia = mi_edad - tu_edad
    print(f"yo soy {diferencia} {'año' if diferencia == 1 else 'años'} mas viejo que tu")
elif mi_edad < tu_edad :
    diferencia = tu_edad - mi_edad
    print(f"tu eres {diferencia} {'año' if diferencia == 1 else 'años'} mas viejo que yo.")
else:
    print("tenemos la misma edad")
"""
Obtener dos números del usuario mediante la solicitud de entrada. Si a es mayor que b, devuelve a mayor que b; si a es 
menor que b, devuelve a menor que b; de lo contrario, a es igual a b.
"""
a = int(input("ingresar numero uno: "))
b = int(input("ingresar numero dos: "))

if a > b:
    print(f"{a} es mayor que {b}.")
elif a < b:
    print(f"{a} es menor que {b}.")
else:
    print(f"{a} es igual a {b}.")