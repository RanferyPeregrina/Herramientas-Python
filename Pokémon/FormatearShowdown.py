def EscribirAtaques(RenglonLeido):

    # Que compruebe si el renglón está vacío.
    if RenglonLeido == "":
        pass
    print("Esto se lee creo")



print("\n" * 5)
print("Ingresa a continuación el texto que quieres formatear.")
print("Linea por línea.")


while True:
    RenglonLeido = input()

    if RenglonLeido == "": break

    if "Nature" in RenglonLeido:
        TextoGrande = "- ".join(EscribirAtaques(RenglonLeido))
    else:
        TextoGrande = "\n".join(RenglonLeido)
print("\n" * 2)
print("Al final el texto leído es:")
print(TextoGrande)