import random
import time



while True:
    print("¿Quieres imprimir cada parte del proceso?")
    print("1.- Sí")
    print("2.- No")
    Impresion = int(input("Respuesta:  "))
    if Impresion == 1:
        Impresion = True
        break
    elif Impresion == 2:
        Impresion = False
        break
    else:
        print("Ingreso no válido.")

def CambiarTurno(Turno):
    print()
    if Turno == 1:
        print("TURNO DEL BOT ----------------------")
        Turno = 0
    elif Turno == 0:
        print(f"***TURNO DE {Nombre} ----------------------")
        Turno = 1
    else:
        print(f"Error con los turnos... no puede ser turno {Turno}")
    return Turno

def ElegirOpcion(Decision, Balas):
    print("1.- Disparar")
    print("2.- Pasar arma")
    print("3.- Agregar bala")
    print("4.- Quitar bala")
    print("5.- Girar tambor")
    if Decision == 0:
        Opcion_Elegida = int(input("   Respuesta:  "))
    else: 
        Opcion_Elegida = Decision
        time.sleep(2)
        print()
        print(f"El bot eligió la opción: {Decision}")

    if Opcion_Elegida == 1:
        print("*¡Click!*")
        time.sleep(1)
        if Disparar(EspaciosConBala) == True:
            
            if Turno == 1: print("Haz muerto...")
            elif Turno == 0: print("Vaya, ganaste.")

            Continuar = False
        else: Continuar = True
    elif Opcion_Elegida == 2:
        print("Se eligió pasar el arma.")
        if Turno == 1: print("La cedes.")
        elif Turno == 0: print("Te la entrega.")
        Continuar = True
    elif Opcion_Elegida == 3:
        Balas = Balas + 1
        Continuar = True
    elif Opcion_Elegida == 4:
        Continuar = True
    elif Opcion_Elegida == 5:
        GirarTambor()
        Continuar = True
    return Continuar

def GirarTambor(Cantidad_Giros, Cantidad_Balas):
    
    for Giro in range(Cantidad_Giros):
        EspacioConBala = []
        if Impresion == True:
            print()
            print(f"Giro {Giro + 1}...")

        for i in range (Cantidad_Balas):
            while True:
                # print(f"Lista con: {EspacioConBala}")
                Espacio_Generado = (random.randint(1,6))
                # print(f"Se está intentando agregar ahora el valor: {Espacio_Generado}")
                if Espacio_Generado in EspacioConBala:
                    Placeholder = "Esta línea no hace nada."        
                else:
                    # print("Este número aún no está...")
                    EspacioConBala.append(Espacio_Generado)
                    break
        if Impresion == True:
            print(f"La bala quedó en el espacio: {EspacioConBala}")

    return EspacioConBala

def Disparar(EspaciosConBala):

    Disparo = random.randint(1,6)

    if Disparo in EspaciosConBala:
        print("¡SE DISPARÓ!")
        if Impresion == True:
            print(f"El disparo estaba en el espacio: {EspaciosConBala}, y la bala cayó en el: {Disparo}")
        return True
    elif Disparo not in EspaciosConBala:
        print("Todo a salvo.")
        if Impresion == True:
            print(f"El disparo salió a: {Disparo} y la bala estaba en el espacio: {EspaciosConBala}")
        return False
    print("="*50)


Giros = 1
Balas = 1
Turno = 0

Nombre = input("Ingresa tu nombre:  ")

#Preguntar por las balas iniciales
while True:
    Balas_Preguntar = int(input("Con cuántas balas quiere iniciar (1 - 6):  "))
    if Balas_Preguntar <= 6:
        Balas = Balas_Preguntar
        break

EspaciosConBala = []
EspaciosConBala = GirarTambor(Giros, Balas) #Primero cantidad de giros, después cantidad de balas

while True:
    Turno = CambiarTurno(Turno)
    if Turno == 1:
        Continuar = ElegirOpcion(0, Balas)
    elif Turno == 0:
        Continuar = ElegirOpcion(random.randint(1,2), Balas)
    if Continuar == True:
        continue
    else: 
        break;
    

    
