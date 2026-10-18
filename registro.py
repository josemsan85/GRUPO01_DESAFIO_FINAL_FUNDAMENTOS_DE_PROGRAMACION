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
    """Genera el codigo, agrega el expediente en las 5 listas y lo devuelve.

    La validacion NO se hace aqui: la hace main.py (con validaciones.py)
    antes de llamar a esta funcion.
    """
    codigo = generar_codigo(codigos)

    # Los 5 append se hacen juntos para que las listas nunca se desalineen
    codigos.append(codigo)
    dnis.append(dni)
    nombres.append(nombre)
    asuntos.append(asunto)
    fechas.append(fecha)

    return codigo


if __name__ == "__main__":
    # Pruebas rapidas de este modulo (python registro.py)
    codigos, dnis, nombres, asuntos, fechas = [], [], [], [], []

    cod1 = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                                "12345678", "Ana Perez", "Solicitud", "10/10/2026")
    cod2 = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                                "87654321", "Luis Rojas", "Reclamo", "11/10/2026")
    print("Codigos generados:", cod1, cod2)
    print(codigos)
    print(dnis)
    print(nombres)
    print(asuntos)
    print(fechas)

    # El codigo siempre sigue al numero mas alto, aunque la lista este desordenada
    print("Con lista desordenada:", generar_codigo(["EXP-005", "EXP-002"]))  # EXP-006
    print("Con lista vacia:", generar_codigo([]))                            # EXP-001
