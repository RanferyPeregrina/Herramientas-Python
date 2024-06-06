import pprint

print("-" *100)
print("          Este programa sirve para calcular lo preparado que está tu equipo pokémon")
print(("         en disposición de tipos, contra qué tipos elementales debes fortalecer etc."))
print("-" *100)

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

def CambiarFuego(Tipos):
    #Debil para atacar
    Tipos["Agua"] = -1
    Tipos["Dragon"] = -1
    Tipos["Fuego"] = -1
    Tipos["Roca"] = -1
    #Debil para resistir
    Tipos["Agua"] = -1
    Tipos["Roca"] = -1
    Tipos["Tierra"] = -1

    #Fuerte para atacar
    Tipos["Acero"] = +1
    Tipos["Bicho"] = +1
    Tipos["Hielo"] = +1
    Tipos["Planta"] = +1
    #Fuerte para resistir
    Tipos["Acero"] = +1
    Tipos["Fuego"] = +1
    Tipos["Bicho"] = +1
    Tipos["Hada"] = +1
    Tipos["Hielo"] = +1
    Tipos["Planta"] = +1
    
def CambiarAcero(Tipos):
    #Debil para atacar
    Tipos["Acero"] = -1
    Tipos["Agua"] = -1
    Tipos["Fuego"] = -1
    Tipos["Electrico"] = -1
    #Debil para resistir
    Tipos["Fuego"] = -1
    Tipos["Lucha"] = -1
    Tipos["Tierra"] = -1

    #Fuerte para atacar
    Tipos["Hada"] = +1
    Tipos["Roca"] = +1
    Tipos["Hielo"] = +1
    #Fuerte para resistir
    Tipos["Acero"] = +1
    Tipos["Dragon"] = +1
    Tipos["Bicho"] = +1
    Tipos["Hada"] = +1
    Tipos["Hielo"] = +1
    Tipos["Normal"] = +1
    Tipos["Planta"] = +1
    Tipos["Psiquico"] = +1
    Tipos["Roca"] = +1

def CambiarAgua(Tipos):
    #Debil para atacar
    Tipos["Dragon"] = -1
    Tipos["Agua"] = -1
    Tipos["Planta"] = -1
    #Debil para resistir
    Tipos["Electrico"] = -1
    Tipos["Planta"] = -1

    #Fuerte para atacar
    Tipos["Fuego"] = +1
    Tipos["Roca"] = +1
    Tipos["Tierra"] = +1
    #Fuerte para resistir
    Tipos["Acero"] = +1
    Tipos["Agua"] = +1
    Tipos["Fuego"] = +1
    Tipos["Hielo"] = +1

def CambiarBicho(Tipos):
    #Debil para atacar
    Tipos["Acero"] = -1
    Tipos["Agua"] = -1
    Tipos["Fantasma"] = -1
    Tipos["Fuego"] = -1
    Tipos["Lucha"] = -1
    Tipos["Veneno"] = -1
    Tipos["Volador"] = -1
    #Debil para resistir
    Tipos["Fuego"] = -1
    Tipos["Roca"] = -1

    #Fuerte para atacar
    Tipos["Planta"] = +1
    Tipos["Psiquico"] = +1
    Tipos["Siniestro"] = +1
    #Fuerte para resistir
    Tipos["Planta"] = +1
    Tipos["Lucha"] = +1
    Tipos["Tierra"] = +1

def CambiarDragon(Tipos):
    #Debil para atacar
    Tipos["Acero"] = -1
    Tipos["Hada"] = -1
    #Debil para resistir
    Tipos["Dragon"] = -1
    Tipos["Hada"] = -1
    Tipos["Hielo"] = -1

    #Fuerte para atacar
    Tipos["Dragon"] = +1
    #Fuerte para resistir
    Tipos["Planta"] = +1
    Tipos["Agua"] = +1
    Tipos["Electrico"] = +1
    Tipos["Fuego"] = +1

def CambiarElectrico(Tipos):
    #Debil para atacar
    Tipos["Electrico"] = -1
    Tipos["Dragon"] = -1
    Tipos["Planta"] = -1
    Tipos["Tierra"] = -1
    #Debil para resistir
    Tipos["Tierra"] = -1


    #Fuerte para atacar
    Tipos["Planta"] = +1
    Tipos["Psiquico"] = +1
    Tipos["Siniestro"] = +1
    #Fuerte para resistir
    Tipos["Planta"] = +1
    Tipos["Lucha"] = +1
    Tipos["Tierra"] = +1


print("= "*20)
print("Ahora ingresar los tipos de cada pokémon que forman su equipo:")
print("")