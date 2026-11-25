# Busca un codigo exacto y devuelve su posicion o -1 si no esta
def buscar_por_codigo(codigos, codigo):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i
    return -1


# Cambia de lugar dos elementos usando una variable auxiliar
def intercambiar(lista, pos1, pos2):
    aux = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = aux


# Ordena por codigo con burbuja y mueve todas las listas juntas
def ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas):
    n = len(codigos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if codigos[j] > codigos[j + 1]:
                intercambiar(codigos, j, j + 1)
                intercambiar(dnis, j, j + 1)
                intercambiar(nombres, j, j + 1)
                intercambiar(asuntos, j, j + 1)
                intercambiar(fechas, j, j + 1)


# Busca coincidencias sin importar mayusculas y devuelve las posiciones
def buscar_coincidencias(lista, texto):
    posiciones = []
    if texto.strip() == "":
        return posiciones
    for i in range(len(lista)):
        if texto.lower() in lista[i].lower():
            posiciones.append(i)
    return posiciones


# Convierte DD/MM/AAAA en AAAAMMDD para poder comparar fechas
def convertir_fecha(fecha):
    return fecha[6:10] + fecha[3:5] + fecha[0:2]


# Ordena por fecha (la mas antigua primero) con burbuja y mueve todas las listas juntas
def ordenar_por_fecha(codigos, dnis, nombres, asuntos, fechas):
    n = len(fechas)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if convertir_fecha(fechas[j]) > convertir_fecha(fechas[j + 1]):
                intercambiar(codigos, j, j + 1)
                intercambiar(dnis, j, j + 1)
                intercambiar(nombres, j, j + 1)
                intercambiar(asuntos, j, j + 1)
                intercambiar(fechas, j, j + 1)


if __name__ == "__main__":
    # Prueba 1: ordenar por codigo y buscar por codigo
    codigos = ["EXP-002", "EXP-001"]
    dnis = ["87654321", "12345678"]
    nombres = ["Luis Rojas", "Ana Perez"]
    asuntos = ["Reclamo", "Solicitud"]
    fechas = ["11/10/2026", "10/10/2026"]
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    print("Ordenado:", codigos)
    print("Buscar EXP-001:", buscar_por_codigo(codigos, "EXP-001"))
    print("Buscar EXP-009:", buscar_por_codigo(codigos, "EXP-009"))

    # Prueba 2: busqueda por coincidencia (mes, sin resultados, texto vacio)
    fechas_prueba = ["05/10/2026", "20/09/2026", "28/09/2026"]
    print("Mes 09/2026:", buscar_coincidencias(fechas_prueba, "09/2026"))
    print("Fecha 01/01/2000:", buscar_coincidencias(fechas_prueba, "01/01/2000"))
    print("Texto vacio:", buscar_coincidencias(fechas_prueba, ""))

    # Prueba 3: ordenar por fecha (el dia no debe pesar mas que el mes o el anio)
    print("Fecha convertida:", convertir_fecha("05/10/2026"))
    codigos = ["EXP-001", "EXP-002", "EXP-003", "EXP-004"]
    dnis = ["11111111", "22222222", "33333333", "44444444"]
    nombres = ["Ana", "Beto", "Carla", "Dora"]
    asuntos = ["A", "B", "C", "D"]
    fechas = ["05/10/2026", "20/09/2026", "01/01/2027", "28/09/2025"]
    ordenar_por_fecha(codigos, dnis, nombres, asuntos, fechas)
    print("Por fecha:", fechas)
    print("Codigos alineados:", codigos)

    # Prueba 4: casos limite (lista vacia y un solo elemento)
    print("Buscar en lista vacia:", buscar_por_codigo([], "EXP-001"))
    uno = ["EXP-001"]
    ordenar_por_codigo(uno, ["1"], ["A"], ["B"], ["C"])
    print("Un solo elemento:", uno)