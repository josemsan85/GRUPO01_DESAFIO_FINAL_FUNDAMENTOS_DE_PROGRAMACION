Algoritmo MesaDePartesVirtual
	Definir maxExp, totalExp, opcion Como Entero
	Definir respSalida Como Cadena
	Definir guardado Como Logico
	
	maxExp <- 100
	totalExp <- 0
	guardado <- Falso
	
	Dimension codigos[maxExp]
	Dimension dnis[maxExp]
	Dimension nombres[maxExp]
	Dimension asuntos[maxExp]
	Dimension fechas[maxExp]
	Dimension coincidencias[maxExp]
	
	CargarDatosIniciales(codigos, dnis, nombres, asuntos, fechas, totalExp, maxExp)
	
	Escribir "========================================"
	Escribir "   BIENVENIDO A MESA DE PARTES VIRTUAL"
	Escribir "========================================"
	Escribir "Expedientes cargados: ", totalExp
	
	Repetir
		MostrarMenu
		Leer opcion
		
		Segun opcion Hacer
			1:
				RegistrarExpediente(codigos, dnis, nombres, asuntos, fechas, totalExp, maxExp)
			2:
				BuscarPorCodigo(codigos, dnis, nombres, asuntos, fechas, totalExp)
			3:
				OrdenarPorCodigo(codigos, dnis, nombres, asuntos, fechas, totalExp)
			4:
				ListarExpedientes(codigos, dnis, nombres, asuntos, fechas, totalExp)
			5:
				GuardarDatos(codigos, dnis, nombres, asuntos, fechas, totalExp, guardado)
			6:
				BuscarPorCoincidencia(codigos, dnis, nombres, asuntos, fechas, totalExp, coincidencias)
			7:
				OrdenarPorFecha(codigos, dnis, nombres, asuntos, fechas, totalExp)
			0:
				Escribir "Desea guardar los datos antes de salir? (S/N): "
				Leer respSalida
				Si Mayusculas(respSalida) = "S" Entonces
					GuardarDatos(codigos, dnis, nombres, asuntos, fechas, totalExp, guardado)
				FinSi
				Escribir "Saliendo del sistema. Hasta luego."
			De Otro Modo:
				Escribir "Opcion no valida. Intente nuevamente."
		FinSegun
		
		Si opcion <> 0 Entonces
			Escribir ""
			Escribir "Presione ENTER para continuar..."
			Esperar Tecla
		FinSi
	Hasta Que opcion = 0
FinAlgoritmo


SubProceso MostrarMenu
	Escribir ""
	Escribir "----- MENU PRINCIPAL -----"
	Escribir "1. Registrar expediente"
	Escribir "2. Buscar expediente por codigo"
	Escribir "3. Ordenar expedientes por codigo"
	Escribir "4. Listar expedientes"
	Escribir "5. Guardar datos"
	Escribir "6. Buscar por coincidencia"
	Escribir "7. Ordenar expedientes por fecha"
	Escribir "0. Salir"
	Escribir "Elija una opcion: " Sin Saltar
FinSubProceso


SubProceso CargarDatosIniciales(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia, maxExp Por Referencia)
	totalExp <- 2
	codigos[1] <- "EXP-001"
	dnis[1] <- "12345678"
	nombres[1] <- "Juan Perez Lopez"
	asuntos[1] <- "Solicitud de constancia"
	fechas[1] <- "15/09/2026"
	
	codigos[2] <- "EXP-002"
	dnis[2] <- "87654321"
	nombres[2] <- "Maria Quispe Rojas"
	asuntos[2] <- "Mesa de partes recurso"
	fechas[2] <- "02/08/2026"
FinSubProceso


