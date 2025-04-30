#6. Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.
numSecre = 520 # Se define el número secreto que el usuario debe adivinar


numSecre1 = int(input("Ingresa numero para adivinar: "))

# Se compara el número ingresado con el número secreto y se imprime un mensaje correspondiente
if numSecre1 > numSecre:
    print("Su número es mayor que numero secreto")

if numSecre1 < numSecre:
     print("Su número es menor que numero secreto")


if numSecre1 == numSecre: 
     print("El numero ingresado es igual a numero secreto")# Si el usuario adivinó el número
