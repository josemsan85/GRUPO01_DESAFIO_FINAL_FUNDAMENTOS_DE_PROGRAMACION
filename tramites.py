"""HU-02: Gestion integral del ciclo de vida de tramites (CRUD) en memoria.

Cada tramite se guarda en 7 listas paralelas (la posicion i de todas las
listas corresponde al mismo tramite):
    codigos, dnis, nombres, correos, tipos, fechas, estados

Este modulo NO usa main.py. Se prueba solo con:
    python tramites.py
    python ejecutar.py tramites     (igual, pero con el control de errores)
"""

from validaciones import (validar_dni, validar_nombre, validar_fecha,
                          validar_correo, validar_estado,
                          TIPOS_VALIDOS, ESTADOS_VALIDOS)
from registro import generar_codigo
from busqueda_orden import buscar_por_codigo
from manejo_errores import pedir_entero, ejecutar_seguro


# ---------------------------------------------------------------------------
# LOGICA DEL CRUD (no pide datos por consola)
# ---------------------------------------------------------------------------

def crear_tramite(codigos, dnis, nombres, correos, tipos, fechas, estados,
                  dni, nombre, correo, tipo, fecha):
    """Genera un codigo unico, agrega el tramite en las 7 listas y lo devuelve.

    El estado inicial siempre es el primero de ESTADOS_VALIDOS ('Pendiente').
    La validacion de los datos la hace la parte de consola (mas abajo).
    """
    codigo = generar_codigo(codigos)
    # Los 7 append juntos para que las listas nunca se desalineen
    codigos.append(codigo)
    dnis.append(dni)
    nombres.append(nombre)
    correos.append(correo)
    tipos.append(tipo)
    fechas.append(fecha)
    estados.append(ESTADOS_VALIDOS[0])
    return codigo


def modificar_campo(codigos, lista_campo, codigo, nuevo_valor):
    """Busca el tramite por codigo y cambia su valor en 'lista_campo'.

    Devuelve True si lo modifico y False si el codigo no existe.
    """
    pos = buscar_por_codigo(codigos, codigo)
    if pos == -1:
        return False
    lista_campo[pos] = nuevo_valor
    return True


def cambiar_estado(codigos, estados, codigo, nuevo_estado):
    """Cambia el estado de un tramite.

    Devuelve False si el codigo no existe o si el estado no es valido.
    """
    if not validar_estado(nuevo_estado):
        return False
    return modificar_campo(codigos, estados, codigo, nuevo_estado)


def calcular_ancho(titulo, valores):
    """Ancho de una columna: el texto mas largo (o el titulo) + 2 espacios."""
    mayor = len(titulo)
    for valor in valores:
        if len(valor) > mayor:
            mayor = len(valor)
    return mayor + 2


def listar_tramites(codigos, dnis, nombres, correos, tipos, fechas, estados):
    """Muestra todos los tramites en formato de tabla (usa f-strings)."""
    if len(codigos) == 0:
        print("No hay tramites registrados.")
        return
    titulos = ["CODIGO", "DNI", "NOMBRE", "CORREO", "TIPO", "FECHA", "ESTADO"]
    columnas = [codigos, dnis, nombres, correos, tipos, fechas, estados]

    anchos = []
    for i in range(len(columnas)):
        anchos.append(calcular_ancho(titulos[i], columnas[i]))

    encabezado = ""
    for i in range(len(titulos)):
        encabezado += f"{titulos[i]:<{anchos[i]}}"
    print("\n" + encabezado.rstrip())
    print("-" * sum(anchos))

    for fila in range(len(codigos)):
        linea = ""
        for i in range(len(columnas)):
            linea += f"{columnas[i][fila]:<{anchos[i]}}"
        print(linea.rstrip())

    print(f"\nTotal: {len(codigos)} tramite(s)")


def mostrar_detalle(pos, codigos, dnis, nombres, correos, tipos, fechas, estados):
    """Muestra todos los datos de un solo tramite."""
    print(f"\nCodigo : {codigos[pos]}")
    print(f"DNI    : {dnis[pos]}")
    print(f"Nombre : {nombres[pos]}")
    print(f"Correo : {correos[pos]}")
    print(f"Tipo   : {tipos[pos]}")
    print(f"Fecha  : {fechas[pos]}")
    print(f"Estado : {estados[pos]}")


# ---------------------------------------------------------------------------
# PARTE DE CONSOLA (pide datos y los valida)
# ---------------------------------------------------------------------------

def pedir_dato(mensaje, funcion_validar):
    """Pide un dato hasta que sea valido."""
    while True:
        valor = input(mensaje).strip()
        if funcion_validar(valor):
            return valor
        print("Dato invalido, intenta de nuevo.")


