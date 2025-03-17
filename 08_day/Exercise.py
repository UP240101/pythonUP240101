#Crear un diccionario vacío llamado perro
perro = {}
#Añade nombre, color, raza, patas y edad al diccionario de perros
perro = {'nombre':'chop', 'color':'marron', 'raza':'gran danes', 'patas':'cuatro', 'edad':'10 años'}
print(perro)
#Cree un diccionario de estudiante y agregue nombre, apellido, género, edad, estado civil, habilidades,
#país, ciudad y dirección como claves para el diccionario.
estudiante = {'nombre':'sergio', 'apellido':'martinez', 'genero':'masculino', 'edad':'18', 'estado civil':'soltero',
'habilidades': ['matematicas', 'ingles', 'computadora'], 'pais':'mexico', 'ciudad':'aguascalientes', 'direccion':{'colonia':
'los arellano', 'codigo postal':'20340', 'calle':'rancho san jose'} }
#Obtenga la longitud del diccionario del estudiante
print(len(estudiante))
#Obtenga el valor de las habilidades y verifique el tipo de dato, debe ser una lista
habilidades = estudiante['habilidades']
print(habilidades, type(habilidades))
#Modifique los valores de las habilidades agregando una o dos habilidades

#Obtenga las claves del diccionario como una lista
#Obtener los valores del diccionario como una lista
#Cambie el diccionario a una lista de tuplas usando el método items()
#Eliminar uno de los elementos del diccionario

#Eliminar uno de los diccionarios
del perro