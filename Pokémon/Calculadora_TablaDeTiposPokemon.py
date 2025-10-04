import pprint
CantidadPokemon = 0

print("-" *100)
print("          Este programa sirve para calcular lo preparado que está tu equipo pokémon")
print(("         en disposición de tipos, contra qué tipos elementales debes fortalecer etc."))
print("\n")
print("-" *100)

print("\n Cada elemento puede iniciar con una puntuación idéntica a las demás. Pero puedes iniciar con una calibración estándar que considera:")
print(" - Frecuencia de aparición de ese tipo pokémon.")
print(" - Cantidad de movimientos de ese tipo")
print(" - Cantidad de pokémon de ese tipo")
print(" - Potencia de los movimientos de ese tipo")
print(" - Fortaleza de los pokémon de ese tipo")
print()
print("¿Utilizar tabla ponderada?")
print("1.- Sí")
print("2.- No")
print("3.- Ponderarla yo mismo.")
PonderarEleccion = input("    Respuesta:  ")

while True:
    if PonderarEleccion == "1" or PonderarEleccion == "Si":
        print("\nPONDERACIÓN CON PESOS CALIBRADOS\n")
        Tipos ={
            "Agua": -1,
            "Fuego" : 0,
            "Planta" : -1,
            "Electrico" : -1,
            "Volador" : -1,
            "Tierra" : -1,
            "Roca" : -1,
            "Acero" : 0,
            "Hada" : 0,
            "Dragon" : 0,
            "Psiquico" : 0,
            "Siniestro" : -1,
            "Fantasma" : 0,
            "Veneno" : -2,
            "Bicho" : -1,
            "Lucha" : -1,
            "Hielo" : 0,
            "Normal" : 1
        }
        SeleccionDefensiva = True

    elif PonderarEleccion == "2" or PonderarEleccion == "No":
        print("\nPONDERACIÓN AUTOMÁTICA\n")
        Tipos ={
            "Agua": -1,
            "Fuego" : -1,
            "Planta" : -1,
            "Electrico" : -1,
            "Volador" : -1,
            "Tierra" : -1,
            "Roca" : -1,
            "Acero" : -1,
            "Hada" : -1,
            "Dragon" : -1,
            "Psiquico" : -1,
            "Siniestro" : -1,
            "Fantasma" : -1,
            "Veneno" : -1,
            "Bicho" : -1,
            "Lucha" : -1,
            "Hielo" : -1,
            "Normal" : -1
        }
        SeleccionDefensiva = False
        
    elif PonderarEleccion == "3" or PonderarEleccion == "Ponderarla yo mismo":
        tipos_Disponibles =[
            "Acero", "Agua", "Bicho", "Dragon", "Eléctrico", "Fantasma", "Fuego",
            "Hada", "Hielo", "Lucha", "Normal", "Planta", "Psiquico", "Roca",
            "Siniestro", "Tierra", "Veneno", "Volador"
        ]

        Tipos = {}

        for tipo in tipos_Disponibles:
            while True:
                try:
                    Valor = int(input(f"Ingrese una puntuación para el {tipo}:  "))
                    Tipos[tipo] = Valor
                except ValueError:
                    print("Por favor, ingrese un número entero válido.")

    break


def CambiarFuego(Tipos):
    #Debil para atacar
    Tipos["Agua"] -= 1
    Tipos["Dragon"] -= 1
    Tipos["Fuego"] -= 1
    Tipos["Roca"] -= 1
    #Debil para resistir
    Tipos["Agua"] -= 1
    Tipos["Roca"] -= 1
    Tipos["Tierra"] -= 1

    #Fuerte para atacar
    Tipos["Acero"] += 1
    Tipos["Bicho"] += 1
    Tipos["Hielo"] += 1
    Tipos["Planta"] += 1
    #Fuerte para resistir
    Tipos["Acero"] += 1
    Tipos["Fuego"] += 1
    Tipos["Bicho"] += 1
    Tipos["Hada"] += 1
    Tipos["Hielo"] += 1
    Tipos["Planta"] += 1
    return Tipos
    
