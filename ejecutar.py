"""HU-07: lanzador seguro. Ejecuta el programa SIN modificar main.py.

Uso:
    python ejecutar.py            -> Mesa de Partes (main.py)
    python ejecutar.py tramites   -> Gestion de tramites (HU-02)

Si la persona presiona Ctrl+C, cierra la entrada o falla un archivo,
se muestra un mensaje limpio en lugar de una traza larga de errores.
"""

import sys
from manejo_errores import ejecutar_seguro


def iniciar_mesa_de_partes():
    import main  # se importa aqui para que cualquier error quede protegido
    main.main()


def iniciar_tramites():
    from tramites import menu_tramites
    menu_tramites()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "tramites":
        ejecutar_seguro(iniciar_tramites)
    else:
        ejecutar_seguro(iniciar_mesa_de_partes)
