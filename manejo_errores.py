"""HU-07: Control de excepciones y estabilidad ante entradas invalidas.

Funciones reutilizables (no dependen de main.py ni de archivos.py):
  - pedir_entero:    pide un numero y nunca lanza ValueError.
  - guardar_seguro:  llama a una funcion de guardado protegida con try/except.
  - cargar_seguro:   llama a una funcion de carga protegida con try/except.
  - ejecutar_seguro: corre un programa y atrapa Ctrl+C, Ctrl+Z y errores.

Ejemplo con las funciones de archivos.py (cuando se integre al main):
    guardar_seguro(guardar_datos, RUTA_ARCHIVO,
                   codigos, dnis, nombres, asuntos, fechas)
    datos = cargar_seguro(cargar_datos, RUTA_ARCHIVO, ([], [], [], [], []))
"""

import os


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Pide un numero entero y repite hasta que sea valido.

    Si se escriben letras, simbolos, decimales o se deja vacio, muestra
    'Opcion invalida' y vuelve a preguntar (el programa no se cierra).
    """
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("Opcion invalida: escribe solo numeros enteros.")
            continue
        if minimo is not None and numero < minimo:
            print(f"Opcion invalida: el minimo permitido es {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f"Opcion invalida: el maximo permitido es {maximo}.")
            continue
        return numero


def asegurar_carpeta(ruta):
    """Crea la carpeta de la ruta si no existe (ej. 'datos/' en 'datos/a.txt')."""
    carpeta = os.path.dirname(ruta)
    if carpeta != "":
        os.makedirs(carpeta, exist_ok=True)


def guardar_seguro(funcion_guardar, ruta, *listas):
    """Ejecuta funcion_guardar(ruta, *listas) protegida con try/except.

    Devuelve True si se guardo y False si hubo un error (el error se
    explica con un mensaje; el programa NO se cierra).
    """
    try:
        asegurar_carpeta(ruta)
        funcion_guardar(ruta, *listas)
        return True
    except FileNotFoundError:
        print(f"Error: no se encontro la ruta '{ruta}'.")
    except PermissionError:
        print(f"Error: no hay permisos para escribir en '{ruta}'.")
    except IOError as error:  # en Python 3, IOError es lo mismo que OSError
        print(f"Error de archivo al guardar: {error}")
    except Exception as error:
        print(f"Error inesperado al guardar: {error}")
    return False


def cargar_seguro(funcion_cargar, ruta, por_defecto=None):
    """Ejecuta funcion_cargar(ruta) protegida con try/except.

    Devuelve lo que devuelva funcion_cargar, o 'por_defecto' si falla.
    """
    try:
        return funcion_cargar(ruta)
    except FileNotFoundError:
        print(f"Aviso: el archivo '{ruta}' no existe todavia. Se inicia sin datos.")
    except PermissionError:
        print(f"Error: no hay permisos para leer '{ruta}'.")
    except UnicodeDecodeError:
        print(f"Error: '{ruta}' esta danado o no es un archivo de texto UTF-8.")
    except IOError as error:
        print(f"Error de archivo al cargar: {error}")
    except Exception as error:
        print(f"Error inesperado al cargar: {error}")
    return por_defecto


def ejecutar_seguro(funcion):
    """Ejecuta funcion() y evita que el programa termine con trazas largas.

    - Ctrl+C         -> KeyboardInterrupt
    - Ctrl+Z + Enter -> EOFError (Windows)  /  Ctrl+D (Linux, Mac)
    - Errores de archivo y cualquier otro error imprevisto
    """
    try:
        funcion()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. Hasta luego.")
    except EOFError:
        print("\n\nSe cerro la entrada de datos. Hasta luego.")
    except IOError as error:
        print(f"\nError de archivo: {error}. Revisa la ruta y los permisos.")
    except Exception as error:
        print(f"\nOcurrio un error inesperado: {error}")
