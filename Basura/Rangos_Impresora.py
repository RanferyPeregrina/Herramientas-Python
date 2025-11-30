Rango = input('Ingrese su rango en formato: 1, 2, 4, 5-9, 10:  ')
Cadena = ''
def exclusion(Rango):
    Rango_Separado = Rango.split(', ')
    print(Rango_Separado)

    Cadena = ''.join('1 - ', (int(Rango_Separado[0]) - 1))
    return Cadena
Cadena = exclusion(Rango)
print(Cadena)