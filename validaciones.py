"""Validaciones de los datos de un expediente.

Cada funcion recibe un texto (str) y devuelve True si el dato es valido
o False si no lo es. Solo se usan metodos de cadenas: len, strip, isdigit,
isalpha, split y el operador in.
"""


def validar_dni(dni):
    """El DNI debe tener exactamente 8 caracteres y todos deben ser digitos."""
    return len(dni) == 8 and dni.isdigit()


def validar_nombre(nombre):
    # TODO: no vacio, solo letras y espacios, minimo 3 caracteres
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

