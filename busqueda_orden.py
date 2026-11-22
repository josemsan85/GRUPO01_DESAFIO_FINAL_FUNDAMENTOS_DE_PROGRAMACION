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


if __name__ == "__main__":
    codigos = ["EXP-002", "EXP-001"]
    dnis = ["87654321", "12345678"]
    nombres = ["Luis Rojas", "Ana Perez"]
    asuntos = ["Reclamo", "Solicitud"]
    fechas = ["11/10/2026", "10/10/2026"]
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    print("Ordenado:", codigos)
    print("Buscar EXP-001:", buscar_por_codigo(codigos, "EXP-001"))

    fechas_prueba = ["05/10/2026", "20/09/2026", "28/09/2026"]
    print("Mes 09/2026:", buscar_coincidencias(fechas_prueba, "09/2026"))