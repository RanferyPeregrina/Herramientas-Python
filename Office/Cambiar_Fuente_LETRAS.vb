Sub CambiarFuenteAlAzar()
    Randomize ' Establecer una semilla para la función Rnd
    
    Dim palabra As Range
    Dim fuentes() As Variant
    Dim fuenteElegida As String
    
    ' Definir las fuentes disponibles
    fuentes = Array("Fuentenormal1", "Fuentenormal2", "Fuentenormal3", "Fuentenormal4", "Fuentenormal5")
    
    For Each palabra In ActiveDocument.Words
        ' Elegir al azar una fuente de la lista
        fuenteElegida = fuentes(Int((UBound(fuentes) + 1) * Rnd))
        
        ' Aplicar la fuente a la palabra
        palabra.Font.Name = fuenteElegida
    Next palabra
End Sub
