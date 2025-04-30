# 15. ¿Está en la lista de invitados?

#     Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#     Pide al usuario su nombre.
#     Usa if para decir si está en la lista de invitados o no.

list =list(["Jhoiver","Maria","Yadiel", "Sofia","Ana"]) # Crea una lista 

nombre = str(input("Ingresa tu nombre: "))# Solicita al usuario que ingrese su nombre

if nombre in list:# Verifica si el nombre ingresado está en la lista
  print(f"El nombre de {nombre} esta en la lista de invitados")

else:
  print(f"El nombre de {nombre} no esta en la lista de invitados")# Si el nombre no está en la lista
    
            