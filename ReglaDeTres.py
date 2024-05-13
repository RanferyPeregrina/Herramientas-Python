print("")
print("--------------La cosa está así---------------")
print("El valor x... Equivale al y")
print("Entonces el valor z equivale a: [Respuesta]")
print("Entonces responde: ")


print()
i = 1
Valor1 = float(input(f"El valor {i}:  "))
Valor2= float(input(f"Equivale a :  "))
while(True):
    Valor3 = float(input(f"Entonces el valor:  "))
    Valor4 = (Valor3 * Valor2) / Valor1
    print(f"Equivale a: {Valor4}")