def elegir_de_lista(titulo, opciones):
    """Muestra opciones numeradas y devuelve la que elija la persona."""
    print(titulo)
    for i in range(len(opciones)):
        print(f"  {i + 1}. {opciones[i]}")
    numero = pedir_entero("Elige una opcion: ", 1, len(opciones))
    return opciones[numero - 1]


def opcion_registrar(codigos, dnis, nombres, correos, tipos, fechas, estados):
    dni = pedir_dato("DNI (8 digitos): ", validar_dni)
    nombre = pedir_dato("Nombre completo: ", validar_nombre)
    correo = pedir_dato("Correo electronico: ", validar_correo)
    tipo = elegir_de_lista("Tipo de tramite:", TIPOS_VALIDOS)
    fecha = pedir_dato("Fecha (DD/MM/AAAA): ", validar_fecha)
    codigo = crear_tramite(codigos, dnis, nombres, correos, tipos, fechas,
                           estados, dni, nombre, correo, tipo, fecha)
    print(f"Tramite registrado con codigo: {codigo} (estado: {estados[-1]})")


def opcion_listar(codigos, dnis, nombres, correos, tipos, fechas, estados):
    listar_tramites(codigos, dnis, nombres, correos, tipos, fechas, estados)


def opcion_modificar(codigos, dnis, nombres, correos, tipos, fechas, estados):
    if len(codigos) == 0:
        print("No hay tramites registrados.")
        return
    codigo = input("Codigo del tramite a modificar (ej. EXP-001): ").strip().upper()
    pos = buscar_por_codigo(codigos, codigo)
    if pos == -1:
        print("No se encontro el tramite.")
        return

    mostrar_detalle(pos, codigos, dnis, nombres, correos, tipos, fechas, estados)
    print("\nQue campo deseas modificar?")
    print("  1. DNI")
    print("  2. Nombre")
    print("  3. Correo")
    print("  4. Tipo")
    print("  5. Fecha")
    print("  0. Cancelar")
    campo = pedir_entero("Elige una opcion: ", 0, 5)

    if campo == 0:
        print("Modificacion cancelada.")
        return
    if campo == 1:
        nuevo = pedir_dato("Nuevo DNI (8 digitos): ", validar_dni)
        modificar_campo(codigos, dnis, codigo, nuevo)
    elif campo == 2:
        nuevo = pedir_dato("Nuevo nombre: ", validar_nombre)
        modificar_campo(codigos, nombres, codigo, nuevo)
    elif campo == 3:
        nuevo = pedir_dato("Nuevo correo: ", validar_correo)
        modificar_campo(codigos, correos, codigo, nuevo)
    elif campo == 4:
        nuevo = elegir_de_lista("Nuevo tipo de tramite:", TIPOS_VALIDOS)
        modificar_campo(codigos, tipos, codigo, nuevo)
    else:
        nuevo = pedir_dato("Nueva fecha (DD/MM/AAAA): ", validar_fecha)
        modificar_campo(codigos, fechas, codigo, nuevo)
    print("Tramite actualizado. Usa 'Listar tramites' para ver el cambio.")


def opcion_cambiar_estado(codigos, dnis, nombres, correos, tipos, fechas, estados):
    if len(codigos) == 0:
        print("No hay tramites registrados.")
        return
    codigo = input("Codigo del tramite (ej. EXP-001): ").strip().upper()
    pos = buscar_por_codigo(codigos, codigo)
    if pos == -1:
        print("No se encontro el tramite.")
        return
    print(f"Estado actual de {codigo}: {estados[pos]}")
    nuevo = elegir_de_lista("Nuevo estado:", ESTADOS_VALIDOS)
    cambiar_estado(codigos, estados, codigo, nuevo)
    print(f"Estado actualizado a: {nuevo}")


def mostrar_menu():
    print("\n===== GESTION DE TRAMITES (HU-02) =====")
    print("1. Registrar tramite")
    print("2. Listar tramites")
    print("3. Buscar y modificar tramite por codigo")
    print("4. Cambiar estado de un tramite")
    print("0. Salir")


def menu_tramites():
    """Menu principal del CRUD. Los datos viven solo en memoria."""
    codigos, dnis, nombres, correos, tipos, fechas, estados = [], [], [], [], [], [], []
    print("Bienvenido a la Gestion de Tramites")

    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = pedir_entero("Elige una opcion: ", 0, 4)
        if opcion == 1:
            opcion_registrar(codigos, dnis, nombres, correos, tipos, fechas, estados)
        elif opcion == 2:
            opcion_listar(codigos, dnis, nombres, correos, tipos, fechas, estados)
        elif opcion == 3:
            opcion_modificar(codigos, dnis, nombres, correos, tipos, fechas, estados)
        elif opcion == 4:
            opcion_cambiar_estado(codigos, dnis, nombres, correos, tipos, fechas, estados)
    print("Hasta luego.")


if __name__ == "__main__":
    ejecutar_seguro(menu_tramites)
