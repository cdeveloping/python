### LISTAS ###

my_list = list()
my_order_list = []


print(len(my_list))

my_list = [45, 38, 4, 1, 5, 1]
print(my_list)

my_order_list = [45, 1.80, "Carlos", "Pascual"]

print(type(my_order_list))

print(my_order_list[0])

print(my_order_list.count(1)) #Count contará las veces que se repite el parámetro que le indiquemos.

# Podemos "asignarle" un nombre a cada elemento de la lista

age, height, name, surname = my_order_list
print(age) #Imprimirá en este caso el primer valor, el nombre es meramente descriptivo, ya que el programa no sabe que es la edad lo que representa.


my_order_list.append("cdeveloping") # Al utilizar append, lo que hacemos es añadir un elemento nuevo al final de la lista
print(my_order_list)

my_order_list.insert(1, "Verde") # Utilizando la opción insert, introduciremos el valor que queremos en la posición que indiquemos.
print(my_order_list)

my_order_list.remove("Verde") # Remove eliminará el valor que indiquemos, pero solo el primero si está repetido
print(my_order_list)


my_new_list = my_list.copy() # copiamos la lista a la variable que hemos creado.

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # Sort nos ordenará la lista de mayor a menor o alfabeticamente dependiendo del tipo de datos.
print(my_new_list)


### Fin de las listas ###
