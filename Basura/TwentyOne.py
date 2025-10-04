import random

Cartas_EnJuego = [];
Cartas_PorJugar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
Cartas_Enemigo = [];
Cartas_Propias = [];


def JuegoContar():
    Continuar = True

    while Continuar == 1:
        CartasPosibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
        random.shuffle(CartasPosibles)
        
        print(f"Primer carta: {CartasPosibles[1]}")
        Sumatoria = CartasPosibles[1]
        CartasPosibles.remove(CartasPosibles[1])

        for Carta in CartasPosibles:

                if (Carta + Sumatoria) <= 21:
                    Sumatoria = Sumatoria + Carta
                    print(f"Más: {Carta}")

        Respuesta = int(input("Resultado:  "))

        if Respuesta == Sumatoria:
            print("¡CORRECTO!🎉")
        else: print("Nah.");
        print("\n\n")




        print("¿Quiere continuar?")
        print("1.- Sí")
        print("2.- No")
        Continuar = int(input("Respuesta:  "))
        print("\n\n")
    
    

def IniciarJuego():
    Carta_Inicial = int(input("Cuál es la carta que te tocó al principio:  "))
    Cartas_Propias.append(Carta_Inicial)
    Cartas_PorJugar.remove(Carta_Inicial)
    Cartas_EnJuego.append(Carta_Inicial)

    print("¿Quién inicia jugando?")
    print("1.- Tú")
    print("2.- Otra persona")
    Respuesta = int(input("Respuesta:  "))

    if Respuesta == 1:
        Turno_Propio()
    elif Respuesta == 2:
        Turno_Enemigo()
    else: IniciarJuego()

def Turno_Propio():
    print()
    print("TURNO PROPIO")

    PreguntarCarta_Propia()
    ImprimirTodo()
    Turno_Enemigo()

def Turno_Enemigo():
    print()
    print("TURNO PROPIO")
    PreguntarCarta_Enemigo()
    ImprimirTodo()
    Turno_Propio()

def PreguntarCarta_Propia():
    Carta = int(input("Carta que te tocó: "))

    if Carta in Cartas_EnJuego:
        print("¡Espera, estar carta ya estaba en el juego!")
        Carta = 0
        PreguntarCarta_Propia

    Cartas_Propias.append(Carta)
    Cartas_EnJuego.append(Carta)
    Cartas_PorJugar.remove(Carta)

def PreguntarCarta_Enemigo():
    Carta = int(input("Carta que le tocó a tu adversario: "))

    if Carta in Cartas_EnJuego:
        print("¡Espera, estar carta ya estaba en el juego!")
        Carta = 0
        PreguntarCarta_Enemigo

    Cartas_Enemigo.append(Carta)
    Cartas_EnJuego.append(Carta)
    Cartas_PorJugar.remove(Carta)

def ImprimirTodo():

    print(" =" * 20)
    print(f"Cartas propias:  {Cartas_Propias} con {sum(Cartas_Propias)} puntos")
    print(f"Cartas enemigas:  {Cartas_Enemigo} con {sum(Cartas_Enemigo)} puntos")
    print(f"Cartas posibles cartas disponibles:  {Cartas_PorJugar}")

print("=" * 20)
print("      Twenty One       ")
print("=" * 20)

print("1.- Jugar 21")
print("2.- Practicar sumas de 21")
Eleccion = int(input("Respuesta:  "))
print("\n" * 10)
if Eleccion == 1:
    Eleccion()
elif Eleccion == 2:
    JuegoContar()

