#SingleInstance, Force
SendMode Input


; Bucle de muchas veces para presionar "Q"
PgUp::
    Loop 142
    {
        Send, {q down} ; Presiona la tecla "E"
        Sleep, 2       ; Durante 2 Milisegundos
        Send, {q up}   ; Y suelta
        
        ; Genera un número aleatorio entre 1 y 2 milisegundos
        Random, sleepTime, 1, 2
        Sleep, sleepTime ; Pausa por el tiempo aleatorio generado
    }
Return

;Bucle para presionar pero sólo unas 20 veces
PgDn::
    Loop 50
    {
        Send, {q down}
        Sleep, 2
        Send, {q up}

        Sleep, 1
    }
Return