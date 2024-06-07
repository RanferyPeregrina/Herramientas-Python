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
    Tipos["Agua"] = -1
    


print("= "*20)
print("Ahora ingresar los tipos de cada pokémon que forman su equipo:")
print("")