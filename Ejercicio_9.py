# 9.Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

ano = int(input("Ingresa año: ")) # Solicita al usuario que ingrese un año

if ano % 4 == 0 and ano % 100 != 0 : #verificación de si el año es bisiesto
    print(f"El año {ano} es bisiesto") 
else:
    print("El año no es bisiesto") # Si no cumple con la condición, no es bisiesto