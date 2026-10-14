def buscar_por_codigo(codigos, codigo):
    # TODO (FRANK): busqueda lineal (o binaria si la lista esta ordenada)
    # Devuelve la posicion del codigo en la lista, o -1 si no existe.
    return -1
def ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas):
    # TODO (FRANK): burbuja, seleccion o insercion.
    # Al intercambiar posiciones en 'codigos', intercambiar tambien
    # en las otras 4 listas para no desalinear los datos.
    # Modifica las listas directamente (no devuelve nada). RESALTO EL NO DEVEULVE NADA PORQUE TE CONOZCO
    pass
if __name__ == "__main__":
    codigos = ["EXP-002", "EXP-001"]
    dnis = ["87654321", "12345678"]
    nombres = ["Luis Rojas", "Ana Perez"]
    asuntos = ["Reclamo", "Solicitud"]
    fechas = ["11/10/2026", "10/10/2026"]
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    print("Ordenado:", codigos)
    print("Buscar EXP-001:", buscar_por_codigo(codigos, "EXP-001"))
