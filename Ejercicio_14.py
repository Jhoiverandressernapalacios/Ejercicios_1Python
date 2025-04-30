# 14. Edad válida

#     Pide al usuario su edad.
#     Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
#     Si está en el rango correcto, imprime "Edad válida".

edad = int(input("Ingersa tu edad: "))# Solicita al usuario que ingrese su edad


if 0 <= edad <= 120:# Verifica si la edad ingresada está en el rango de 0 a 120
  print(f" la eddad {edad} es válida")

else:
  print(f"la eddad {edad} no válida")# Si la edad no está dentro del rango válido
