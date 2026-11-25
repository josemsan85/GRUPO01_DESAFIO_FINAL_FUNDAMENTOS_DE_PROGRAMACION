import os


def guardar_datos(ruta, codigos, dnis, nombres, asuntos, fechas, estados):
    """Guarda un expediente por linea, separado por "|".

    Ejemplo: EXP-001|12345678|Ana Perez|Solicitud|10/10/2026|Pendiente

    HU-07: usa try-except para que un error al guardar no cierre el programa.
    Devuelve True si se guardo bien y False si hubo un error.
    """
    try:
        # Si la carpeta (por ejemplo "datos") no existe, la creamos
        carpeta = os.path.dirname(ruta)
        if carpeta != "" and not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # "with" cierra el archivo solo cuando terminamos de escribir
        with open(ruta, "w", encoding="utf-8") as archivo:
            for i in range(len(codigos)):
                linea = (f"{codigos[i]}|{dnis[i]}|{nombres[i]}|"
                         f"{asuntos[i]}|{fechas[i]}|{estados[i]}")
                archivo.write(linea + "\n")
        return True
    except FileNotFoundError:
        print("Error: no se encontro la ruta del archivo:", ruta)
    except IOError as error:
        print("Error al guardar el archivo:", error)
    return False


def cargar_datos(ruta):
    """Lee el archivo y devuelve las 6 listas en este orden:
    codigos, dnis, nombres, asuntos, fechas, estados

    HU-07: usa try-except para que un error al leer no cierre el programa.
    - Si el archivo no existe (primera vez), devuelve las listas vacias.
    - Si una linea esta mal escrita, la omite y avisa.
    - Si una linea es del formato viejo (5 datos, sin estado), le pone "Pendiente".
    """
    codigos, dnis, nombres, asuntos, fechas, estados = [], [], [], [], [], []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue                      # salta lineas vacias
                partes = linea.split("|")
                if len(partes) == 5:              # archivo viejo, sin estado
                    partes.append("Pendiente")
                if len(partes) != 6:              # cada linea debe tener 6 datos
                    print("Aviso: se omitio una linea mal escrita:", linea)
                    continue
                codigos.append(partes[0])
                dnis.append(partes[1])
                nombres.append(partes[2])
                asuntos.append(partes[3])
                fechas.append(partes[4])
                estados.append(partes[5])
    except FileNotFoundError:
        pass    # todavia no hay archivo: se empieza con todo vacio
    except UnicodeDecodeError:
        print("Error: el archivo tiene caracteres que no se pueden leer.")
    except IOError as error:
        print("Error al leer el archivo:", error)
    return codigos, dnis, nombres, asuntos, fechas, estados


if __name__ == "__main__":
    # Prueba rapida de este archivo (python archivos.py)
    ruta = "datos/prueba.txt"
    guardar_datos(ruta, ["EXP-001"], ["12345678"], ["Ana Perez"],
                  ["Solicitud"], ["10/10/2026"], ["Pendiente"])
    print(cargar_datos(ruta))
    print(cargar_datos("datos/no_existe.txt"))   # listas vacias, sin error
