# 7. Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.
# Se solicita al usuario que ingrese dos números enteros
num = int(input("Ingresa primer numero: "))

num1 = int(input("Ingresa segundo numero:"))


if num > num1:# Se compara si el primer número es mayor que el segundo
    print(f"El {num} es mayor que {num1}")
else:
    print(f"El {num1} es menor que {num}")

if num == num1:# Se evalúa si los dos números son iguales
    print(f"El numero{num1} y {num} son iguales")