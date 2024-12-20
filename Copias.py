CantidadMayoreo = 10
Precio_BlancoNegro = 1
Precio_Color = 4

HojasColor = int(input("Cantidad de hojas a color:  "))
HojasBlancoNegro = int(input("Cantidad de hojasen Blanco  Negro:  "))

if HojasBlancoNegro > CantidadMayoreo:
    Precio_BlancoNegro = 0.4

Precio = (Precio_BlancoNegro * HojasBlancoNegro) + (Precio_Color * HojasColor)

print(f"Se cobran:  {Precio}")