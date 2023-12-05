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


#### FIN PRIMERA PARTE DE LAS LISTAS ####
