def buscar_por_codigo(codigos, codigo):
    """Busqueda lineal: revisa la lista posicion por posicion.

    Devuelve la posicion donde esta el codigo, o -1 si no existe.
    Sirve aunque la lista este desordenada.
    """
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i          # lo encontramos: devolvemos su posicion
    return -1                 # termino el recorrido y no estaba


def intercambiar(lista, pos1, pos2):
    """Intercambia dos elementos de una lista (usa una variable auxiliar)."""
    aux = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = aux


def ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas):
    """Ordena los expedientes por codigo (de menor a mayor) con burbuja.

    Cada vez que se intercambian dos codigos, se intercambian tambien
    las mismas posiciones en las otras 4 listas, para que los datos de
    un expediente no se desalineen.
    Modifica las listas directamente (no devuelve nada).
    """
    n = len(codigos)
    for i in range(n - 1):              # numero de pasadas
        for j in range(n - 1 - i):      # compara pares vecinos
            if codigos[j] > codigos[j + 1]:
                intercambiar(codigos, j, j + 1)
                intercambiar(dnis, j, j + 1)
                intercambiar(nombres, j, j + 1)
                intercambiar(asuntos, j, j + 1)
                intercambiar(fechas, j, j + 1)


if __name__ == "__main__":
    # Prueba 1: lista desordenada (la del ejemplo original)
    codigos = ["EXP-002", "EXP-001"]
    dnis = ["87654321", "12345678"]
    nombres = ["Luis Rojas", "Ana Perez"]
    asuntos = ["Reclamo", "Solicitud"]
    fechas = ["11/10/2026", "10/10/2026"]
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    print("Ordenado:", codigos)
    print("Los datos siguen alineados:", nombres, dnis)
    print("Buscar EXP-001:", buscar_por_codigo(codigos, "EXP-001"))   # 0
    print("Buscar EXP-009:", buscar_por_codigo(codigos, "EXP-009"))   # -1

    # Prueba 2: lista con 4 expedientes en desorden
    codigos = ["EXP-004", "EXP-002", "EXP-003", "EXP-001"]
    dnis = ["44444444", "22222222", "33333333", "11111111"]
    nombres = ["Dora", "Beto", "Carla", "Ana"]
    asuntos = ["Asunto D", "Asunto B", "Asunto C", "Asunto A"]
    fechas = ["04/10/2026", "02/10/2026", "03/10/2026", "01/10/2026"]
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    print("Ordenado:", codigos)
    print("Nombres:", nombres)

    # Prueba 3: casos limite (lista vacia y lista con 1 elemento)
    ordenar_por_codigo([], [], [], [], [])
    print("Buscar en lista vacia:", buscar_por_codigo([], "EXP-001"))  # -1
    uno = ["EXP-001"]
    ordenar_por_codigo(uno, ["1"], ["A"], ["B"], ["C"])
    print("Un solo elemento:", uno)