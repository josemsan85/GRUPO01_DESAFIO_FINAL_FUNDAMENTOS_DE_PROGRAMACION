

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
    # TODO: no vacio, longitud minima, sin el simbolo "|"
    return True


def validar_fecha(fecha):
    # TODO: formato DD/MM/AAAA, dia y mes en rango valido
    return True


if __name__ == "__main__":
    # Pruebas rapidas de este modulo (python validaciones.py)
    print("DNI valido:", validar_dni("12345678"))
    print("DNI invalido:", validar_dni("123"))

