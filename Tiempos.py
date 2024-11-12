from pynput import keyboard as keyboard
import time


print("= " * 50)
print("Programa para medir tiempos (Intervalos)")
print("1.- Contador de tiempo en pulsos")
print("2.- Contador de tiempo en presiones")
Eleccion = int(input("\nElección:  "))
print("= " * 50)


if Eleccion == 1:
    ListaTiemposNotas = []
    i = 0
    input("Presione ENTER para empezar a contar.")
    while(True):
        i += 1

        print("= "* 20)
        Inicio = time.time()
        R = input("Presione ENTER para detener (Escriba algo para pausar)")
        Fin = time.time()

        if len(R) != 0:
            break
        

        TiempoTranscurrido = Fin - Inicio
        ListaTiemposNotas.append(TiempoTranscurrido)
        print(f"El tiempo transcurrido fue: {TiempoTranscurrido}")

if Eleccion == 2:

    # Variables globales para almacenar los tiempos
    inicio = None  # Se almacenará el tiempo cuando la tecla es presionada

    def on_press(tecla):
        global inicio
        inicio = time.time()  # Capturamos el tiempo actual al presionar la tecla
        print(f"Tecla presionada: {tecla}")

    def on_release(tecla):
        if inicio is not None:  # Solo si hay un valor válido en `inicio`
            final = time.time()  # Capturamos el tiempo actual al soltar la tecla
            tiempo_presionado = final - inicio
            print(f"Tecla liberada: {tecla}. Tiempo presionada: {tiempo_presionado:.3f} segundos")
        
        # Si presionas "Esc", el programa se detiene
        if tecla == keyboard.Key.esc:
            return False

    # Listener que escucha cuando se presiona o libera una tecla
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

print("\n =============================================")
print("¿Imprimir lista de tiempos?")
print("1.- Sí")
print("2.- No")
Impresion = int(input("Respuesta:  "))

if Impresion == 1:
    Indice = 1
    for i in ListaTiemposNotas:
        print(f"Nota {Indice}: {int(round(i, 3) * 1000)} milisegundos")
        Indice += 1
elif Impresion == 2:
    print("Programa terminado")