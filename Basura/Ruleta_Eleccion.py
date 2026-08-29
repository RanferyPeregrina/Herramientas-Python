import random
Elecciones = []
Cantidad_Elecciones = int(input("Cantidad de opciones:  "))

for Opcion in range(Cantidad_Elecciones):
    Elecciones.append(input(f"Opción {Opcion + 1}: "))

print(f"La respuesta es: {random.choice(Elecciones)}")