def CambiarAcero(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Agua"] -= 1
    Tipos["Fuego"] -= 1
    Tipos["Electrico"] -= 1
    #Debil para resistir
    Tipos["Fuego"] -= 1
    Tipos["Lucha"] -= 1
    Tipos["Tierra"] -= 1

    #Fuerte para atacar
    Tipos["Hada"] += 1
    Tipos["Roca"] += 1
    Tipos["Hielo"] += 1
    #Fuerte para resistir
    Tipos["Acero"] += 1
    Tipos["Dragon"] += 1
    Tipos["Bicho"] += 1
    Tipos["Hada"] += 1
    Tipos["Hielo"] += 1
    Tipos["Normal"] += 1
    Tipos["Planta"] += 1
    Tipos["Psiquico"] += 1
    Tipos["Roca"] += 1
    Tipos["Veneno"]

    return Tipos

def CambiarAgua(Tipos):
    #Debil para atacar
    Tipos["Dragon"] -= 1
    Tipos["Agua"] -= 1
    Tipos["Planta"] -= 1
    #Debil para resistir
    Tipos["Electrico"] -= 1
    Tipos["Planta"] -= 1
    
    #Fuerte para atacar
    Tipos["Fuego"] += 1
    Tipos["Roca"] += 1
    Tipos["Tierra"] += 1
    #Fuerte para resistir
    Tipos["Acero"] += 1
    Tipos["Agua"] += 1
    Tipos["Fuego"] += 1
    Tipos["Hielo"] += 1

    return Tipos

def CambiarBicho(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Agua"] -= 1
    Tipos["Fantasma"] -= 1
    Tipos["Fuego"] -= 1
    Tipos["Lucha"] -= 1
    Tipos["Veneno"] -= 1
    Tipos["Volador"] -= 1
    #Debil para resistir
    Tipos["Fuego"] -= 1
    Tipos["Roca"] -= 1

    #Fuerte para atacar
    Tipos["Planta"] += 1
    Tipos["Psiquico"] += 1
    Tipos["Siniestro"] += 1
    #Fuerte para resistir
    Tipos["Planta"] += 1
    Tipos["Lucha"] += 1
    Tipos["Tierra"] += 1

    return Tipos

def CambiarDragon(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Hada"] -= 1
    #Debil para resistir
    Tipos["Dragon"] -= 1
    Tipos["Hada"] -= 1
    Tipos["Hielo"] -= 1

    #Fuerte para atacar
    Tipos["Dragon"] += 1
    #Fuerte para resistir
    Tipos["Planta"] += 1
    Tipos["Agua"] += 1
    Tipos["Electrico"] += 1
    Tipos["Fuego"] += 1

    return Tipos

def CambiarElectrico(Tipos):
    #Debil para atacar
    Tipos["Electrico"] -= 1
    Tipos["Dragon"] -= 1
    Tipos["Planta"] -= 1
    Tipos["Tierra"] -= 1
    #Debil para resistir
    Tipos["Tierra"] -= 1

    #Fuerte para atacar
    Tipos["Agua"] += 1
    Tipos["Volador"] += 1
    #Fuerte para resistir
    Tipos["Acero"] += 1
    Tipos["Electrico"] += 1
    Tipos["Volador"] += 1

    return Tipos

def CambiarFantasma(Tipos):
    #Debil para atacar
    Tipos["Normal"] -= 1
    Tipos["Siniestro"] -= 1
    #Debil para resistir
    Tipos["Fantasma"] -= 1
    Tipos["Siniestro"] -= 1

    #Fuerte para atacar
    Tipos["Fantasma"] += 1
    Tipos["Psiquico"] += 1
   #Fuerte para resistir
    Tipos["Bicho"] += 1
    Tipos["Lucha"] += 1
    Tipos["Normal"] += 1
    Tipos["Veneno"] += 1
    return Tipos

def CambiarHada(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Veneno"] -= 1
    Tipos["Fuego"] -= 1
    #Debil para resistir
    Tipos["Acero"] -= 1
    Tipos["Veneno"] -= 1

    #Fuerte para atacar
    Tipos["Dragon"] += 1
    Tipos["Lucha"] += 1
    Tipos["Siniestro"] += 1
    #Fuerte para resistir
    Tipos["Lucha"] += 1
    Tipos["Dragon"] += 1
    Tipos["Bicho"] += 1
    Tipos["Siniestro"] += 1

    return Tipos

def CambiarHielo(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Agua"] -= 1
    Tipos["Fuego"] -= 1
    Tipos["Lucha"] -= 1
    #Debil para resistir
    Tipos["Fuego"] -= 1
    Tipos["Lucha"] -= 1
    Tipos["Acero"] -= 1
    Tipos["Roca"] -= 1

    #Fuerte para atacar
    Tipos["Dragon"] += 1
    Tipos["Planta"] += 1
    Tipos["Tierra"] += 1
    Tipos["Volador"] += 1

    #Fuerte para resistir
    Tipos["Hielo"] += 1

    return Tipos
 
def CambiarLucha(Tipos):
    #Debil para atacar
    Tipos["Bicho"] -= 1
    Tipos["Hada"] -= 1
    Tipos["Psiquico"] -= 1
    Tipos["Veneno"] -= 1
    Tipos["Volador"] -= 1
    Tipos["Fantasma"] -= 1
    #Debil para resistir
    Tipos["Hada"] -= 1
    Tipos["Volador"] -= 1
    Tipos["Psiquico"] -= 1

    #Fuerte para atacar
    Tipos["Acero"] += 1
    Tipos["Normal"] += 1
    Tipos["Siniestro"] += 1
    Tipos["Roca"] += 1
    Tipos["Hielo"] += 1
    #Fuerte para resistir
    Tipos["Bicho"] += 1
    Tipos["Siniestro"] += 1
    Tipos["Roca"] += 1

    return Tipos

def CambiarNormal(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Fantasma"] -= 1
    Tipos["Roca"] -= 1
    #Debil para resistir
    Tipos["Lucha"] -= 1

    #Fuerte para atacar
    #... Oh.

    #Fuerte para resistir
    Tipos["Fantasma"] += 1

    return Tipos

def CambiarPlanta(Tipos):
    #Debil para atacar
    Tipos["Bicho"] -= 1
    Tipos["Acero"] -= 1
    Tipos["Planta"] -= 1
    Tipos["Dragon"] -= 1
    Tipos["Volador"] -= 1
    Tipos["Fuego"] -= 1
    Tipos["Veneno"]
    #Debil para resistir
    Tipos["Bicho"] -= 1
    Tipos["Volador"] -= 1
    Tipos["Fuego"] -= 1
    Tipos["Hielo"] -= 1
    Tipos["Veneno"] -= 1

    #Fuerte para atacar
    Tipos["Agua"] += 1
    Tipos["Roca"] += 1
    Tipos["Tierra"] += 1
    #Fuerte para resistir
    Tipos["Agua"] += 1
    Tipos["Electrico"] += 1
    Tipos["Planta"] += 1
    Tipos["Tierra"]
    return Tipos

def CambiarPsiquico(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Siniestro"] -= 1
    Tipos["Psiquico"] -= 1
    #Debil para resistir
    Tipos["Bicho"] -= 1
    Tipos["Fantasma"] -= 1
    Tipos["Siniestro"] -= 1

    #Fuerte para atacar
    Tipos["Lucha"] += 1
    Tipos["Veneno"] += 1
    #Fuerte para resistir
    Tipos["Lucha"] += 1
    Tipos["Psiquico"] += 1

    return Tipos

def CambiarRoca(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Lucha"] -= 1
    Tipos["Tierra"] -= 1
    #Debil para resistir
    Tipos["Acero"] -= 1
    Tipos["Agua"] -= 1
    Tipos["Lucha"] -= 1
    Tipos["Planta"] -= 1
    Tipos["Tierra"] -= 1

    #Fuerte para atacar
    Tipos["Bicho"] += 1
    Tipos["Fuego"] += 1
    Tipos["Hielo"] += 1
    Tipos["Volador"] += 1
    #Fuerte para resistir
    Tipos["Normal"] += 1
    Tipos["Veneno"] += 1
    Tipos["Volador"] += 1
    return Tipos

def CambiarSiniestro(Tipos):
    #Debil para atacar
    Tipos["Lucha"] -= 1
    Tipos["Hada"] -= 1
    Tipos["Siniestro"] -= 1
    #Debil para resistir
    Tipos["Bicho"] -= 1
    Tipos["Hada"] -= 1
    Tipos["Lucha"] -= 1

    #Fuerte para atacar
    Tipos["Fantasma"] += 1
    Tipos["Psiquico"] += 1
    #Fuerte para resistir
    Tipos["Fantasma"] += 1
    Tipos["Siniestro"] += 1

    return Tipos

def CambiarTierra(Tipos):
    #Debil para atacar
    Tipos["Bicho"] -= 1
    Tipos["Planta"] -= 1
    Tipos["Volador"] -= 1
    #Debil para resistir
    Tipos["Agua"] -= 1
    Tipos["Hielo"] -= 1
    Tipos["Planta"] -= 1

    #Fuerte para atacar
    Tipos["Acero"] += 1
    Tipos["Electrico"] += 1
    Tipos["Fuego"] += 1
    Tipos["Roca"] += 1
    Tipos["Veneno"] += 1
    #Fuerte para resistir
    Tipos["Bicho"] += 1
    Tipos["Siniestro"] += 1
    Tipos["Roca"] += 1
    Tipos["Electrico"] += 1

    return Tipos

def CambiarVeneno(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Fantasma"] -= 1
    Tipos["Roca"] -= 1
    Tipos["Veneno"] -= 1
    Tipos["Tierra"] -= 1
    #Debil para resistir
    Tipos["Tierra"] -= 1
    Tipos["Psiquico"] -= 1

    #Fuerte para atacar
    Tipos["Hada"] += 1
    Tipos["Planta"] += 1
    #Fuerte para resistir
    Tipos["Bicho"] += 1
    Tipos["Hada"] += 1
    Tipos["Lucha"] += 1
    Tipos["Planta"] += 1
    Tipos["Veneno"] += 1

    return Tipos

def CambiarVolador(Tipos):
    #Debil para atacar
    Tipos["Acero"] -= 1
    Tipos["Electrico"] -= 1
    Tipos["Roca"] -= 1
    #Debil para resistir
    Tipos["Electrico"] -= 1
    Tipos["Hielo"] -= 1
    Tipos["Roca"] -= 1

    #Fuerte para atacar
    Tipos["Bicho"] += 1
    Tipos["Lucha"] += 1
    Tipos["Planta"] += 1
    #Fuerte para resistir
    Tipos["Bicho"] += 1
    Tipos["Lucha"] += 1
    Tipos["Planta"] += 1
    Tipos["Tierra"] += 1

    return Tipos


print("= "*20)
print("Ahora ingresar los tipos de cada pokémon que forman su equipo:")


while(True):
    while(True):
        Cantidad_Tipos = input("\n¿Su pokemon tiene 1 o 2 tipos?:  ")
        if Cantidad_Tipos == "1" or Cantidad_Tipos == "2":
            break
    if Cantidad_Tipos == "1":
        while True:
            print("\n¿De qué tipo es su Pokémon?")
            print("1.- Acero")
            print("2.- Agua")
            print("3.- Bicho")
            print("4.- Dragon")
            print("5.- Eléctrico")
            print("6.- Fantasma")
            print("7.- Fuego")        
            print("8.- Hada")
            print("9.- Hielo")
            print("10.- Lucha")
            print("11.- Normal")
            print("12.- Planta")
            print("13.- Psiquico")
            print("14.- Roca")
            print("15.- Siniestro")
            print("16.- Tierra")
            print("17.- Veneno")
            print("18.- Volador")
            Tipo_Elegido = input(" - - - - - - Respuesta:  ")

            if Tipo_Elegido == "Acero" or Tipo_Elegido == "1":
                Tipos = CambiarAcero(Tipos)
                break
            elif Tipo_Elegido == "Agua" or Tipo_Elegido == "2":
                Tipos = CambiarAgua(Tipos)
                break
            elif Tipo_Elegido == "Bicho" or Tipo_Elegido == "3":
                Tipos = CambiarBicho(Tipos)
                break
            elif Tipo_Elegido == "Dragon" or Tipo_Elegido == "4":
                Tipos = CambiarDragon(Tipos)
                break
            elif Tipo_Elegido == "Electrico" or Tipo_Elegido == "5":
                Tipos = CambiarElectrico(Tipos)
                break
            elif Tipo_Elegido == "Fantasma" or Tipo_Elegido == "6":
                Tipos = CambiarFantasma(Tipos)
                break
            elif Tipo_Elegido == "Fuego" or Tipo_Elegido == "7":
                Tipos = CambiarFuego(Tipos)
                break
            elif Tipo_Elegido == "Hada" or Tipo_Elegido == "8":
                Tipos = CambiarHada(Tipos)
                break
            elif Tipo_Elegido == "Hielo" or Tipo_Elegido == "9":
                Tipos = CambiarHielo(Tipos)
                break
            elif Tipo_Elegido == "Lucha" or Tipo_Elegido == "10":
                Tipos = CambiarLucha(Tipos)
                break
            elif Tipo_Elegido == "Normal" or Tipo_Elegido == "11":
                Tipos = CambiarNormal(Tipos)
                break
            elif Tipo_Elegido == "Planta" or Tipo_Elegido == "12":
                Tipos = CambiarPlanta(Tipos)
                break
            elif Tipo_Elegido == "Psiquico" or Tipo_Elegido == "13":
                Tipos = CambiarPsiquico(Tipos)
                break
            elif Tipo_Elegido == "Roca" or Tipo_Elegido == "14":
                Tipos = CambiarRoca(Tipos)
                break
            elif Tipo_Elegido == "Siniestro" or Tipo_Elegido == "15":
                Tipos = CambiarSiniestro(Tipos)
                break
            elif Tipo_Elegido == "Tierra" or Tipo_Elegido == "16":
                Tipos = CambiarTierra(Tipos)
                break
            elif Tipo_Elegido == "Veneno" or Tipo_Elegido == "17":
                Tipos = CambiarVeneno(Tipos)
                break
            elif Tipo_Elegido == "Volador" or Tipo_Elegido == "18":
                Tipos = CambiarVolador(Tipos)
                break
            else:
                print("Entrada no válida, intente de nuevo.")


    elif Cantidad_Tipos == "2":
        for i in range(2):
            while True:
                print("\n¿De qué tipo es su Pokémon?")
                print("1.- Acero")
                print("2.- Agua")
                print("3.- Bicho")
                print("4.- Dragon")
                print("5.- Eléctrico")
                print("6.- Fantasma")
                print("7.- Fuego")        
                print("8.- Hada")
                print("9.- Hielo")
                print("10.- Lucha")
                print("11.- Normal")
                print("12.- Planta")
                print("13.- Psiquico")
                print("14.- Roca")
                print("15.- Siniestro")
                print("16.- Tierra")
                print("17.- Veneno")
                print("18.- Volador")
                Tipo_Elegido = input(" - - - - - - Respuesta:  ")

                if Tipo_Elegido == "Acero" or Tipo_Elegido == "1":
                    Tipos = CambiarAcero(Tipos)
                    break
                elif Tipo_Elegido == "Agua" or Tipo_Elegido == "2":
                    Tipos = CambiarAgua(Tipos)
                    break
                elif Tipo_Elegido == "Bicho" or Tipo_Elegido == "3":
                    Tipos = CambiarBicho(Tipos)
                    break
                elif Tipo_Elegido == "Dragon" or Tipo_Elegido == "4":
                    Tipos = CambiarDragon(Tipos)
                    break
                elif Tipo_Elegido == "Electrico" or Tipo_Elegido == "5":
                    Tipos = CambiarElectrico(Tipos)
                    break
                elif Tipo_Elegido == "Fantasma" or Tipo_Elegido == "6":
                    Tipos = CambiarFantasma(Tipos)
                    break
                elif Tipo_Elegido == "Fuego" or Tipo_Elegido == "7":
                    Tipos = CambiarFuego(Tipos)
                    break
                elif Tipo_Elegido == "Hada" or Tipo_Elegido == "8":
                    Tipos = CambiarHada(Tipos)
                    break
                elif Tipo_Elegido == "Hielo" or Tipo_Elegido == "9":
                    Tipos = CambiarHielo(Tipos)
                    break
                elif Tipo_Elegido == "Lucha" or Tipo_Elegido == "10":
                    Tipos = CambiarLucha(Tipos)
                    break
                elif Tipo_Elegido == "Normal" or Tipo_Elegido == "11":
                    Tipos = CambiarNormal(Tipos)
                    break
                elif Tipo_Elegido == "Planta" or Tipo_Elegido == "12":
                    Tipos = CambiarPlanta(Tipos)
                    break
                elif Tipo_Elegido == "Psiquico" or Tipo_Elegido == "13":
                    Tipos = CambiarPsiquico(Tipos)
                    break
                elif Tipo_Elegido == "Roca" or Tipo_Elegido == "14":
                    Tipos = CambiarRoca(Tipos)
                    break
                elif Tipo_Elegido == "Siniestro" or Tipo_Elegido == "15":
                    Tipos = CambiarSiniestro(Tipos)
                    break
                elif Tipo_Elegido == "Tierra" or Tipo_Elegido == "16":
                    Tipos = CambiarTierra(Tipos)
                    break
                elif Tipo_Elegido == "Veneno" or Tipo_Elegido == "17":
                    Tipos = CambiarVeneno(Tipos)
                    break
                elif Tipo_Elegido == "Volador" or Tipo_Elegido == "18":
                    Tipos = CambiarVolador(Tipos)
                    break
                else:
                    print("Entrada no válida, intente de nuevo.")
   
    CantidadPokemon += 1
    if CantidadPokemon <= 5:
        print("\n¿Introducir otro Pokémon?")
        print("1.- Sí.")
        print("2.- No.")
        Seguir_AñadirPokemon = input("Respuesta:  ")
        if Seguir_AñadirPokemon == "1":
            print("  -"*40)
        elif Seguir_AñadirPokemon == "2":
            print("Pues aquí termina el programa...")
            break;
    else: break;
print("  =="*70)
print("Al final, todo:")
# Ordenar de menor a mayor
Tipos_Ordenados_Menor_Mayor = dict(sorted(Tipos.items(), key=lambda item: item[1]))
for tipo, valor in Tipos_Ordenados_Menor_Mayor.items():
    print(f"{tipo}: {valor}")