import itertools
import string
import time

# Definir la contraseña objetivo
target_password = "V4ni11a[h|stoso73"

# Crear una lista de caracteres que podrían usarse en la contraseña
characters = string.ascii_letters + string.digits + string.punctuation  # letras minúsculas, mayúsculas y dígitos

# Medir el tiempo de inicio
start_time = time.time()

# Función para intentar adivinar la contraseña carácter por carácter
def brute_force_password(target):
    guessed_password = [''] * len(target)  # Arreglo para construir la contraseña adivinada
    for i in range(len(target)):
        for char in characters:
            attempt_password = ''.join(guessed_password[:i]) + char + ''.join(guessed_password[i+1:])
            print("Intento:", attempt_password)
            # Comparar el carácter en la posición actual
            if char == target[i]:
                guessed_password[i] = char
                break  # Pasar al siguiente carácter
    return ''.join(guessed_password)

# Llamar a la función
found_password = brute_force_password(target_password)

# Medir el tiempo de finalización
end_time = time.time()

if found_password == target_password:
    print("\n¡Contraseña encontrada!: ", found_password)
else:
    print("\nContraseña no encontrada.")

print("Tiempo total: {:.2f} segundos".format(end_time - start_time))
