import random

def CrearListaPokemon(RespuestaLista, CantidadEntrenadores):
    Pokemon = []
    if RespuestaLista == 1:
        for i in range(CantidadEntrenadores * 6):
            PokemonNuevo = input(f'Ingrese un pokémon (Restan {(CantidadEntrenadores * 6) - (i)} espacios)')
            Pokemon.append(PokemonNuevo)

    elif RespuestaLista == 2:
        PokemonTematica = []
        print('Ingresa tooodos los pokémon de tu lista temática a continuación, separados por un salto de línea cada uno.')
        print('Para terminar, escribe TERMINAR y presiona ENTER. \n\n')

        while True:
            PokemonIngresado = input('Ingrese pokémon:  ').strip()

            if PokemonIngresado.strip() == '': continue
            if PokemonIngresado.lower() == 'terminar': break
            PokemonTematica.append(PokemonIngresado)

        Pokemon = random.sample(PokemonTematica, (CantidadEntrenadores * 6))

    return Pokemon

        
CantidadEntrenadores = int(input('¿Cuántos entrenadores van a participar?:  '))
print(f'\n¿Traen su lista con con {CantidadEntrenadores * 6} pokémon o se elegirán al azar de una lista más grande?')
print('1.- La traemos.')
print(f'2.- Traemos una mega lista y no hemos elegido los {CantidadEntrenadores * 6}')
ListaDisponible = int(input('Respuesta:  '))

Pokemon = CrearListaPokemon(ListaDisponible, CantidadEntrenadores)
print(f'\nLos pokemon disponibles son: {Pokemon}')

for j in range(CantidadEntrenadores):
    print(f'Entrenador {j + 1}')
    for k in range(6):
        PokemonElegido = random.choice(Pokemon)
        print(PokemonElegido)
        Pokemon.remove(PokemonElegido)
    print('\n')