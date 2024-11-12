
print("= " * 50)
Numero_Deseado = int (input("Ingrese el número al que le quiere calcular el factorial:  "))
Numero = Numero_Deseado

while Numero_Deseado != 1:

    print(f"El producto de {Numero} * {Numero_Deseado - 1} es:  {Numero}")

    Numero_Deseado -= 1

print(" - " * 50)
print(f"El factorial es: {Numero}")