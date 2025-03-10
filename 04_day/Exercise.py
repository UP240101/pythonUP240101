#concatena la cadena 30 dias de python
thirty = "treinta "
days = "dias "
of = "de "
python = "Python"
cadena = thirty + days + of + python
print(cadena)
#concatena la cadrna codificacion para todos
coding = "codificacion " 
FOR = "para "
ALL = "todos "
cadena_1 = coding + FOR + ALL
#Declare una variable llamada empresa y asígnele un valor inicial
empresa = cadena_1
#Imprima la variable empresa 
print(cadena_1)
#Imprimir la longitud de la cadena de la empresa
print(len(empresa))
#Cambiar todos los caracteres a letras mayúsculas
print(str.upper(empresa))
#Cambiar todos los caracteres a letras minúsculas
print(str.lower(empresa))
#formatear el valor de la cadena codificacion para todos
str.capitalize(empresa)
str.title(empresa)
str.swapcase(empresa)
#Recortar la primera palabra de la cadena Codificación para todos
empresa = " ".join(empresa.split()[1:])
print(empresa)
#Compruebe si la cadena Codificación Para Todos contiene una palabra Codificación 
empresa
palabra = "codificacion"
if palabra in cadena:
    print("Sí, la palabra está en la cadena.")
else:
    print("No, la palabra no está en la cadena.")
#Reemplace la palabra codificación por python
empresa = cadena_1.replace("codificacion", "python")
print(empresa)
#Cambiar Python para todos por Python for All
challenge = 'python para todos'
challenge = challenge.replace('para', 'for').replace('todos', 'all')
print(challenge)  
#Divida la cadena codigo para todos
(str.split(empresa))
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" dividir la cadena en la coma
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(", "))
#preguntas
cadena_pregunta = "Codificación para todos"
# ¿Cuál es el carácter en el índice 0 en la cadena "Codificación para todos"?
print(cadena_pregunta[0])  # Salida: C
# ¿Cuál es el último índice de la cadena "Codificación para todos"?
print(cadena_pregunta[-1])  # Salida: s
# ¿Qué carácter está en el índice 10 en la cadena "Codificación para todos"?
print(cadena_pregunta[10])  # Salida: i
def crear_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join(palabra[0].upper() for palabra in palabras)
    return acronimo
frase = "python para todos"
acronimo = crear_acronimo(frase)
print(acronimo)
#Crear un acrónimo o una abreviatura para 'Codificacion para todos'
def crear_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join(palabra[0].upper() for palabra in palabras)
    return acronimo
frase = "Codificacion para todos"
acronimo = crear_acronimo(frase)
print(acronimo)
#Utilizar el índex para determinar la posición de la primera aparición de C en Codificación para todos
challenge = 'Codificación para todos'
sub_string = 'c'
print(challenge.index(sub_string))
#Utilizar el índex para determinar la posición de la primera aparición de F en Codificación para todos
challenge = 'Codificación para todos'
sub = 'f'
print(challenge.index(sub_string))
#Utilice rfind para determinar la posición de la última aparición de l en Coding For All People
desafio = 'Coding For All People'
print(desafio.rfind('i')) 
#Utilizar index o find para encontrar la posición de la primera aparición de la palabra 'because' en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
palabra2 = 'You cannot end a sentence with because because because is a conjunction'
string = 'because'
print(palabra2.index(string))
#Utilice rindex para encontrar la posición de la última aparición de la palabra 'because' en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
palabra3 = 'You cannot end a sentence with because because because is a conjunction'
string2 = 'because'
print(palabra2.rindex(string2))
#Elimina la frase 'because because because' en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
frase2 = palabra3.replace('because because because','')
print(frase2)
#Encuentra la posición de la primera aparición de la palabra 'because' en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
print(palabra3.index(string2))
#¿''Coding For All' comienza con una subcadena Coding ?
palabra4 = 'Coding For All'
print(palabra4.startswith("Coding"))
#¿'Coding For All' termina con una subcadena 'coding '?
print(palabra4.endswith("Coding"))
#'   Coding For All      ' , elimina los espacios finales izquierdo y derecho en la cadena dada.
palabra5 = "   Coding For All      "
palabra5_sin_espacios = palabra5.strip()
print(palabra5_sin_espacios)
'''
¿Cuál de las siguientes variables devuelve Verdadero cuando usamos el método isidentifier()?
-30 días de Python
-Treinta_días_de_Python
'''
palabra6 = "30 dias de python"
print(palabra6.isidentifier()) #false
palabra7 = "treinta_dias_de_python"
print(palabra7.isidentifier()) #true
#['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únir la lista con un hash con una cadena de espacios
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
cadena_unida = " ".join(librerias)
print(cadena_unida)
#Utilizar la secuencia de escape de nueva línea para separar las oraciones.
mensaje = "I am enjoying this challenge.\nI just wonder what is next."
print(mensaje)
#Utilizar una secuencia de escape de tabulación para escribir las líneas.
informacion = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(informacion)
#utilizar el método de formato de cadena para mostrar lo siguiente:
radio = 10
area = 3.14 * radio ** 2
mensaje = "The area of a circle with radius {} is {} meters square.".format(radio, area)
print(mensaje)
#Realizar lo siguiente utilizando métodos de formato de cadena:
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}") 
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")