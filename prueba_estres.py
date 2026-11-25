"""HU-07: pruebas de estres con datos anomalos (sin escribir nada a mano).

Ejecutar:  python prueba_estres.py

Simula lo que teclearia una persona usando un input() falso y comprueba
los casos de prueba CP-02.1, CP-02.2, CP-02.3, CP-07.1 y CP-07.2.
"""

import builtins
import io
import os
import shutil
import tempfile
from contextlib import redirect_stdout

from manejo_errores import (pedir_entero, guardar_seguro, cargar_seguro,
                            ejecutar_seguro)
from validaciones import (validar_dni, validar_nombre, validar_correo,
                          validar_fecha, validar_tipo, validar_estado)
import tramites

resultados = []


def comprobar(descripcion, condicion):
    if condicion:
        print("OK    ", descripcion)
    else:
        print("ERROR ", descripcion)
    resultados.append(bool(condicion))


def simular(funcion, entradas):
    """Ejecuta funcion() con un input() falso que va entregando 'entradas'.

    Si una entrada es KeyboardInterrupt, simula que se presiono Ctrl+C.
    Devuelve (texto_impreso, excepcion_que_escapo_o_None).
    """
    pendientes = list(entradas)

    def input_falso(mensaje=""):
        print(mensaje, end="")
        if len(pendientes) == 0:
            raise EOFError
        valor = pendientes.pop(0)
        if valor is KeyboardInterrupt:
            raise KeyboardInterrupt
        print(valor)
        return valor

    original = builtins.input
    builtins.input = input_falso
    salida = io.StringIO()
    error = None
    try:
        with redirect_stdout(salida):
            funcion()
    except BaseException as e:
        error = e
    finally:
        builtins.input = original
    return salida.getvalue(), error


def listas_nuevas():
    return [], [], [], [], [], [], []


print("--- Validadores con datos anomalos ---")
comprobar("DNI con letras rechazado", not validar_dni("abcdefgh"))
comprobar("DNI larguisimo rechazado", not validar_dni("1" * 50))
comprobar("DNI con simbolos rechazado", not validar_dni("12345-78"))
comprobar("Nombre con numeros rechazado", not validar_nombre("R2D2"))
comprobar("Nombre con simbolos rechazado", not validar_nombre("<script>"))
comprobar("Correo sin @ rechazado", not validar_correo("anagmail.com"))
comprobar("Correo con espacios rechazado", not validar_correo("ana perez@gmail.com"))
comprobar("Correo con dos @ rechazado", not validar_correo("a@@b.com"))
comprobar("Correo sin punto en dominio rechazado", not validar_correo("ana@gmail"))
comprobar("Correo con | rechazado", not validar_correo("a|b@gmail.com"))
comprobar("Correo valido aceptado", validar_correo("ana.perez@gmail.com"))
comprobar("Fecha inexistente 31/02 rechazada", not validar_fecha("31/02/2026"))
comprobar("Fecha con texto rechazada", not validar_fecha("hoy"))
comprobar("Tipo inventado rechazado", not validar_tipo("Hackeo"))
comprobar("Estado inventado rechazado", not validar_estado("Volando"))

print("\n--- CP-07.1: texto donde se esperan numeros ---")
retorno = []
salida, error = simular(
    lambda: retorno.append(pedir_entero("Opcion: ", 1, 4)),
    ["abc", "", "   ", "3.5", "-7", "99", "@#$%", "2"])
comprobar("pedir_entero no lanza excepcion", error is None)
comprobar("pedir_entero termina devolviendo el 2 valido", retorno == [2])
comprobar("Muestra el mensaje 'Opcion invalida'", "Opcion invalida" in salida)

salida, error = simular(tramites.menu_tramites,
                        ["abc", "@#$%", "", "   ", "99", "-1", "3.5", "0"])
comprobar("Menu principal sobrevive a entradas basura", error is None)
comprobar("Menu muestra 'Opcion invalida' y vuelve a pedir",
          salida.count("Opcion invalida") >= 6)
comprobar("Menu termina normalmente con la opcion 0", "Hasta luego." in salida)

print("\n--- CP-02.1: registro con datos anomalos antes de los validos ---")
cod, dni, nom, cor, tip, fec, est = listas_nuevas()
entradas = [
    "abc", "123", "", "12345678",                        # DNI
    "R2D2", "A", "Ana Perez",                            # nombre
    "sin-arroba", "a@b", "ana@gmail.com",                # correo
    "x", "9", "1",                                       # tipo (menu)
    "31/02/2026", "10-10-2026", "10/10/2026",            # fecha
]
salida, error = simular(
    lambda: tramites.opcion_registrar(cod, dni, nom, cor, tip, fec, est),
    entradas)
comprobar("Registro no lanza excepcion", error is None)
comprobar("Se genero el codigo EXP-001", cod == ["EXP-001"])
comprobar("Las 7 listas quedaron alineadas",
          len(dni) == len(nom) == len(cor) == len(tip) == len(fec) == len(est) == 1)
