# Escribir un programa que almacene en una lista los números del 1 al 1
#  y los muestre por pantalla en orden inverso separados por comas.
Numeros = []
for i in range(10):
    Numeros.append(int(input(f"Ingrese el número #{i+1}:  ")))

Numeros.sort()
Numeros_Invertidos = Numeros[::-1]
print(Numeros_Invertidos)