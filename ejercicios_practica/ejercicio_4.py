# CODE:4
# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
palabra_1 = str(input('Ingrese palabra 1:'))

palabra_2 = str(input('Ingrese palabra 2:'))

palabra_3 = str(input('Ingrese palabra 3:'))

print('Eligio las palabras:', palabra_1, palabra_2, 'y', palabra_3)
# Objetivo:
# De cada palabra ingresada se utilizará
# la primera letra para armar un acrónimo, por ejemplo:
# Si las palabras ingresadas fueran:
# --> Alumbrado, barrido y limpieza
# El acrónimo resultado es --> abl

# Alumno:
# Crear una variable llamada acronimo donde se 
# almacene la primera letra de cada palabra
# en el orden corespondiente
acronimo = (palabra_1[0] + palabra_2[0] + palabra_3[0])
print('El acronimo es:', acronimo)

# Imprimir la variable acronimo en pantalla
