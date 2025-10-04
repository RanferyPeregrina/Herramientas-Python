import requests #Librería para hacer consultas a APIs.
import pandas as pd #Librería para manejar datos en formas de tablas o más ordenados en general.

def PreguntarImpresion():
    Imprimir = input("¿Imprimir? (Sí/No):  ")
    if Imprimir.lower() == "si": Impresion = True
    else: Impresion = False
    return Impresion

def Obtener_Datos_Pokemon(nombre_Pokemon):
    #Define la URL que usará como: PokeAPI-NombreDelPokemonSolicitado (en minúsculas)
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_Pokemon.lower()}" 
    respuesta = requests.get(url)        #Hacemos una petición http GET del servidor
    data = respuesta.json()              #Guardamos toda la respuesta a esa petición
                                         #En un objeto Json, seguramente una lista.
    #Esta respuesta "data" no sólo tiene los datos que nos interesan. Tiene en realidad
    #toda la información de la respuesta. Sólo por seguridad por si después ocupamos
    #datos de la respuesta.
    #Por ejemplo:   response.status_code:   200 es bueno.
                #                           404 es malo.
                #   response.headers:       Metadatos
                #   response.content:       Lo mero chingón

    if Impresion == True:
        print(f"Código de la consulta: {respuesta.status_code}")    #Revisamos conexión
        print(f"Headers de la consulta: {respuesta.headers}")       #Revisamos metadatos
        print(f"Los campos leídos son: {data.keys()}")              #Revisamos las etiqeutas que leyó
    
    print()
    print(f"Nombre: {data['name']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}\n")
    print(f"Stats ------------------")
    for stat in data['stats']:
     print(f"{stat['stat']['name']}: {stat['base_stat']}")


Impresion = PreguntarImpresion()
nombre_Pokemon = input("Nombre pokemon:  ")
Obtener_Datos_Pokemon(nombre_Pokemon)
input()