print("="*50)
Limite = int(input ("Ingrese el número hasta el que quiere llegar:  "))

Numero1 = 0
Numero2 = 1
for Numero in range(Limite):
    print(Numero1)
    NumeroActual = Numero1 + Numero2
    Numero1 = Numero2
    Numero2 = NumeroActual
    