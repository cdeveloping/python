# Creación de variables en Python

# MyVariable = "My String Variable"  # Esta forma no sería correcta de nombrar una variable

my_string_variable = "My String Variable"

print(my_string_variable)

# Variable int
my_int_variable = 5
print(my_int_variable)

# Variable tipo boolean
my_bool_variable = True
print(my_bool_variable)

# Pasamos varios argumentos al print  y concatenamos los datos 
print(my_string_variable, my_int_variable)

# Otra forma de concatenación
print("El valor de my_bool_variable: ", my_bool_variable)

# Vamos a transformar una cadena int a una str
my_int_to_str_variable = str(my_int_variable) # Asignamos a la variable el valor de la variable int convirtiendola a string
print(my_int_to_str_variable) # Salida por consola del valor de la variable
print(type(my_int_to_str_variable)) # Mostramos por consola el tipo de variable en la que hemos convertido la misma.

#Algunas funciones del sistema

# Funcion LEN
print(len(my_string_variable))
"""
Esta función lo que hace es contar el número de carácteres que tiene la variable
en este caso my_string_variable tiene 18 carácteres y es lo que nos mostrará
en la salida por consola.
"""


#Variables en una sola línea
name, surname, alias, age = "Carlos", "Pascual", "cdeveloping", 45 # Hemos creado tres strings y un int ¡ Esta sintaxis es una mala práctica!
print("Mi nombre es: ", name, surname, ". Mi edad es: ", age, ". Y mi alias en GitHub es: ", alias) 

#Inputs
#La consola detendrá la ejecución a la espera de que le demos datos
name = input("¿Cuál es tu nombre?")
age = input("¿Cuál es tu edad?")

print("Bienvenido ", name, " tu edad es: ", age, " años.")

"""
Las variables como su nombre indica pueden variar su valor
en el siguiente ejemplo vamos a cambiar el valor de algunoas de ellas.
"""

name = 123
age = "cdeveloping"

print(name)
print(age)

# Forzamos el tipo de dato
address: str = "Mi dirección"

