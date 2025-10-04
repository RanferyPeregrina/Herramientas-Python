Sub CambiarFuenteAlAzarLetraPorLetra()
    Randomize ' Establecer una semilla para la función Rnd
    
    Dim caracter As Range
    Dim simbolos As String
    Dim fuentesSimbolos() As Variant
    Dim fuenteElegida As String
    
    ' Definir los símbolos y las fuentes correspondientes
    simbolos = "# $ % & ( ) * + - / 0 1 2 3 4 5 6 7 8 9 < = > @ [ ] ^ _ ` { } ~"
    fuentesSimbolos = Array("Simbolos1", "Simbolos2", "Simbolos3")
    
    For Each caracter In ActiveDocument.Range.Characters
        ' Verificar si el caracter es un símbolo
        If InStr(simbolos, caracter.Text) > 0 Then
            ' Elegir al azar una fuente de la lista
            fuenteElegida = fuentesSimbolos(Int((UBound(fuentesSimbolos) + 1) * Rnd))
            
            ' Aplicar la fuente al caracter
            caracter.Font.Name = fuenteElegida
        End If
    Next caracter
End Sub
