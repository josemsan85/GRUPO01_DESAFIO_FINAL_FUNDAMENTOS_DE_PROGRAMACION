def generar_codigo(codigos):
    # TODO (EMANUEL): generar un codigo unico, ej. "EXP-001", "EXP-002"...
    return "EXP-001"
def registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                         dni, nombre, asunto, fecha):
    # TODO (EMANUEL): generar el codigo, hacer append en las 5 listas
    # y devolver el codigo generado.
    # La validacion NO se hace aqui, la hace main.py antes de llamar. NO ME HAGAS RENEGAR CHOLO BELLO
    return "EXP-001"
if __name__ == "__main__":
    codigos, dnis, nombres, asuntos, fechas = [], [], [], [], []
    cod = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                               "12345678", "Ana Perez", "Solicitud", "10/10/2026")
    print("Codigo generado:", cod)
    print(codigos, dnis, nombres, asuntos, fechas)