SubProceso RegistrarExpediente(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia, maxExp Por Referencia)
	Definir dniTemp, nomTemp, asuntoTemp, fechaTemp, codGenerado Como Cadena
	Definir valido Como Logico
	
	Escribir ""
	Escribir "--- REGISTRAR EXPEDIENTE ---"
	
	Si totalExp >= maxExp Entonces
		Escribir "Error: Se alcanzo la capacidad maxima de expedientes."
	SiNo
		Repetir
			Escribir "Ingrese DNI (8 digitos): " Sin Saltar
			Leer dniTemp
			valido <- ValidarDNI(dniTemp)
			Si NO valido Entonces
				Escribir "  -> DNI invalido. Debe tener exactamente 8 digitos."
			FinSi
		Hasta Que valido
		
		Repetir
			Escribir "Ingrese Nombres Completos: " Sin Saltar
			Leer nomTemp
			valido <- ValidarTextoMinimo(nomTemp, 3)
			Si NO valido Entonces
				Escribir "  -> Nombre invalido. Ingrese al menos 3 caracteres."
			FinSi
		Hasta Que valido
		
		Repetir
			Escribir "Ingrese Asunto: " Sin Saltar
			Leer asuntoTemp
			valido <- ValidarAsunto(asuntoTemp)
			Si NO valido Entonces
				Escribir "  -> Asunto invalido. Minimo 5 caracteres y sin el simbolo barra."
			FinSi
		Hasta Que valido
		
		Repetir
			Escribir "Ingrese Fecha (DD/MM/AAAA): " Sin Saltar
			Leer fechaTemp
			valido <- ValidarFecha(fechaTemp)
			Si NO valido Entonces
				Escribir "  -> Fecha invalida. Use el formato DD/MM/AAAA (ej. 24/11/2026)."
			FinSi
		Hasta Que valido
		
		totalExp <- totalExp + 1
		codGenerado <- GenerarCodigo(totalExp)
		
		codigos[totalExp] <- codGenerado
		dnis[totalExp] <- dniTemp
		nombres[totalExp] <- nomTemp
		asuntos[totalExp] <- asuntoTemp
		fechas[totalExp] <- fechaTemp
		
		Escribir "Expediente registrado exitosamente con codigo: ", codGenerado
	FinSi
FinSubProceso


Funcion cod <- GenerarCodigo(num)
	Definir cod Como Cadena
	Si num < 10 Entonces
		cod <- Concatenar("EXP-00", ConvertirATexto(num))
	SiNo
		Si num < 100 Entonces
			cod <- Concatenar("EXP-0", ConvertirATexto(num))
		SiNo
			cod <- Concatenar("EXP-", ConvertirATexto(num))
		FinSi
	FinSi
FinFuncion


Funcion ok <- ValidarDNI(dni)
	Definir ok Como Logico
	Definir i Como Entero
	Definir car Como Cadena
	
	Si Longitud(dni) <> 8 Entonces
		ok <- Falso
	SiNo
		ok <- Verdadero
		Para i <- 1 Hasta 8 Hacer
			car <- Subcadena(dni, i, i)
			Si (car < "0") O (car > "9") Entonces
				ok <- Falso
			FinSi
		FinPara
	FinSi
FinFuncion


Funcion ok <- ValidarTextoMinimo(texto, minLen)
	Definir ok Como Logico
	Si Longitud(texto) >= minLen Entonces
		ok <- Verdadero
	SiNo
		ok <- Falso
	FinSi
FinFuncion


Funcion ok <- ValidarAsunto(asunto)
	Definir ok Como Logico
	Definir i Como Entero
	
	Si Longitud(asunto) < 5 Entonces
		ok <- Falso
	SiNo
		ok <- Verdadero
		Para i <- 1 Hasta Longitud(asunto) Hacer
			Si Subcadena(asunto, i, i) = "|" Entonces
				ok <- Falso
			FinSi
		FinPara
	FinSi
FinFuncion


Funcion ok <- ValidarFecha(fecha)
	Definir ok Como Logico
	Definir dia, mes, anio Como Entero
	
	Si Longitud(fecha) <> 10 Entonces
		ok <- Falso
	SiNo
		Si (Subcadena(fecha, 3, 3) <> "/") O (Subcadena(fecha, 6, 6) <> "/") Entonces
			ok <- Falso
		SiNo
			dia <- ConvertirANumero(Subcadena(fecha, 1, 2))
			mes <- ConvertirANumero(Subcadena(fecha, 4, 5))
			anio <- ConvertirANumero(Subcadena(fecha, 7, 10))
			
			Si (dia < 1) O (dia > 31) O (mes < 1) O (mes > 12) O (anio < 1900) O (anio > 2100) Entonces
				ok <- Falso
			SiNo
				ok <- Verdadero
			FinSi
		FinSi
	FinSi
FinFuncion


