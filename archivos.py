import os
def guardar_datos(ruta, codigos, dnis, nombres, asuntos, fechas):
    # crea la carpeta (ej. "datos") si no existe
    carpeta = os.path.dirname(ruta)
    if carpeta != "" and not os.path.exists(carpeta):
        os.makedirs(carpeta)
    with open (ruta, "w", encoding="utf-8") as archivo:
        for i in range(0, len (fechas)):
            archivo.write(codigos[i] + "|" + dnis[i] + "|" + nombres[i] + "|" + asuntos[i] + "|" + fechas[i] + "\n")
def cargar_datos(ruta):
    # devuelve las 5 listas en este orden:
    # codigos, dnis, nombres, asuntos, fechas
    codigos = []
    dnis = []
    nombres = []
    asuntos = []
    fechas = []
    try:
        with open (ruta, "r", encoding="utf-8") as archivo:

            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split("|")
                if len(partes) != 5:
                    continue   # ignora lineas mal formadas
                codigos.append(partes[0])
                dnis.append(partes[1])
                nombres.append(partes[2])
                asuntos.append(partes[3])
                fechas.append(partes[4])
    except FileNotFoundError:
        pass   # primera vez: no existe el archivo, se devuelven listas vacias
    return codigos, dnis, nombres, asuntos, fechas
if __name__ == "__main__":
    from Datos_Prueba import codigos, dnis, nombres, asuntos, fechas

    ruta = "datos/prueba.txt"
    guardar_datos(ruta, codigos, dnis, nombres, asuntos, fechas)
    print (cargar_datos(ruta))