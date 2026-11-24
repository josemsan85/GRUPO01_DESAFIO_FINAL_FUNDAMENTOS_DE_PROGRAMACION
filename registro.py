# Estados posibles de un expediente
ESTADOS = ["Pendiente", "En proceso", "Atendido", "Rechazado"]


def generar_codigo(codigos):
    """Genera un codigo unico: EXP-001, EXP-002, EXP-003...

    Empieza con (cantidad de expedientes + 1). Si ese codigo ya existe,
    sigue subiendo de uno en uno hasta encontrar uno libre.
    """
    numero = len(codigos) + 1
    # zfill(3) rellena con ceros a la izquierda: 7 -> "007"
    while "EXP-" + str(numero).zfill(3) in codigos:
        numero = numero + 1
    return "EXP-" + str(numero).zfill(3)


def registrar_expediente(codigos, dnis, nombres, asuntos, fechas, estados,
                         dni, nombre, asunto, fecha):
    """Crea el codigo, guarda el expediente en las 6 listas y devuelve el codigo.

    Todo expediente nuevo empieza con estado "Pendiente".
    Los datos ya vienen validados desde main.py.
    """
    codigo = generar_codigo(codigos)
    codigos.append(codigo)
    dnis.append(dni)
    nombres.append(nombre)
    asuntos.append(asunto)
    fechas.append(fecha)
    estados.append(ESTADOS[0])
    return codigo


if __name__ == "__main__":
    # Pruebas rapidas de este archivo (python registro.py)
    codigos, dnis, nombres, asuntos, fechas, estados = [], [], [], [], [], []
    cod1 = registrar_expediente(codigos, dnis, nombres, asuntos, fechas, estados,
                                "12345678", "Ana Perez", "Solicitud", "10/10/2026")
    cod2 = registrar_expediente(codigos, dnis, nombres, asuntos, fechas, estados,
                                "87654321", "Luis Rojas", "Reclamo", "11/10/2026")
    print("Codigos generados:", cod1, cod2)   # EXP-001 EXP-002
    print(estados)                            # ["Pendiente", "Pendiente"]
    print("Lista vacia:", generar_codigo([]))                   # EXP-001
    print("Con dos expedientes:", generar_codigo(["EXP-001", "EXP-002"]))  # EXP-003
    print("Si el codigo ya existe:", generar_codigo(["EXP-002"]))          # EXP-003
