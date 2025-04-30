# 10. Número Dentro de Rango pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive).

num = int(input("Ingresa numero para verificar: "))# Solicita al usuario que ingrese un número 

if num in range(0,11):# Verifica si el número ingresado está dentro del rango de 0 a 10
    print(f"El numero {num} esta dentro del rango")
else:
    print(f"El numero {num} no esta dentro del rango")# Si el número no está dentro del rango