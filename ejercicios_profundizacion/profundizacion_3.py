# CODE:8
# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

¡Cualquier duda con estos métodos pueden consultarnos!

Alumno:
- Crear una una variable llamada nombre_completo
  para almacenar el nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_lower
  para almacenar el nombre completo con todas
  las letras transformadas a minúsculas
  por la función lower
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_upper
  para almacenar el nombre completo con todas
  las letras transformadas a mayúsculas
  por la función upper
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_capitalize
  para almacenar el nombre completo con
  la primera letra del nombre en mayúscula
  por la función capitalize
  Imprimir en consola el contenido de esta variable

'''

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio

# Para este ejercicio logre 2 formas distintas de llegar al mismo resultado
# Primera forma:
 
nombre_completo = str(input('Ingrese su nombre y apellido:'))

print('Su nombre:',nombre_completo, 
      '\nSu nombre en minusculas:', str.lower(nombre_completo), 
      '\nSu nombre en mayusculas:', str.upper(nombre_completo), 
      '\nSu nombre solo con la primer letra mayuscula:', str.capitalize(nombre_completo))

# Segunda forma:

nombre_completo = str(input('Ingrese su nombre y apellido:'))
print('Su nombre:',nombre_completo)

nombre_lower = str.lower(nombre_completo)
print('Su nombre en minusculas:',nombre_lower)

nombre_upper = str.upper(nombre_completo)
print('Su nombre en mayusculas:', nombre_upper)

nombre_capitalize = str.capitalize(nombre_completo)
print('Su nombre solo con la primer letra mayuscula:', nombre_capitalize)