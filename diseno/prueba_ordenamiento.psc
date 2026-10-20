Algoritmo prueba_ordenamiento
    Definir codigos, dnis, nombres, asuntos, fechas Como Caracter
    Dimension codigos[3], dnis[3], nombres[3], asuntos[3], fechas[3]
	
    codigos[1] <- "EXP-003"
    codigos[2] <- "EXP-001"
    codigos[3] <- "EXP-002"
    nombres[1] <- "Carla"
    nombres[2] <- "Ana"
    nombres[3] <- "Beto"
    dnis[1] <- "33333333"
    dnis[2] <- "11111111"
    dnis[3] <- "22222222"
    asuntos[1] <- "Asunto C"
    asuntos[2] <- "Asunto A"
    asuntos[3] <- "Asunto B"
    fechas[1] <- "03/10/2026"
    fechas[2] <- "01/10/2026"
    fechas[3] <- "02/10/2026"
	
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas, 3)
	
    Para k <- 1 Hasta 3 Con Paso 1 Hacer
        Escribir codigos[k], " - ", nombres[k], " - ", dnis[k]
    FinPara
FinAlgoritmo

SubProceso intercambiar(lista, pos1, pos2)
    Definir aux Como Caracter
    aux <- lista[pos1]
    lista[pos1] <- lista[pos2]
    lista[pos2] <- aux
FinSubProceso

SubProceso ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas, n)
    Definir i, j Como Entero
    Para i <- 1 Hasta n-1 Con Paso 1 Hacer
        Para j <- 1 Hasta n-i Con Paso 1 Hacer
            Si codigos[j] > codigos[j+1] Entonces
                intercambiar(codigos, j, j+1)
                intercambiar(dnis, j, j+1)
                intercambiar(nombres, j, j+1)
                intercambiar(asuntos, j, j+1)
                intercambiar(fechas, j, j+1)
            FinSi
        FinPara
    FinPara
FinSubProceso