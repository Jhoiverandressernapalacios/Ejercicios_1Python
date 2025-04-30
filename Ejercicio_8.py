# 8. Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

#     "Bajo peso" si es menor a 18.5
#     "Normal" si está entre 18.5 y 24.9
#     "Sobrepeso" si está entre 25 y 29.9
#     "Obesidad" si es mayor o igual a 30

peso = float(input("Ingresa tu peso en Kg: "))# Solicitamos al usuario su peso en kilogramos
altura = float(input("Ingresa tu altura en M: "))# Solicitamos al usuario su altura en metros
IMC = peso/altura **2 # Calculamos el IMC 

print(f"Su indice de masa corporal es: {IMC:.2f}") # Mostramos el resultado del IMC con dos decimales

# Clasificamos el IMC según los rangos establecidos y mostramos el mensaje correspondiente.
if IMC < 18.5: 
    print (f"Tu indice de masa corporal es: {IMC:.2f} y esta en el rago de bajaste de peso")

elif 18.5 <= IMC <= 24.9:
    print(f"Tu indice de masa corporal es: {IMC:.2f} y esta en el rago de lo normal") 

elif 25.0 <= IMC <= 29.9:
    print(f"Tu indice de masa corporal es: {IMC:.2f} y esta en el rago de Sobrepeso") 

elif IMC > 30.0:
   print(f"Tu indice de masa corporal es: {IMC:.2f} y esta en el rago de obesidad") 

