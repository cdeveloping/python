### TUPLES ###


# Como definir una tupla

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (45, 1.82, "Carlos", "Pascual")
print(my_tuple) #Sacamos por pantalla la tupla

print(type(my_tuple)) #Verificamos que es una tupla a través de una salida por consola

# Vamos a acceder a los datos 
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[3])

print(my_tuple.count("Carlos")) #Cuenta las veces que está el valor que le hemos definido en count
print(my_tuple.index("Pascual")) # Nos dice que posición ocupa el valor que definimos en index


# Las tuplas son inmutables, no se pueden modificar.

print(my_tuple[1:3]) # Imprime todos los valores que hay entre esos indices, ellos incluidos.