SubProceso BuscarPorCodigo(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia)
	Definir codBuscado Como Cadena
	Definir i, pos Como Entero
	
	Escribir ""
	Escribir "--- BUSCAR EXPEDIENTE POR CODIGO ---"
	Si totalExp = 0 Entonces
		Escribir "No hay expedientes registrados."
	SiNo
		Escribir "Ingrese codigo a buscar (ej. EXP-001): " Sin Saltar
		Leer codBuscado
		codBuscado <- Mayusculas(codBuscado)
		
		pos <- -1
		Para i <- 1 Hasta totalExp Hacer
			Si Mayusculas(codigos[i]) = codBuscado Entonces
				pos <- i
			FinSi
		FinPara
		
		Si pos = -1 Entonces
			Escribir "No se encontro el expediente con codigo: ", codBuscado
		SiNo
			Escribir "Expediente encontrado:"
			Escribir "  Codigo : ", codigos[pos]
			Escribir "  DNI    : ", dnis[pos]
			Escribir "  Nombre : ", nombres[pos]
			Escribir "  Asunto : ", asuntos[pos]
			Escribir "  Fecha  : ", fechas[pos]
		FinSi
	FinSi
FinSubProceso


SubProceso OrdenarPorCodigo(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia)
	Definir i, j Como Entero
	Definir auxCod, auxDni, auxNom, auxAsu, auxFec Como Cadena
	
	Escribir ""
	Escribir "--- ORDENAR EXPEDIENTES POR CODIGO ---"
	Si totalExp <= 1 Entonces
		Escribir "No hay suficientes expedientes para ordenar."
	SiNo
		Para i <- 1 Hasta totalExp - 1 Hacer
			Para j <- 1 Hasta totalExp - i Hacer
				Si codigos[j] > codigos[j + 1] Entonces
					auxCod <- codigos[j]
					codigos[j] <- codigos[j + 1]
					codigos[j + 1] <- auxCod
					
					auxDni <- dnis[j]
					dnis[j] <- dnis[j + 1]
					dnis[j + 1] <- auxDni
					
					auxNom <- nombres[j]
					nombres[j] <- nombres[j + 1]
					nombres[j + 1] <- auxNom
					
					auxAsu <- asuntos[j]
					asuntos[j] <- asuntos[j + 1]
					asuntos[j + 1] <- auxAsu
					
					auxFec <- fechas[j]
					fechas[j] <- fechas[j + 1]
					fechas[j + 1] <- auxFec
				FinSi
			FinPara
		FinPara
		
		Escribir "Expedientes ordenados por codigo (ascendente)."
	FinSi
FinSubProceso


SubProceso ListarExpedientes(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia)
	Definir i Como Entero
	
	Escribir ""
	Escribir "--- LISTA DE EXPEDIENTES ---"
	Si totalExp = 0 Entonces
		Escribir "No hay expedientes registrados."
	SiNo
		Para i <- 1 Hasta totalExp Hacer
			Escribir i, ". [", codigos[i], "] | DNI: ", dnis[i], " | ", nombres[i], " | Asunto: ", asuntos[i], " | Fecha: ", fechas[i]
		FinPara
		Escribir "Total de expedientes: ", totalExp
	FinSi
FinSubProceso


SubProceso GuardarDatos(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia, guardado Por Referencia)
	Definir i Como Entero
	Escribir ""
	Escribir "--- GUARDAR DATOS ---"
	Para i <- 1 Hasta totalExp Hacer
		Escribir "GUARDADO -> ", codigos[i], "|", dnis[i], "|", nombres[i], "|", asuntos[i], "|", fechas[i]
	FinPara
	guardado <- Verdadero
	Escribir "Datos guardados correctamente (", totalExp, " registro(s))."
FinSubProceso


