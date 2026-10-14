def validar_dni(dni):
    # TODO (EMANUEL): 8 caracteres, solo digitos
    return True
def validar_nombre(nombre):
    # TODO (EMANUEL): no vacio, solo letras y espacios, minimo 3 caracteres
    return True
def validar_asunto(asunto):
    # TODO (EMANUEL): no vacio, longitud minima
    return True
def validar_fecha(fecha):
    # TODO (EMANUEL): formato DD/MM/AAAA, dia y mes en rango valido
    return True
if __name__ == "__main__":
    # Pruebas rapidas de este modulo (python validaciones.py)
    print("DNI valido:", validar_dni("12345678"))
    print("DNI invalido:", validar_dni("123"))
