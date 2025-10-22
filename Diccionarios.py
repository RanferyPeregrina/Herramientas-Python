import random
import time

#Inventario RPG
Inventario = {
    "Poción de vida" : 3,
    "Poción de maná": 2,
    "Flechas": 25,
    "Arco": 1,
    "Espada": 0
}

def Añadir_PocionVida(Inventario):
    Inventario["Poción de vida"] += 1
    return Inventario

def Añadir_PocionMana(Inventario):
    Inventario["Poción de maná"] += 1
    return Inventario

def Quitar_PocionVida(Inventario):
    Inventario["Poción de vida"] -= 1
    return Inventario

def Quitar_PocionMana(Inventario):
    Inventario["Poción de maná"] -= 1
    return Inventario

ListaFunciones = [Añadir_PocionVida, Añadir_PocionMana, Quitar_PocionVida, Quitar_PocionMana]
print("=" * 25)
print("Comienza el viaje de nuestro viajero.")
print()
while True:
    Funcion_Elegida = random.choice(ListaFunciones)
    Inventario = Funcion_Elegida(Inventario)
    print(Inventario)
    if Inventario["Poción de vida"] <= 0: 
        print("Se acabaron las pociones, la aventura termina, hay que volver")
        break
    time.sleep(0.3)
print("=" * 25)

