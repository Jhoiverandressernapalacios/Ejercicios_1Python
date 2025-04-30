# 13. Lista vacía y append()

#     Crea una lista vacía llamada nombres.
#     Pide al usuario su nombre y agrégalo a la lista usando append().
#     Muestra la lista final.

nombre1 = str(input("Ingresa tu nombre: ")) # Solicita al usuario que ingrese su nombre

nombre = list([]) # Crea una lista vacía

nombre.append(nombre1) # Agrega el nombre ingresado a la lista

print (f"El nombre ingresado a la lista es: {nombre}")
