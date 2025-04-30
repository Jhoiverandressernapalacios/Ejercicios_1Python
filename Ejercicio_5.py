# 5. Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

cuenta = float(input("Ingresa el total de tu cuenta: "))# Solicita al usuario que ingrese el total de la cuenta
porcentaje = int(input("porcentaje deseado: "))


if porcentaje == 10: # Verifica si el porcentaje es 10, 15 o 20, y calcula la propina en cada caso

    propina = (cuenta*porcentaje)/100

    print(f"El valor de la propina es: {propina}")
elif porcentaje == 15:

    propina = (cuenta*porcentaje)/100

    print(f"El valor de la propina es: {propina}")
elif porcentaje == 20:

    propina = (cuenta*porcentaje)/100
    
    print(f"El valor de la propina es: {propina}")
else:
    print("El valor de la propina es incorrecto")     # Si el porcentaje no es válido, muestra un mensaje de error