#Esto es para hacer pruebas y experimentos
print('\n' * 3)
N1 = int(input('Ingrese su número:  '))
N2 = int(input('Ingrese divisor:  '))

Division = int(N1/N2)
Residuo = N1 % N2
Inicio = 0
Final = Division

for i in range(1, N2+1):
    Final = Division * i
    if i == N2: Final = Cantidad_Paginas
    print(f'Parte {i} es desde {Inicio + 1} hasta {Final}')
    if Final % 2 != 0: Final += 1
    Inicio = Final
