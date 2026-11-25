import os
import random
CANTIDAD = 20
lista_nombres = ["Juan Carlos", "Maria Alejandra", "Luis Alberto", "Ana Sofia",
                 "Carlos Enrique", "Rosa Elena", "Jorge Luis", "Lucia Beatriz",
                 "Miguel Angel", "Carmen Rosa"]

lista_ape_paterno = ["Perez", "Quispe", "Sanchez", "Huaman", "Ramos",
                     "Flores", "Castillo", "Vargas", "Romero", "Diaz"]

lista_asuntos = ["Solicitud de constancia de estudios", "Reclamo por cobro indebido",
                 "Solicitud de licencia", "Pedido de copia certificada",
                 "Reclamo por demora en tramite", "Solicitud de reincorporacion",
                 "Pedido de informacion publica", "Solicitud de beca",
                 "Rectificacion de datos personales", "Solicitud de convalidacion"]

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(CARPETA, "datos", "expedientes.txt")
def generar_dni():
    """Devuelve un DNI ficticio de 8 digitos."""
    return str(random.randint(10000000, 79999999))
def generar_fecha():
    """Devuelve una fecha valida entre agosto y octubre de 2026 (DD/MM/AAAA)."""
    dia = random.randint(1, 28)
    mes = random.randint(8, 10)
    return str(dia).zfill(2) + "/" + str(mes).zfill(2) + "/2026"
def generar_datos():
    """Crea las 6 listas con CANTIDAD expedientes ficticios."""
    codigos = []
    dnis = []
    nombres = []
    asuntos = []
    fechas = []
    estados = []
    # Los numeros de codigo salen desordenados a proposito,
    # asi en la demo se nota la opcion "Ordenar por codigo".
    numeros = list(range(1, CANTIDAD + 1))
    random.shuffle(numeros)

    for numero in numeros:
        codigos.append("EXP-" + str(numero).zfill(3))
        dnis.append(generar_dni())
        primer_nombre = random.choice(lista_nombres).split(" ")[0]
        nombres.append(primer_nombre + " " + random.choice(lista_ape_paterno))
        asuntos.append(random.choice(lista_asuntos))
        fechas.append(generar_fecha())
        estados.append("Pendiente")

    return codigos, dnis, nombres, asuntos, fechas, estados

if __name__ == "__main__":
    from archivos import guardar_datos

    random.seed(2026)  # misma salida cada vez que se ejecuta
    codigos, dnis, nombres, asuntos, fechas, estados = generar_datos()
    guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas, estados)
    print("Se generaron", len(codigos), "expedientes en", RUTA_ARCHIVO)