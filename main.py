from validaciones import (validar_dni, validar_nombre,
                          validar_asunto, validar_fecha)
from registro import registrar_expediente, ESTADOS
from busqueda_orden import buscar_por_codigo, ordenar_por_codigo
from archivos import guardar_datos, cargar_datos

RUTA_ARCHIVO = "datos/expedientes.txt"


def mostrar_menu():
    print("\n===== MESA DE PARTES DIGITAL =====")
    print("1. Registrar expediente")
    print("2. Buscar expediente por codigo")
    print("3. Ordenar expedientes por codigo")
    print("4. Listar expedientes")
    print("5. Guardar datos")
    print("6. Editar expediente")
    print("7. Cambiar estado de un expediente")
    print("0. Salir")


def pausar():
    input("\nPresiona ENTER para continuar...")


def pedir_numero(mensaje, minimo, maximo):
    """Pide un numero entre minimo y maximo (HU-07).

    Si escriben letras, simbolos o nada, muestra "Opcion invalida"
    y vuelve a pedir el numero, sin cerrar el programa.
    """
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)          # si no es un numero, salta a "except"
            if numero >= minimo and numero <= maximo:
                return numero
            print(f"Opcion invalida: elige un numero entre {minimo} y {maximo}.")
        except ValueError:
            print("Opcion invalida: escribe solo numeros.")


def pedir_dato(mensaje, funcion_validar):
    """Pide un dato hasta que sea valido."""
    while True:
        valor = input(mensaje).strip()
        if funcion_validar(valor):
            return valor
        print("Dato invalido, intenta de nuevo.")


def pedir_dato_o_mantener(mensaje, funcion_validar, valor_actual):
    """Igual que pedir_dato, pero si presionan ENTER se queda el valor actual."""
    while True:
        valor = input(f"{mensaje} [{valor_actual}]: ").strip()
        if valor == "":
            return valor_actual
        if funcion_validar(valor):
            return valor
        print("Dato invalido, intenta de nuevo.")


def pedir_posicion(codigos, mensaje):
    """Pide un codigo y devuelve su posicion en la lista (-1 si no existe)."""
    codigo = input(mensaje).strip().upper()
    pos = buscar_por_codigo(codigos, codigo)
    if pos == -1:
        print("No se encontro el expediente.")
    return pos


# ---------------------------------------------------------------- HU-02: CRUD

def opcion_registrar(codigos, dnis, nombres, asuntos, fechas, estados):
    dni = pedir_dato("DNI (8 digitos): ", validar_dni)
    nombre = pedir_dato("Nombre completo: ", validar_nombre)
    asunto = pedir_dato("Asunto: ", validar_asunto)
    fecha = pedir_dato("Fecha (DD/MM/AAAA): ", validar_fecha)
    codigo = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                                  estados, dni, nombre, asunto, fecha)
    print(f"Expediente registrado con codigo: {codigo} (estado: Pendiente)")


def opcion_buscar(codigos, dnis, nombres, asuntos, fechas, estados):
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    pos = pedir_posicion(codigos, "Codigo a buscar: ")
    if pos != -1:
        print(f"Codigo: {codigos[pos]}")
        print(f"DNI:    {dnis[pos]}")
        print(f"Nombre: {nombres[pos]}")
        print(f"Asunto: {asuntos[pos]}")
        print(f"Fecha:  {fechas[pos]}")
        print(f"Estado: {estados[pos]}")


def opcion_ordenar(codigos, dnis, nombres, asuntos, fechas, estados):
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas, estados)
    print("Expedientes ordenados por codigo.")


def opcion_listar(codigos, dnis, nombres, asuntos, fechas, estados):
    """Muestra todos los expedientes en una tabla usando f-strings."""
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    print()
    print(f"{'CODIGO':<10}{'DNI':<10}{'NOMBRE':<22}{'ASUNTO':<24}"
          f"{'FECHA':<12}{'ESTADO'}")
    print("-" * 90)
    for i in range(len(codigos)):
        # [:20] y [:22] cortan los textos largos para que la tabla no se descuadre
        print(f"{codigos[i]:<10}{dnis[i]:<10}{nombres[i][:20]:<22}"
              f"{asuntos[i][:22]:<24}{fechas[i]:<12}{estados[i]}")
    print(f"\nTotal: {len(codigos)} expediente(s)")


