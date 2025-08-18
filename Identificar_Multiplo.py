print("Identificar si un número es divisible entre otro.")
Numero = int(input("Ingrese su número (Dividendo):  "))
Divisor = int(input("Ingrese su número (Divisor):  "))

if Numero % Divisor == 0:
    print(f"\n El número {Divisor} sí es múltiplo de {Numero}")
    print(f"Es el divisor número: {int(Numero/Divisor)}")
else:
    print(f"\n Este número no es divisor de {Numero}")
    print(f"El número queda dividido como {int(Numero/Divisor)} y sobran {Numero % Divisor}")
