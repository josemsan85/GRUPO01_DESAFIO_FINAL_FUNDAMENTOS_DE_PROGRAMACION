Algoritmo prueba_busqueda
    Definir codigos Como Caracter
    Definir p Como Entero
    Dimension codigos[3]
    codigos[1] <- "EXP-001"
    codigos[2] <- "EXP-002"
    codigos[3] <- "EXP-003"
	
    p <- buscar_por_codigo(codigos, "EXP-002", 3)
    Escribir "Posicion de EXP-002: ", p
    p <- buscar_por_codigo(codigos, "EXP-009", 3)
    Escribir "Posicion de EXP-009: ", p
FinAlgoritmo

Funcion pos <- buscar_por_codigo(codigos, codigo, n)
    Definir i, pos Como Entero
    pos <- -1
    i <- 1
    Mientras i <= n Y pos = -1 Hacer
        Si codigos[i] = codigo Entonces
            pos <- i
        FinSi
        i <- i + 1
    FinMientras
FinFuncion