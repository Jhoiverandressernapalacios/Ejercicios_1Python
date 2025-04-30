#3. Pide un número entero. Indica si es par o impar.

num = int(input("Ingresa numero: ")) # Solicita al usuario que ingrese un número entero
R = num % 2 # Calcula el residuo de dividir el número entre 2
if R == 0: # Si el residuo es 0, el número es par
    print(f"El numero {num} es par")  # Si el residuo no es 0, el número es impar
else:
    print(f"El numero {num} es impar")