"""Pruebas sencillas de HU-02 (CRUD) y HU-07 (archivos y errores).

Se ejecuta con:  python pruebas_hu02_hu07.py

Aqui se prueban las funciones. Lo que depende del teclado (el menu, Ctrl+C,
editar y listar) se prueba a mano: la lista esta al final de este archivo.
"""
import os

from registro import registrar_expediente, ESTADOS
from busqueda_orden import buscar_por_codigo
from archivos import guardar_datos, cargar_datos
from validaciones import validar_dni, validar_nombre, validar_fecha

RUTA_PRUEBA = "prueba_temporal.txt"
resultados = []


def probar(descripcion, resultado, esperado):
    """Compara el resultado con lo esperado y muestra OK o ERROR."""
    if resultado == esperado:
        print("OK    ", descripcion)
    else:
        print("ERROR ", descripcion, "-> se obtuvo", resultado)
    resultados.append(resultado == esperado)


# ------------------------------------------------------------------ HU-02
print("=== HU-02: registrar y buscar tramites ===")

codigos, dnis, nombres, asuntos, fechas, estados = [], [], [], [], [], []
cod1 = registrar_expediente(codigos, dnis, nombres, asuntos, fechas, estados,
                            "12345678", "Ana Perez", "Solicitud de licencia",
                            "10/10/2026")
cod2 = registrar_expediente(codigos, dnis, nombres, asuntos, fechas, estados,
                            "87654321", "Luis Rojas", "Reclamo por demora",
                            "11/10/2026")

probar("CP-02.1 el primer codigo es EXP-001", cod1, "EXP-001")
probar("CP-02.1 el segundo codigo es EXP-002 (no se repite)", cod2, "EXP-002")
probar("CP-02.1 el expediente nuevo empieza como Pendiente", estados[0], ESTADOS[0])
probar("CP-02.1 se guardaron 2 expedientes", len(codigos), 2)
probar("CP-02.1 los datos quedan en la misma posicion", nombres[1], "Luis Rojas")
probar("Buscar EXP-002 devuelve su posicion", buscar_por_codigo(codigos, "EXP-002"), 1)
probar("Buscar un codigo que no existe devuelve -1",
       buscar_por_codigo(codigos, "EXP-999"), -1)

# ------------------------------------------------------------------ HU-07
print("\n=== HU-07: archivos y datos raros ===")

# Guardar y volver a cargar debe dar lo mismo
guardar_datos(RUTA_PRUEBA, codigos, dnis, nombres, asuntos, fechas, estados)
datos = cargar_datos(RUTA_PRUEBA)
probar("Guardar y cargar devuelve los mismos datos",
       datos, (codigos, dnis, nombres, asuntos, fechas, estados))

# Archivo que no existe: no debe fallar, solo devolver listas vacias
probar("Cargar un archivo que no existe devuelve listas vacias",
       cargar_datos("no_existe.txt"), ([], [], [], [], [], []))

# Ruta invalida: "." es una carpeta, no un archivo, asi que no se puede escribir
probar("Guardar en una ruta invalida devuelve False y no se cierra",
       guardar_datos(".", ["EXP-001"], ["1"], ["A"], ["B"], ["C"], ["D"]), False)

# Una linea mal escrita se omite y las demas se cargan
archivo = open(RUTA_PRUEBA, "w", encoding="utf-8")
archivo.write("EXP-001|12345678|Ana|Solicitud|10/10/2026|Pendiente\n")
archivo.write("linea rota\n")
archivo.close()
datos = cargar_datos(RUTA_PRUEBA)
probar("Una linea mal escrita se omite y las demas se cargan", datos[0], ["EXP-001"])

# Datos raros en los formularios: las validaciones deben rechazarlos
probar("DNI con letras se rechaza", validar_dni("abc"), False)
probar("DNI vacio se rechaza", validar_dni(""), False)
probar("Nombre con simbolos se rechaza", validar_nombre("@#$%"), False)
probar("Fecha que no existe (31/04) se rechaza", validar_fecha("31/04/2026"), False)

os.remove(RUTA_PRUEBA)    # borra el archivo temporal de la prueba

print("\nResultado:", resultados.count(True), "de", len(resultados), "pruebas OK")

# ------------------------------------------------------- PRUEBAS A MANO
# Ejecuta: python main.py
#
# CP-02.2 (listado): registra 2 expedientes, elige la opcion 4
#         -> se ven todos en la tabla.
# CP-02.3 (editar y estado): opcion 6 y cambia el nombre; opcion 7 y cambia
#         el estado; opcion 4 -> los cambios se ven en la tabla.
# CP-07.1 (texto en el menu): en "Elige una opcion" escribe abc, @#$, 1.5 y 99
#         (uno por uno) -> sale "Opcion invalida" y el menu sigue funcionando.
# CP-07.2 (interrupcion): en el menu presiona Ctrl+C
#         -> sale "Programa interrumpido" y "Datos guardados", sin errores rojos.
