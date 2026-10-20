Algoritmo registro_expediente
    Definir codigos, dnis, nombres, asuntos, fechas Como Caracter
    Definir dni, nombre, asunto, fecha, codigo Como Caracter
    Definir n Como Entero
    Dimension codigos[100], dnis[100], nombres[100], asuntos[100], fechas[100]
    n <- 0
	
    Repetir
        Escribir "DNI (8 digitos): "
        Leer dni
    Hasta Que validar_dni(dni)
	
    Repetir
        Escribir "Nombre completo: "
        Leer nombre
    Hasta Que Longitud(nombre) >= 3
	
    Repetir
        Escribir "Asunto: "
        Leer asunto
    Hasta Que Longitud(asunto) >= 5
	
    Repetir
        Escribir "Fecha (DD/MM/AAAA): "
        Leer fecha
    Hasta Que Longitud(fecha) = 10
	
    codigo <- generar_codigo(codigos, n)
    n <- n + 1
    codigos[n] <- codigo
    dnis[n] <- dni
    nombres[n] <- nombre
    asuntos[n] <- asunto
    fechas[n] <- fecha
	
    Escribir "Expediente registrado con codigo: ", codigo
FinAlgoritmo

Funcion ok <- validar_dni(dni)
    Definir ok Como Logico
    Definir k Como Entero
    Si Longitud(dni) = 8 Entonces
        ok <- Verdadero
    SiNo
        ok <- Falso
    FinSi
    Para k <- 1 Hasta Longitud(dni) Con Paso 1 Hacer
        Si Subcadena(dni, k, k) < "0" O Subcadena(dni, k, k) > "9" Entonces
            ok <- Falso
        FinSi
    FinPara
FinFuncion

Funcion nuevo <- generar_codigo(codigos, n)
    Definir nuevo, texto Como Caracter
    Definir mayor, numero, i Como Entero
    mayor <- 0
    Para i <- 1 Hasta n Con Paso 1 Hacer
        numero <- ConvertirANumero(Subcadena(codigos[i], 5, 7))
        Si numero > mayor Entonces
            mayor <- numero
        FinSi
    FinPara
    texto <- ConvertirATexto(mayor + 1)
    Si mayor + 1 < 10 Entonces
        texto <- Concatenar("00", texto)
    SiNo
        Si mayor + 1 < 100 Entonces
            texto <- Concatenar("0", texto)
        FinSi
    FinSi
    nuevo <- Concatenar("EXP-", texto)
FinFuncion