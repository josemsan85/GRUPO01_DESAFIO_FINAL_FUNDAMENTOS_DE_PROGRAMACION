def guardar_datos(ruta, codigos, dnis, nombres, asuntos, fechas):
    # TODO (YNUMA): escribir un expediente por linea, separado por "|"
    # Ej: EXP-001|12345678|Ana Perez|Solicitud|10/10/2026
    pass


def cargar_datos(ruta):
    # TODO (YNUMA): leer el archivo y devolver las 5 listas en este orden:
    # codigos, dnis, nombres, asuntos, fechas
    # Si el archivo no existe, devolver 5 listas vacias (try/except).
    return [], [], [], [], []


if __name__ == "__main__":
    ruta = "datos/prueba.txt"
    guardar_datos(ruta, ["EXP-001"], ["12345678"], ["Ana Perez"],
                  ["Solicitud"], ["10/10/2026"])
    print(cargar_datos(ruta))
