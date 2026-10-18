"""Registro de expedientes.

Los datos se guardan en 5 listas paralelas: la posicion i de cada lista
corresponde al mismo expediente (codigos[i], dnis[i], nombres[i], ...).
"""


def generar_codigo(codigos):
    """Genera un codigo unico con el formato EXP-001, EXP-002, EXP-003...

    Busca el numero mas alto que ya existe en la lista y le suma 1.
    Asi el codigo nuevo nunca se repite, aunque la lista este desordenada
    o se haya cargado desde el archivo.
    """
    mayor = 0
    for codigo in codigos:
        numero_texto = codigo[4:]          # "EXP-007"[4:] -> "007"
        if numero_texto.isdigit():         # ignora codigos mal formados
            numero = int(numero_texto)
            if numero > mayor:
                mayor = numero

    nuevo = mayor + 1
    # zfill(3) rellena con ceros a la izquierda: 7 -> "007"
    return "EXP-" + str(nuevo).zfill(3)


def registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                         dni, nombre, asunto, fecha):
    # TODO: generar el codigo, hacer append en las 5 listas
    # y devolver el codigo generado.
    # La validacion NO se hace aqui, la hace main.py antes de llamar.
    return "EXP-001"


if __name__ == "__main__":
    # Pruebas rapidas de este modulo (python registro.py)
    print("Con lista desordenada:", generar_codigo(["EXP-005", "EXP-002"]))  # EXP-006
    print("Con lista vacia:", generar_codigo([]))                            # EXP-001

