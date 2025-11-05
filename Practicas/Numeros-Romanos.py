#Programa (De práctica) que convierte números a números romanos.

Numero_Normal = int(input("Ingrese su número:  "))

if Numero_Normal > 1000:
    M = Numero_Normal // 1000
elif Numero_Normal > 100:
    C = Numero_Normal // 100
