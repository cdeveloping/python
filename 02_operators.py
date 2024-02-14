# Operadores

### Operadores Aritméticos ###

print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (3 % 4) # Devuelve el resto de una división.
print (3 // 4) # Es una división que siempre devolverá un número entero.
print (2 ** 3) #Calcula el exponente

print ("Hola " +  "Python") #Concatenamos cadenas de texto.

# Para concatenar una cadena de texto con int habrá que transformar el int a str
print("Hola " + str(5))

print ("Hola" * 5) #Multiplica el estring tantas por el int

### Operadores Comparativos ###

print (3 > 4)
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4)

"""
Si comparamos dos string, lo que hace es una ordenación alfabética
"""
print ("Hola" <= "Hola") # Devuelve True
print ("Hola" <= "Bola") #Devuelve False

### Operadores Lógicos ###

"""
Los operadores son:
and
or 
not
"""
print (3 > 4 and "Hola" <= "Bola")
print (3 > 4 or "Hola" <= "Bola")
#
# print (3 > 4 not "Hola" <= "Bola") Esto nos daría un error de ejecución

print(not(3 > 4)) # Aquí estamos negando la comparación por lo que devuelve true

### Fin del bloque de operadores ###
