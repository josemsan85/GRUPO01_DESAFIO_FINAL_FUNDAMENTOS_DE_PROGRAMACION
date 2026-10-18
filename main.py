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
def pausar():
    input("\nPresiona ENTER para continuar...")
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
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
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
def opcion_ordenar(codigos, dnis, nombres, asuntos, fechas):
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    print("Expedientes ordenados por codigo.")
def opcion_listar(codigos, dnis, nombres, asuntos, fechas):
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    print("\n" + "CODIGO".ljust(10) + "DNI".ljust(10) + "NOMBRE".ljust(20)
          + "ASUNTO".ljust(20) + "FECHA")
    print("-" * 70)
    for i in range(len(codigos)):
        print(codigos[i].ljust(10) + dnis[i].ljust(10) + nombres[i].ljust(20)
              + asuntos[i].ljust(20) + fechas[i])
    print("\nTotal:", len(codigos), "expediente(s)")


def main():
    codigos, dnis, nombres, asuntos, fechas = cargar_datos(RUTA_ARCHIVO)
    print("Bienvenido a la Mesa de Partes Digital")
    print("Expedientes cargados:", len(codigos))
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        entrada = input("Elige una opcion: ").strip()
        if not entrada.isdigit():
            print("Opcion invalida.")
            pausar()
            continue
        opcion = int(entrada)
        if opcion == 1:
            opcion_registrar(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 2:
            opcion_buscar(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 3:
            opcion_ordenar(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 4:
            opcion_listar(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 5:
            guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)
            print("Datos guardados.")
        elif opcion == 0:
            respuesta = input("Seguro que deseas salir? (s/n): ").strip().lower()
            if respuesta == "s":
                guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)
                print("Datos guardados. Hasta luego.")
            else:
                opcion = -1  # se queda en el menu
        else:
            print("Opcion invalida.")
        if opcion != 0:
            pausar()
if __name__ == "__main__":
    main()