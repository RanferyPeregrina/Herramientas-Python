while True:
    try:
        Limite = int(input('Ingrese el límite al que quiere llegar:  '))
        if Limite < 0:
            print('Ingrese un número mayor a 0')
            continue
        break
    except ValueError:
        print('Pero un número we')

for Numero in range(Limite + 1):
    Salida = ''
    if Numero % 3 == 0: Salida += 'Fizz'
    if Numero % 5 == 0: Salida += 'Buzz'
    if Numero % 7 == 0: Salida += 'Jazz!'
    else: Salida = Numero
    print(Salida)