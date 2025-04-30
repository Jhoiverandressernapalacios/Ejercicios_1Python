# 12. Verificar si un número está en una lista

#     Crea una lista con 5 números.
#     Pide un número al usuario y verifica si está en la lista usando in.


num = int(input("Ingresa numero: "))# Solicita al usuario que ingrese un número

list = list([5,8,9,77,2])# Crea una lista

if num in list: # Verifica si el número ingresado está en la lista
  print(f"el numero {num} en la lista")
else:
  print(f"el numero {num} no esta en la lista")# Si el número no está en la lista
