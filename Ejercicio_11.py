# 11. Menor de tres números

#     Pide tres números al usuario.
#     Usa condicionales (if) para decir cuál es el más pequeño.

# Solicita al usuario que ingrese tres números y los convierte a enteros
num1 = int(input("Ingresa numero 1: "))
num2 = int(input("Ingresa numero 2: "))
num3 = int(input("Ingresa numero 3: "))


if num1 < num2 and num1 < num3:# Verifica si el num1 es menor que num2 y num3
    print(f"El numero {num1} es menor que el {num2} y el {num3}")

else:
    if num2 < num1 and num2 < num3:  # Si la primera condición no se cumple, verifica si num2 es el menor
        print(f"El numero {num2} es menor que el {num1} y el {num3}")
    else:
        if num3 < num1 and num3 < num2:# Si ninguna de las condiciones anteriores se cumple, num3 es el menor
            print(f"El numero {num3} es menor que el {num1} y el {num2}")
