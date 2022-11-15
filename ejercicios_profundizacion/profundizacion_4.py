# CODE:9
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

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
El objetivo es realizar un programa que determine
cual sería el apellido de una persona
al ingresara los dos nombres completos de sus padres/madres/tutores.
(un solo nombre y un solo apellido en cada caso)
En definitiva se solicita crear una variable nueva que reuna
los dos apellidos.

- Consultar e ingresar por consola el primer nombre completo
- Consultar e ingresar por consola el segundo nombre completo
- Luego debe consultar solo nombre del hijo/a
- Debe extraer los apellidos de los padres (ver la nota al final)
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres/madres/tutores y el nombre del hijo/a
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejamos por su cuenta a que busquen un poco más
acerca de este método llamado split, que seguramente
utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

¡Cualquier duda con el método split pueden consultarnos!

Alumno:
- Crear una una variable llamada nombre_completo_1
  para almacenar el primer nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre_completo_2
  para almacenar el primer nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre
  para almacenar el nombre del hijo/a que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Cuando utilice la función split para dividir
  el nombre_completo_1, almacene los resultados
  en las variables llamadas nombre_1 y apellido_1
  Imprimir en consola el contenido de estas variables

- Cuando utilice la función split para dividir
  el nombre_completo_2, almacene los resultados
  en las variables llamadas nombre_2 y apellido_2
  Imprimir en consola el contenido de estas variables

- Crear una una variable llamada hijo
  para almacenar el nombre del hijo/a contenido en
  la variable nombre sumando/concatenando
  los apellidos almaecnados en apellido_1 y apellido_2
  Imprimir en consola el contenido de esta variable

'''

print('Jugando con texto')
# Empezar aquí la resolución del ejercicio
'''
x = 'blue-red-green'
x.split('-')
a,b,c = x.split('-')

print(a)
'''
nombre_completo_1 = str(input('Ingrese el nombre y apellido del padre:'))
nombre_completo_2 = str(input('Ingrese el nombre y apellido de la madre:'))
nombre = str(input('Ingrese el nombre del hijo/a:'))

print('Nombre completo del padre:', nombre_completo_1, 
      '\nNombre completo de la madre:', nombre_completo_2, 
      '\nNombre del hijo/a:', nombre)

nombre_completo_1.split(' ')
nombre_1,apellido_1 = nombre_completo_1.split(' ')
nombre_completo_2.split(' ')
nombre_2,apellido_2 = nombre_completo_2.split(' ')

print('Nombre del padre:',nombre_1,
      '\nApellido del padre:',apellido_1,
      '\nNombre de la madre:', nombre_2,
      '\nApellido de la madre:',apellido_2)

hijo = nombre + ' ' + apellido_1 + ' ' + apellido_2
print('Nombre completo del hijo/a:',hijo)