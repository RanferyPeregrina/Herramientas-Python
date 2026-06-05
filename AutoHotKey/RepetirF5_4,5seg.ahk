; Variable para controlar el estado
ModoRepetir := False

; Tecla J para activar/desactivar el modo
j::
    ModoRepetir := !ModoRepetir  ; Alterna entre True/False
    if (ModoRepetir) {
        ; Inicia el timer para repetir F5 cada 5 segundos
        SetTimer, EnviarF5, 6800
        SoundBeep, 1000, 200  ; Beep de confirmación (opcional)
        ToolTip, Modo Repetir ACTIVADO - Presiona J para desactivar
        Sleep, 1000
        ToolTip
    } else {
        ; Detiene el timer
        SetTimer, EnviarF5, Off
        SoundBeep, 500, 200  ; Beep diferente para desactivado
        ToolTip, Modo Repetir DESACTIVADO
        Sleep, 1000
        ToolTip
    }
return

EnviarF5:
    Send, {F5}
return