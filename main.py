from validaciones import (validar_dni, validar_nombre,
                          validar_asunto, validar_fecha)
from registro import registrar_expediente
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
    print("0. Salir")
def pedir_dato(mensaje, funcion_validar):
    """Pide un dato hasta que sea valido."""
    while True:
        valor = input(mensaje).strip()
        if funcion_validar(valor):
            return valor
        print("Dato invalido, intenta de nuevo.")
def opcion_registrar(codigos, dnis, nombres, asuntos, fechas):
    dni = pedir_dato("DNI (8 digitos): ", validar_dni)
    nombre = pedir_dato("Nombre completo: ", validar_nombre)
    asunto = pedir_dato("Asunto: ", validar_asunto)
    fecha = pedir_dato("Fecha (DD/MM/AAAA): ", validar_fecha)
    codigo = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                                  dni, nombre, asunto, fecha)
    print("Expediente registrado con codigo:", codigo)
def opcion_buscar(codigos, dnis, nombres, asuntos, fechas):
    codigo = input("Codigo a buscar: ").strip().upper()
    pos = buscar_por_codigo(codigos, codigo)
    if pos == -1:
        print("No se encontro el expediente.")
    else:
        print("Codigo:", codigos[pos])
        print("DNI:", dnis[pos])
        print("Nombre:", nombres[pos])
        print("Asunto:", asuntos[pos])
        print("Fecha:", fechas[pos])
def opcion_listar(codigos, dnis, nombres, asuntos, fechas):
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    print("\nCODIGO    | DNI      | NOMBRE            | ASUNTO         | FECHA")
    for i in range(len(codigos)):
        print(codigos[i], "|", dnis[i], "|", nombres[i], "|",
              asuntos[i], "|", fechas[i])
def main():
    codigos, dnis, nombres, asuntos, fechas = cargar_datos(RUTA_ARCHIVO)
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        entrada = input("Elige una opcion: ").strip()
        if not entrada.isdigit():
            print("Opcion invalida.")
            continue
        opcion = int(entrada)
        if opcion == 1:
            opcion_registrar(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 2:
            opcion_buscar(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 3:
            ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
            print("Expedientes ordenados por codigo.")
        elif opcion == 4:
            opcion_listar(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 5:
            guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)
            print("Datos guardados.")
        elif opcion == 0:
            guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)
            print("Datos guardados. Hasta luego.")
        else:
            print("Opcion invalida.")
if __name__ == "__main__":
    main()
