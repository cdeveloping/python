"""
En el primer laboratorio debemos realizar prácticas con la funcion print de Python
Crearemos diferentes lineas con comillas dobles y simples y veremos que errores arroja
al crear fallos en el código de manera intencionada.
"""

print("Esto es una cadena de texto entre comillas dobles.")
print('Esto es una cadena de texto entre comillas simples.')


"""
Vamos a crear errores de manera intencionada eliminando parentesis o comillas.
"""
print("Esto va a generar un error al eliminar el paréntesis final")
print('Si eliminamos el parentesis final, el error generado es el sisguiente:')
print("SyntaxError: '(' was never closed")
print ('Genera un error porque indica que no fue cerrada la función al pasar los parámetros.')

"""
Tampoco podemos poner dos print en una misma linea, esto nos arrojará un error de sintaxis también.
"""