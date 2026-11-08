import os
from validaciones import (validar_dni, validar_nombre,
                          validar_asunto, validar_fecha)
from registro import registrar_expediente
from busqueda_orden import buscar_por_codigo, ordenar_por_codigo
from archivos import guardar_datos, cargar_datos
CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(CARPETA, "datos", "expedientes.txt")
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
def pedir_dato(mensaje, funcion_validar, mensaje_error):
    """Pide un dato hasta que sea valido y muestra que se esperaba."""
    while True:
        valor = input(mensaje).strip()
        if funcion_validar(valor):
            return valor
        print("  -> " + mensaje_error)
def cortar(texto, ancho):
    """Recorta el texto con '...' si es mas largo que el ancho de la columna."""
    if len(texto) > ancho:
        return texto[:ancho - 3] + "..."
    return texto
def opcion_registrar(codigos, dnis, nombres, asuntos, fechas):
    print("\n--- Registrar expediente ---")
    dni = pedir_dato("DNI (8 digitos): ", validar_dni,
                     "El DNI debe tener exactamente 8 digitos.")
    nombre = pedir_dato("Nombre completo: ", validar_nombre,
                        "Solo letras y espacios, minimo 3 caracteres.")
    asunto = pedir_dato("Asunto: ", validar_asunto,
                        "Minimo 5 caracteres y sin el simbolo '|'.")
    fecha = pedir_dato("Fecha (DD/MM/AAAA): ", validar_fecha,
                       "Usa el formato DD/MM/AAAA con una fecha real.")
    codigo = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                                  dni, nombre, asunto, fecha)
    print("\nExpediente registrado con codigo:", codigo)
def opcion_buscar(codigos, dnis, nombres, asuntos, fechas):
    print("\n--- Buscar expediente ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    codigo = input("Codigo a buscar (ej. EXP-001): ").strip().upper()
    pos = buscar_por_codigo(codigos, codigo)
    if pos == -1:
        print("No se encontro el expediente", codigo)
    else:
        print("\nExpediente encontrado:")
        print("  Codigo:", codigos[pos])
        print("  DNI:   ", dnis[pos])
        print("  Nombre:", nombres[pos])
        print("  Asunto:", asuntos[pos])
        print("  Fecha: ", fechas[pos])
def opcion_ordenar(codigos, dnis, nombres, asuntos, fechas):
    print("\n--- Ordenar expedientes ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    print("Expedientes ordenados por codigo (de menor a mayor).")
def opcion_listar(codigos, dnis, nombres, asuntos, fechas):
    print("\n--- Lista de expedientes ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    print("\n" + "CODIGO".ljust(10) + "DNI".ljust(10) + "NOMBRE".ljust(22)
          + "ASUNTO".ljust(28) + "FECHA")
    print("-" * 80)
    for i in range(len(codigos)):
        print(codigos[i].ljust(10) + dnis[i].ljust(10)
              + cortar(nombres[i], 20).ljust(22)
              + cortar(asuntos[i], 26).ljust(28) + fechas[i])
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
            print("Opcion invalida. Escribe un numero del menu.")
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
            guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres,
                          asuntos, fechas)
            print("Datos guardados.")
        elif opcion == 0:
            respuesta = input("Seguro que deseas salir? (s/n): ").strip().lower()
            if respuesta == "s":
                guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres,
                              asuntos, fechas)
                print("Datos guardados. Hasta luego.")
            else:
                opcion = -1
        else:
            print("Opcion invalida. Elige una opcion del menu.")
        if opcion != 0:
            pausar()
if __name__ == "__main__":
    main()