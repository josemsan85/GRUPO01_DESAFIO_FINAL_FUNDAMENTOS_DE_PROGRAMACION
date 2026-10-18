
def validar_no_vacio(texto):
    """Un campo no puede estar vacio ni tener solo espacios."""
    return len(texto.strip()) > 0


def validar_dni(dni):
    """El DNI debe tener exactamente 8 caracteres y todos deben ser digitos."""
    return len(dni) == 8 and dni.isdigit()


def validar_nombre(nombre):
    """Nombre no vacio, minimo 3 caracteres, solo letras y espacios."""
    nombre = nombre.strip()
    if not validar_no_vacio(nombre):
        return False
    if len(nombre) < 3:
        return False
    for caracter in nombre:
        # isalpha() acepta tildes y la ñ; ademas dejamos pasar el espacio
        if not (caracter.isalpha() or caracter == " "):
            return False
    return True


def validar_asunto(asunto):
    """Asunto no vacio, de minimo 5 caracteres y sin el simbolo '|'.

    El simbolo '|' no se permite porque el archivo de datos usa '|'
    para separar los campos de cada expediente.
    """
    asunto = asunto.strip()
    if not validar_no_vacio(asunto):
        return False
    if len(asunto) < 5:
        return False
    if "|" in asunto:
        return False
    return True


def dias_del_mes(mes, anio):
    """Devuelve cuantos dias tiene un mes (considera los años bisiestos)."""
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            return 29
        return 28
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    return 31


def validar_fecha(fecha):
    """Formato DD/MM/AAAA con dia, mes y año en un rango valido."""
    partes = fecha.split("/")
    if len(partes) != 3:
        return False

    dia_texto = partes[0]
    mes_texto = partes[1]
    anio_texto = partes[2]

    # Formato exacto: 2 digitos para dia y mes, 4 digitos para el año
    if len(dia_texto) != 2 or len(mes_texto) != 2 or len(anio_texto) != 4:
        return False
    if not (dia_texto.isdigit() and mes_texto.isdigit() and anio_texto.isdigit()):
        return False

    dia = int(dia_texto)
    mes = int(mes_texto)
    anio = int(anio_texto)

    if anio < 1900:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_del_mes(mes, anio):
        return False
    return True


def probar(descripcion, resultado, esperado):
    """Ayuda para las pruebas: compara el resultado con lo esperado."""
    if resultado == esperado:
        print("OK    ", descripcion)
    else:
        print("ERROR ", descripcion, "-> se obtuvo", resultado)


if __name__ == "__main__":
    # Pruebas rapidas de este modulo (python validaciones.py)
    print("--- DNI ---")
    probar("DNI valido 12345678", validar_dni("12345678"), True)
    probar("DNI con 3 digitos", validar_dni("123"), False)
    probar("DNI con 9 digitos", validar_dni("123456789"), False)
    probar("DNI con letra", validar_dni("1234567a"), False)
    probar("DNI con espacio", validar_dni(" 2345678"), False)
    probar("DNI vacio", validar_dni(""), False)

    print("--- Nombre ---")
    probar("Ana Perez", validar_nombre("Ana Perez"), True)
    probar("María José (con tildes)", validar_nombre("María José"), True)
    probar("Nombre con numero", validar_nombre("Ana2"), False)
    probar("Nombre muy corto", validar_nombre("Al"), False)
    probar("Nombre solo espacios", validar_nombre("    "), False)
    probar("Nombre vacio", validar_nombre(""), False)

    print("--- Asunto ---")
    probar("Solicitud de licencia", validar_asunto("Solicitud de licencia"), True)
    probar("Asunto muy corto", validar_asunto("Hola"), False)
    probar("Asunto vacio", validar_asunto("   "), False)
    probar("Asunto con barra |", validar_asunto("Reclamo | urgente"), False)

    print("--- Fecha ---")
    probar("10/10/2026", validar_fecha("10/10/2026"), True)
    probar("29/02/2024 (bisiesto)", validar_fecha("29/02/2024"), True)
    probar("29/02/2025 (no bisiesto)", validar_fecha("29/02/2025"), False)
    probar("31/04/2026 (abril tiene 30)", validar_fecha("31/04/2026"), False)
    probar("10/13/2026 (mes 13)", validar_fecha("10/13/2026"), False)
    probar("00/10/2026 (dia 0)", validar_fecha("00/10/2026"), False)
    probar("5/3/2026 (sin ceros)", validar_fecha("5/3/2026"), False)
    probar("10-10-2026 (guiones)", validar_fecha("10-10-2026"), False)
    probar("10/10/26 (año corto)", validar_fecha("10/10/26"), False)
    probar("Fecha vacia", validar_fecha(""), False)
