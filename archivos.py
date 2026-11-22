import os
def guardar_datos(ruta, codigos, dnis, nombres, asuntos, fechas):
    carpeta = os.path.dirname(ruta)
    if carpeta != "" and not os.path.exists(carpeta):
        os.makedirs(carpeta)

    with open(ruta, "w", encoding="utf-8") as archivo:
        for i in range(len(codigos)):
            archivo.write(codigos[i] + "|" + dnis[i] + "|" + nombres[i]
                          + "|" + asuntos[i] + "|" + fechas[i] + "\n")
def cargar_datos(ruta):
    codigos = []
    dnis = []
    nombres = []
    asuntos = []
    fechas = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split("|")
                if len(partes) != 5:
                    continue  # linea mal formada: la saltamos
                codigos.append(partes[0])
                dnis.append(partes[1])
                nombres.append(partes[2])
                asuntos.append(partes[3])
                fechas.append(partes[4])
    except FileNotFoundError:
        pass  # no hay archivo todavia: se devuelven las listas vacias
    return codigos, dnis, nombres, asuntos, fechas
if __name__ == "__main__":
    # Prueba rapida de este modulo (python archivos.py)
    ruta_prueba = "datos/prueba.txt"
    guardar_datos(ruta_prueba, ["EXP-001"], ["12345678"], ["Ana Perez"],
                  ["Solicitud"], ["10/10/2026"])
    print(cargar_datos(ruta_prueba))