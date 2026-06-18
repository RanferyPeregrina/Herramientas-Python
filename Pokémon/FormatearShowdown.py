print("\n" * 5)
print("Ingresa a continuación el texto que quieres formatear.")
print("Linea por línea.")


while True:
    RenglonLeido = input()

    if RenglonLeido == "": break

    if "Nature" in RenglonLeido:
        print("ENCONTRÉ LA NATURALEZA!!!")
    else:
        print("Todo bien...")
print("\n" * 5)