comprobar("Estado inicial es Pendiente", est == ["Pendiente"])
comprobar("Se guardaron los datos validos",
          dni == ["12345678"] and nom == ["Ana Perez"]
          and cor == ["ana@gmail.com"] and fec == ["10/10/2026"])

salida, error = simular(
    lambda: tramites.opcion_registrar(cod, dni, nom, cor, tip, fec, est),
    ["87654321", "Luis Rojas", "luis@yahoo.com", "2", "11/10/2026"])
comprobar("Segundo codigo es EXP-002 (unico)", cod == ["EXP-001", "EXP-002"])

print("\n--- CP-02.2: listado general ---")
salida, error = simular(
    lambda: tramites.opcion_listar(cod, dni, nom, cor, tip, fec, est), [])
comprobar("Listado muestra ambos expedientes",
          "EXP-001" in salida and "EXP-002" in salida)
comprobar("Listado muestra el total", "Total: 2 tramite(s)" in salida)

salida, error = simular(
    lambda: tramites.opcion_listar([], [], [], [], [], [], []), [])
comprobar("Listado vacio avisa que no hay tramites",
          "No hay tramites registrados." in salida)

print("\n--- CP-02.3: edicion y cambio de estado ---")
salida, error = simular(
    lambda: tramites.opcion_modificar(cod, dni, nom, cor, tip, fec, est),
    ["EXP-999"])
comprobar("Codigo inexistente se informa sin romper",
          error is None and "No se encontro" in salida)

salida, error = simular(
    lambda: tramites.opcion_modificar(cod, dni, nom, cor, tip, fec, est),
    ["exp-001", "abc", "3", "mal", "nuevo@correo.com"])
comprobar("Modificar correo funciona (codigo en minusculas, menu con basura)",
          error is None and cor[0] == "nuevo@correo.com")

salida, error = simular(
    lambda: tramites.opcion_cambiar_estado(cod, dni, nom, cor, tip, fec, est),
    ["EXP-001", "x", "3"])
comprobar("Cambiar estado a Atendido funciona",
          error is None and est[0] == "Atendido")

salida, error = simular(
    lambda: tramites.opcion_listar(cod, dni, nom, cor, tip, fec, est), [])
comprobar("Los cambios se reflejan al listar nuevamente",
          "nuevo@correo.com" in salida and "Atendido" in salida)

print("\n--- HU-07: proteccion de archivos ---")
carpeta = tempfile.mkdtemp()


def guardar_prueba(ruta, lista):
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("|".join(lista))


def cargar_prueba(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


ruta_ok = os.path.join(carpeta, "datos", "expedientes.txt")
comprobar("Guardar crea la carpeta 'datos' si no existe",
          guardar_seguro(guardar_prueba, ruta_ok, ["a", "b"])
          and os.path.exists(ruta_ok))

archivo_falso = os.path.join(carpeta, "soy_un_archivo.txt")
with open(archivo_falso, "w") as f:
    f.write("x")
ruta_mala = os.path.join(archivo_falso, "datos.txt")
retorno = []
salida, error = simular(
    lambda: retorno.append(guardar_seguro(guardar_prueba, ruta_mala, ["a"])), [])
comprobar("Guardar en ruta imposible devuelve False sin excepcion",
          error is None and retorno == [False] and "Error" in salida)

retorno = []
salida, error = simular(
    lambda: retorno.append(
        cargar_seguro(cargar_prueba, os.path.join(carpeta, "nada.txt"), "VACIO")),
    [])
comprobar("Cargar archivo inexistente devuelve el valor por defecto",
          error is None and retorno == ["VACIO"] and "Aviso" in salida)

ruta_bin = os.path.join(carpeta, "corrupto.dat")
with open(ruta_bin, "wb") as f:
    f.write(bytes([0xFF, 0xFE, 0xFA]))
retorno = []
salida, error = simular(
    lambda: retorno.append(cargar_seguro(cargar_prueba, ruta_bin, "VACIO")), [])
comprobar("Cargar archivo corrupto no rompe el programa",
          error is None and retorno == ["VACIO"])
shutil.rmtree(carpeta)

print("\n--- CP-07.2: interrupcion de ejecucion ---")
salida, error = simular(lambda: ejecutar_seguro(tramites.menu_tramites),
                        ["1", KeyboardInterrupt])
comprobar("Ctrl+C a mitad de un formulario sale limpio",
          error is None and "interrumpido" in salida)

salida, error = simular(lambda: ejecutar_seguro(tramites.menu_tramites), ["1"])
comprobar("Cierre de entrada (Ctrl+Z / Ctrl+D) sale limpio",
          error is None and "entrada" in salida)

salida, error = simular(lambda: ejecutar_seguro(lambda: 1 / 0), [])
comprobar("Un error imprevisto muestra mensaje y no traza",
          error is None and "error inesperado" in salida)

print(f"\nResultado: {sum(resultados)} de {len(resultados)} pruebas OK")
raise SystemExit(0 if all(resultados) else 1)