def opcion_editar(codigos, dnis, nombres, asuntos, fechas, estados):
    """Busca un expediente por su codigo y cambia sus datos."""
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    pos = pedir_posicion(codigos, "Codigo del expediente a editar: ")
    if pos == -1:
        return
    print("Presiona ENTER sin escribir nada para conservar el valor actual.")
    dnis[pos] = pedir_dato_o_mantener("DNI (8 digitos)", validar_dni, dnis[pos])
    nombres[pos] = pedir_dato_o_mantener("Nombre completo", validar_nombre,
                                         nombres[pos])
    asuntos[pos] = pedir_dato_o_mantener("Asunto", validar_asunto, asuntos[pos])
    fechas[pos] = pedir_dato_o_mantener("Fecha (DD/MM/AAAA)", validar_fecha,
                                        fechas[pos])
    print(f"Expediente {codigos[pos]} actualizado.")


def opcion_cambiar_estado(codigos, dnis, nombres, asuntos, fechas, estados):
    """Cambia el estado de un expediente (Pendiente, En proceso, ...)."""
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    pos = pedir_posicion(codigos, "Codigo del expediente: ")
    if pos == -1:
        return
    print(f"Estado actual de {codigos[pos]}: {estados[pos]}")
    for i in range(len(ESTADOS)):
        print(f"{i + 1}. {ESTADOS[i]}")
    eleccion = pedir_numero("Nuevo estado: ", 1, len(ESTADOS))
    estados[pos] = ESTADOS[eleccion - 1]
    print(f"Estado de {codigos[pos]} cambiado a: {estados[pos]}")


# ------------------------------------------------------------------- programa

def main():
    codigos, dnis, nombres, asuntos, fechas, estados = cargar_datos(RUTA_ARCHIVO)
    print("Bienvenido a la Mesa de Partes Digital")
    print(f"Expedientes cargados: {len(codigos)}")

    try:
        while True:
            mostrar_menu()
            opcion = pedir_numero("Elige una opcion: ", 0, 7)

            if opcion == 1:
                opcion_registrar(codigos, dnis, nombres, asuntos, fechas, estados)
            elif opcion == 2:
                opcion_buscar(codigos, dnis, nombres, asuntos, fechas, estados)
            elif opcion == 3:
                opcion_ordenar(codigos, dnis, nombres, asuntos, fechas, estados)
            elif opcion == 4:
                opcion_listar(codigos, dnis, nombres, asuntos, fechas, estados)
            elif opcion == 5:
                if guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres,
                                 asuntos, fechas, estados):
                    print("Datos guardados.")
            elif opcion == 6:
                opcion_editar(codigos, dnis, nombres, asuntos, fechas, estados)
            elif opcion == 7:
                opcion_cambiar_estado(codigos, dnis, nombres, asuntos, fechas,
                                      estados)
            elif opcion == 0:
                respuesta = input("Seguro que deseas salir? (s/n): ").strip().lower()
                if respuesta == "s":
                    if guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres,
                                     asuntos, fechas, estados):
                        print("Datos guardados. Hasta luego.")
                        break                     # sale del while: fin del programa
                    print("No se pudo guardar. Revisa el error e intenta "
                          "de nuevo con la opcion 5.")

            pausar()

    except (KeyboardInterrupt, EOFError):
        # HU-07: Ctrl+C (o cierre de la entrada) -> salida limpia, sin errores rojos
        print("\n\nPrograma interrumpido por el usuario. Guardando datos...")
        if guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas,
                         estados):
            print("Datos guardados. Hasta luego.")


if __name__ == "__main__":
    main()
