#4. Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".

Contra1 = "python123" # Se define una contraseña correcta como cadena de texto
Contra = str(input("Ingresa contraseña: "))

if Contra == Contra1: # Se compara la contraseña ingresada con la contraseña correcta
    print ("Acceso concedido") 
else:
    print("Contraseña incorrecta")