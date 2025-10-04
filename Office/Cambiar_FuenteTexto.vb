'Este programa es para cambiar el tipo de letra a otro
'En este caso, el tipo de letra "Times New Roman" a "Calibri"
'Para usarlo, abre el Word donde lo vas a aplicar, presiona Alt F11
'Y como nuevo módulo, escribes esto:

Sub CambiarFuenteTimesNewRomanACalibri()
    Dim rng As Range
    Set rng = ActiveDocument.Content
    
    ' Buscar todas las palabras con la fuente "Times New Roman" y cambiarlas a "Calibri"
    With rng.Find
        .ClearFormatting
        .Font.Name = "Times New Roman"
        .Replacement.ClearFormatting
        .Replacement.Font.Name = "Calibri"
        .Text = ""
        .Replacement.Text = ""
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
        .Execute Replace:=wdReplaceAll
    End With
End Sub

'Cierra el Editor de VBA.
'En Word, presiona Alt + F8 para abrir el cuadro de diálogo "Macro".
'Selecciona "CambiarFuenteTimesNewRomanACalibri" en la lista de macros y haz clic en "Ejecutar".