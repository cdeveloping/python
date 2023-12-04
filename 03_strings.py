### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

# Concatenamos String

print(my_string + " " + my_other_string)

#Saltos de linea
my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

#Tabulaciones
my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)


#Escape
my_scape_string = "\tEste es un string con \n escape"
print(my_scape_string)

# Formateo

name, surname, age = "Carlos", "Pascual", 45

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Inferencia de datos

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3] # Cogerá los caracteres que esten en la posición indicada
# Si ponemos el valor en negativo empezará por el final.
print(language_slice)


# Reverse - Imprimirá el valor al reves

reverse_language = language
print(reverse_language[::-1])

# Funciones
print(language.capitalize())  #Pone el primer carácter en mayúscula.
print(language.upper()) # Pone todas los carácteres en mayúscula.
print(language.capitalize())
print(language.capitalize())
print(language.capitalize())
print(language.capitalize())

