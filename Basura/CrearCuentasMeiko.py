import random

CantidadOperaciones = int(input('¿Cuántas operaciones vamos a practicar?:  '))
for i in range(CantidadOperaciones):

    Numero1 = random.randint(-20, 20)
    Numero2 = random.randint(-20, 20)
    Respuesta = Numero1 + Numero2

    if Numero2 >= 0: Numero2 = f'+ {Numero2}'
    elif Numero2 < 0: Numero2 = f'- {abs(Numero2)}'
    
    print(f'Pregunta {i + 1}:  {Numero1} {Numero2}:  ')
    print(f'Respuesta: {Respuesta}')

    with open('CuentasMeiko.txt', 'a') as Archivo:
        Archivo.write(f'\nPregunta {i + 1}:  {Numero1} {Numero2}:  ')
        Archivo.write(f'\nRespuesta: {Respuesta}')
        Archivo.write(f'\nVamos con el siguiente.')

input('Programa finalizado. Presione Enter.')