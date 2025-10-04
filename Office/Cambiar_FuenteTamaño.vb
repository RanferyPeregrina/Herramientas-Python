'Para usarlo, abre el Word donde lo vas a aplicar, presiona Alt F11
'Y como nuevo módulo, escribes esto:

Sub CambiarTamañoFuente11a12()
    Dim rng As Range
    
    ' Recorre todo el documento
    For Each rng In ActiveDocument.StoryRanges
        ' Busca en cada rango de texto
        Do
            ' Si el tamaño de la fuente es 11, lo cambia a 12
            If rng.Font.Size = 11 Then
                rng.Font.Size = 12
            End If
            
            ' Avanza al siguiente rango de texto
            Set rng = rng.NextStoryRange
        Loop Until rng Is Nothing
    Next rng
    
    MsgBox "¡Tamaño de fuente cambiado exitosamente!", vbInformation
End Sub

'Cierra el Editor de VBA.
'En Word, presiona Alt + F8 para abrir el cuadro de diálogo "Macro".
'Selecciona "CambiarFuenteTimesNewRomanACalibri" en la lista de macros y haz clic en "Ejecutar".