SubProceso BuscarPorCoincidencia(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia, coincidencias Por Referencia)
	Definir opCampo, i, cantEncontrados, posEnLista Como Entero
	Definir textoBuscar, campoValor Como Cadena
	
	Escribir ""
	Escribir "--- BUSCAR POR COINCIDENCIA ---"
	Si totalExp = 0 Entonces
		Escribir "No hay expedientes registrados."
	SiNo
		Escribir "Buscar en: 1.Codigo  2.DNI  3.Nombre  4.Asunto  5.Fecha"
		Escribir "Elija campo: " Sin Saltar
		Leer opCampo
		
		Si (opCampo < 1) O (opCampo > 5) Entonces
			Escribir "Campo invalido."
		SiNo
			Escribir "Ingrese texto a buscar: " Sin Saltar
			Leer textoBuscar
			textoBuscar <- Minusculas(textoBuscar)
			
			cantEncontrados <- 0
			Para i <- 1 Hasta totalExp Hacer
				Segun opCampo Hacer
					1: campoValor <- Minusculas(codigos[i])
					2: campoValor <- Minusculas(dnis[i])
					3: campoValor <- Minusculas(nombres[i])
					4: campoValor <- Minusculas(asuntos[i])
					5: campoValor <- Minusculas(fechas[i])
				FinSegun
				
				Si ContieneSubcadena(campoValor, textoBuscar) Entonces
					cantEncontrados <- cantEncontrados + 1
					coincidencias[cantEncontrados] <- i
				FinSi
			FinPara
			
			Si cantEncontrados = 0 Entonces
				Escribir "No se encontraron coincidencias."
			SiNo
				Escribir "Coincidencias encontradas: ", cantEncontrados
				Para i <- 1 Hasta cantEncontrados Hacer
					posEnLista <- coincidencias[i]
					Escribir "  [", codigos[posEnLista], "] ", nombres[posEnLista], " - ", asuntos[posEnLista], " (", fechas[posEnLista], ")"
				FinPara
			FinSi
		FinSi
	FinSi
FinSubProceso


Funcion encontrada <- ContieneSubcadena(textoGrande, subTexto)
	Definir encontrada Como Logico
	Definir idx, lonGrande, lonSub Como Entero
	
	lonGrande <- Longitud(textoGrande)
	lonSub <- Longitud(subTexto)
	
	Si lonSub = 0 Entonces
		encontrada <- Verdadero
	SiNo
		Si lonSub > lonGrande Entonces
			encontrada <- Falso
		SiNo
			encontrada <- Falso
			Para idx <- 1 Hasta (lonGrande - lonSub + 1) Hacer
				Si Subcadena(textoGrande, idx, idx + lonSub - 1) = subTexto Entonces
					encontrada <- Verdadero
				FinSi
			FinPara
		FinSi
	FinSi
FinFuncion


Funcion clave <- FechaAOrdenNumero(fecha)
	Definir dia, mes, anio Como Cadena
	dia <- Subcadena(fecha, 1, 2)
	mes <- Subcadena(fecha, 4, 5)
	anio <- Subcadena(fecha, 7, 10)
	clave <- ConvertirANumero(Concatenar(anio, Concatenar(mes, dia)))
FinFuncion


SubProceso OrdenarPorFecha(codigos Por Referencia, dnis Por Referencia, nombres Por Referencia, asuntos Por Referencia, fechas Por Referencia, totalExp Por Referencia)
	Definir i, j Como Entero
	Definir auxCod, auxDni, auxNom, auxAsu, auxFec Como Cadena
	
	Escribir ""
	Escribir "--- ORDENAR EXPEDIENTES POR FECHA ---"
	Si totalExp <= 1 Entonces
		Escribir "No hay suficientes expedientes para ordenar."
	SiNo
		Para i <- 1 Hasta totalExp - 1 Hacer
			Para j <- 1 Hasta totalExp - i Hacer
				Si FechaAOrdenNumero(fechas[j]) > FechaAOrdenNumero(fechas[j + 1]) Entonces
					auxCod <- codigos[j]
					codigos[j] <- codigos[j + 1]
					codigos[j + 1] <- auxCod
					
					auxDni <- dnis[j]
					dnis[j] <- dnis[j + 1]
					dnis[j + 1] <- auxDni
					
					auxNom <- nombres[j]
					nombres[j] <- nombres[j + 1]
					nombres[j + 1] <- auxNom
					
					auxAsu <- asuntos[j]
					asuntos[j] <- asuntos[j + 1]
					asuntos[j + 1] <- auxAsu
					
					auxFec <- fechas[j]
					fechas[j] <- fechas[j + 1]
					fechas[j + 1] <- auxFec
				FinSi
			FinPara
		FinPara
		
		Escribir "Expedientes ordenados por fecha (del mas antiguo al mas reciente)."
	FinSi
FinSubProceso