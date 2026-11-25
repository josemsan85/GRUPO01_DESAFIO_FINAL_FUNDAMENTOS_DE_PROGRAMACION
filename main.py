import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from validaciones import (
    validar_dni,
    validar_nombre,
    validar_asunto,
    validar_fecha,
)
from registro import registrar_expediente
from busqueda_orden import (
    buscar_por_codigo,
    ordenar_por_codigo,
    buscar_coincidencias,
    ordenar_por_fecha,
)
from archivos import guardar_datos, cargar_datos

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(CARPETA, "datos", "expedientes.txt")

# Datos del archivo (se cargan una vez al abrir)
codigos, dnis, nombres, asuntos, fechas = cargar_datos(RUTA_ARCHIVO)

# Colores sobrios en escala de grises
COLOR_FONDO = "#e9ecef"
COLOR_PANEL = "#f8f9fa"
COLOR_TEXTO = "#212529"
COLOR_BOTON = "#dee2e6"

ventana = tk.Tk()
ventana.title("Mesa de partes virtual")
ventana.config(bg=COLOR_FONDO)
ventana.minsize(420, 320)
ventana.geometry("560x390")

# Manejo de frames
registroFrame = tk.Frame(ventana, bg=COLOR_PANEL, padx=12, pady=12)
buscarExpFrame = tk.Frame(ventana, bg=COLOR_PANEL, padx=12, pady=12)
buscarExpFrame2 = tk.Frame(ventana, bg=COLOR_PANEL, padx=12, pady=12)
ordenarCodigoFrame = tk.Frame(ventana, bg=COLOR_PANEL, padx=12, pady=12)
listarExpedientesFrame = tk.Frame(ventana, bg=COLOR_PANEL, padx=12, pady=12)
guardaDatosFrame = tk.Frame(ventana, bg=COLOR_PANEL, padx=12, pady=12)
framesOpci = tk.Frame(ventana, bg=COLOR_PANEL, padx=15, pady=15)

todosLosFrames = [
    registroFrame,
    buscarExpFrame,
    buscarExpFrame2,
    ordenarCodigoFrame,
    listarExpedientesFrame,
    guardaDatosFrame,
    framesOpci,
]


def apagon():
    """Oculta todos los frames antes de mostrar la pantalla elegida."""
    for frame in todosLosFrames:
        frame.grid_remove()


def mostrar_menu_principal():
    """Regresa al menú principal con el Combobox."""
    apagon()
    framesOpci.grid(row=0, column=0, padx=20, pady=20)


# ---------- Registrar expediente ----------
def labelsMuestra(frame_destino):
    campos = ["DNI", "Nombres Completos", "Asunto", "Fecha"]
    for idx, texto in enumerate(campos):
        tk.Label(
            frame_destino, text=texto, bg=COLOR_PANEL, fg=COLOR_TEXTO
        ).grid(row=idx, column=0, sticky="w", padx=5, pady=5)


tk.Label(
    registroFrame,
    text="Registrar nuevo expediente",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 10, "bold"),
).grid(row=0, column=0, columnspan=2, pady=(0, 8))

# Desplazamos los campos 1 fila hacia abajo por el título
tk.Label(registroFrame, text="DNI", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(
    row=1, column=0, sticky="w", padx=5, pady=4
)
entradaDNI = tk.Entry(registroFrame, width=28)
entradaDNI.grid(row=1, column=1, padx=5, pady=4)

tk.Label(registroFrame, text="Nombres Completos", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(
    row=2, column=0, sticky="w", padx=5, pady=4
)
entradaNombre = tk.Entry(registroFrame, width=28)
entradaNombre.grid(row=2, column=1, padx=5, pady=4)

tk.Label(registroFrame, text="Asunto", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(
    row=3, column=0, sticky="w", padx=5, pady=4
)
entradaAsuntos = tk.Entry(registroFrame, width=28)
entradaAsuntos.grid(row=3, column=1, padx=5, pady=4)

tk.Label(registroFrame, text="Fecha (DD/MM/AAAA)", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(
    row=4, column=0, sticky="w", padx=5, pady=4
)
entradaFecha = tk.Entry(registroFrame, width=28)
entradaFecha.grid(row=4, column=1, padx=5, pady=4)


def guardarRegistro():
    """Valida los 4 campos, registra el expediente y lo guarda en el archivo."""
    dni = entradaDNI.get().strip()
    nombre = entradaNombre.get().strip()
    asunto = entradaAsuntos.get().strip()
    fecha = entradaFecha.get().strip()

    if not validar_dni(dni):
        messagebox.showerror("DNI invalido", "El DNI debe tener exactamente 8 digitos.")
        return
    if not validar_nombre(nombre):
        messagebox.showerror("Nombre invalido", "Solo letras y espacios, minimo 3 caracteres.")
        return
    if not validar_asunto(asunto):
        messagebox.showerror("Asunto invalido", "Minimo 5 caracteres y sin el simbolo '|'.")
        return
    if not validar_fecha(fecha):
        messagebox.showerror("Fecha invalida", "Usa el formato DD/MM/AAAA con una fecha real.")
        return

    codigo = registrar_expediente(
        codigos, dnis, nombres, asuntos, fechas, dni, nombre, asunto, fecha
    )
    guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)

    for caja in (entradaDNI, entradaNombre, entradaAsuntos, entradaFecha):
        caja.delete(0, tk.END)
    messagebox.showinfo("Registro exitoso", "Expediente registrado con codigo " + codigo)


tk.Button(
    registroFrame, text="Registrar", bg=COLOR_BOTON, command=guardarRegistro
).grid(row=5, column=0, padx=5, pady=10)
tk.Button(
    registroFrame, text="Atras", bg=COLOR_BOTON, command=mostrar_menu_principal
).grid(row=5, column=1, padx=5, pady=10)
# ----------------- Fin Registro expediente -----------------


# ----------------- Buscar Expediente -----------------
tk.Label(
    buscarExpFrame,
    text="Buscar expediente por codigo",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 10, "bold"),
).grid(row=0, column=0, columnspan=2, pady=(0, 8))

tk.Label(
    buscarExpFrame, text="Codigo (ej. EXP-001):", bg=COLOR_PANEL, fg=COLOR_TEXTO
).grid(row=1, column=0, padx=5, pady=5)
entradaBusquedaExpediente = tk.Entry(buscarExpFrame, width=20)
entradaBusquedaExpediente.grid(row=1, column=1, padx=5, pady=5)


def buscar_y_mostrar():
    """Busca el expediente ingresado y muestra su detalle."""
    codigo_buscado = entradaBusquedaExpediente.get().strip().upper()
    if not codigo_buscado:
        messagebox.showwarning("Campo vacio", "Ingresa un codigo de expediente.")
        return

    if len(codigos) == 0:
        messagebox.showinfo("Sin registros", "No hay expedientes registrados.")
        return

    pos = buscar_por_codigo(codigos, codigo_buscado)
    if pos == -1:
        messagebox.showerror("No encontrado", f"No se encontro el expediente {codigo_buscado}.")
        return

    resultadoExp.config(text=codigos[pos])
    resultadoDNI.config(text=dnis[pos])
    resultadoNombre.config(text=nombres[pos])
    resultadoAsunto.config(text=asuntos[pos])
    resultadoFecha.config(text=fechas[pos])

    apagon()
    buscarExpFrame2.grid(row=0, column=0, padx=20, pady=20)


def volver_a_buscar():
    apagon()
    buscarExpFrame.grid(row=0, column=0, padx=20, pady=20)


tk.Button(
    buscarExpFrame, text="Buscar", bg=COLOR_BOTON, command=buscar_y_mostrar
).grid(row=2, column=0, padx=5, pady=10)
tk.Button(
    buscarExpFrame, text="Atras", bg=COLOR_BOTON, command=mostrar_menu_principal
).grid(row=2, column=1, padx=5, pady=10)

# Frame de resultados de búsqueda
tk.Label(
    buscarExpFrame2,
    text="Detalle del expediente",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 10, "bold"),
).grid(row=0, column=0, columnspan=2, pady=(0, 8))

for fila, etiqueta in enumerate(
    ["Codigo:", "DNI:", "Nombre:", "Asunto:", "Fecha:"], start=1
):
    tk.Label(buscarExpFrame2, text=etiqueta, bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(
        row=fila, column=0, sticky="w", padx=5, pady=3
    )

resultadoExp = tk.Label(buscarExpFrame2, text="-", bg=COLOR_PANEL, fg=COLOR_TEXTO)
resultadoExp.grid(row=1, column=1, sticky="w", padx=10, pady=3)

resultadoDNI = tk.Label(buscarExpFrame2, text="-", bg=COLOR_PANEL, fg=COLOR_TEXTO)
resultadoDNI.grid(row=2, column=1, sticky="w", padx=10, pady=3)

resultadoNombre = tk.Label(buscarExpFrame2, text="-", bg=COLOR_PANEL, fg=COLOR_TEXTO)
resultadoNombre.grid(row=3, column=1, sticky="w", padx=10, pady=3)

resultadoAsunto = tk.Label(buscarExpFrame2, text="-", bg=COLOR_PANEL, fg=COLOR_TEXTO)
resultadoAsunto.grid(row=4, column=1, sticky="w", padx=10, pady=3)

resultadoFecha = tk.Label(buscarExpFrame2, text="-", bg=COLOR_PANEL, fg=COLOR_TEXTO)
resultadoFecha.grid(row=5, column=1, sticky="w", padx=10, pady=3)

tk.Button(
    buscarExpFrame2, text="Nueva busqueda", bg=COLOR_BOTON, command=volver_a_buscar
).grid(row=6, column=0, padx=5, pady=10)
tk.Button(
    buscarExpFrame2, text="Menu", bg=COLOR_BOTON, command=mostrar_menu_principal
).grid(row=6, column=1, padx=5, pady=10)
# ----------------- Fin de busqueda expediente -----------------


# ----------------- Ordenar por Codigo -----------------
tk.Label(
    ordenarCodigoFrame,
    text="Ordenar expedientes por codigo",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 10, "bold"),
).grid(row=0, column=0, columnspan=2, pady=(0, 8))

lbl_estado_orden = tk.Label(
    ordenarCodigoFrame,
    text="Ordena de menor a mayor manteniendo los datos alineados.",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
)
lbl_estado_orden.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


def accion_ordenar_codigo():
    """Ordena los expedientes por código en memoria."""
    if len(codigos) == 0:
        lbl_estado_orden.config(text="No hay expedientes registrados para ordenar.")
        messagebox.showinfo("Sin registros", "No hay expedientes registrados.")
        return

    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas)
    lbl_estado_orden.config(
        text=f"Se ordenaron {len(codigos)} expediente(s) por codigo."
    )
    messagebox.showinfo(
        "Ordenado", "Expedientes ordenados por codigo (de menor a mayor)."
    )


tk.Button(
    ordenarCodigoFrame, text="Ordenar ahora", bg=COLOR_BOTON, command=accion_ordenar_codigo
).grid(row=2, column=0, padx=5, pady=10)
tk.Button(
    ordenarCodigoFrame, text="Atras", bg=COLOR_BOTON, command=mostrar_menu_principal
).grid(row=2, column=1, padx=5, pady=10)
# ----------------- Fin Ordenar por Codigo -----------------


# ----------------- Listar Expedientes -----------------
tk.Label(
    listarExpedientesFrame,
    text="Lista de expedientes",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 10, "bold"),
).grid(row=0, column=0, columnspan=2, pady=(0, 6))

columnas_exp = ("Codigo", "DNI", "Nombre", "Asunto", "Fecha")
tabla_expedientes = ttk.Treeview(
    listarExpedientesFrame, columns=columnas_exp, show="headings", height=8
)
anchos_col = {
    "Codigo": 80,
    "DNI": 80,
    "Nombre": 125,
    "Asunto": 140,
    "Fecha": 85,
}
for col in columnas_exp:
    tabla_expedientes.heading(col, text=col)
    tabla_expedientes.column(col, width=anchos_col[col], anchor="center")

tabla_expedientes.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

lbl_total_exp = tk.Label(
    listarExpedientesFrame, text="Total: 0 expediente(s)", bg=COLOR_PANEL, fg=COLOR_TEXTO
)
lbl_total_exp.grid(row=2, column=0, columnspan=2, padx=5, pady=3)


def mostrar_lista_expedientes():
    """Refresca el Treeview con las listas actuales en memoria."""
    for item in tabla_expedientes.get_children():
        tabla_expedientes.delete(item)
    for i in range(len(codigos)):
        tabla_expedientes.insert(
            "",
            tk.END,
            values=(codigos[i], dnis[i], nombres[i], asuntos[i], fechas[i]),
        )
    lbl_total_exp.config(text=f"Total: {len(codigos)} expediente(s)")


tk.Button(
    listarExpedientesFrame,
    text="Actualizar",
    bg=COLOR_BOTON,
    command=mostrar_lista_expedientes,
).grid(row=3, column=0, padx=5, pady=8)
tk.Button(
    listarExpedientesFrame, text="Atras", bg=COLOR_BOTON, command=mostrar_menu_principal
).grid(row=3, column=1, padx=5, pady=8)
# ----------------- Fin de listas expedientes -----------------


# ----------------- Guardar Datos -----------------
tk.Label(
    guardaDatosFrame,
    text="Guardar expedientes en archivo",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 10, "bold"),
).grid(row=0, column=0, columnspan=2, pady=(0, 8))

lbl_guardado_info = tk.Label(
    guardaDatosFrame, text="", bg=COLOR_PANEL, fg=COLOR_TEXTO
)
lbl_guardado_info.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


def guardar_datos_gui():
    """Persiste los datos actuales en expedientes.txt."""
    guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)
    lbl_guardado_info.config(text=f"Guardados: {len(codigos)} expediente(s)")
    messagebox.showinfo("Guardar datos", "Datos guardados correctamente.")


tk.Button(
    guardaDatosFrame, text="Guardar", bg=COLOR_BOTON, command=guardar_datos_gui
).grid(row=2, column=0, padx=5, pady=10)
tk.Button(
    guardaDatosFrame, text="Atras", bg=COLOR_BOTON, command=mostrar_menu_principal
).grid(row=2, column=1, padx=5, pady=10)
# ----------------- Fin Guardar Datos -----------------


# ----------------- Menú principal (Combobox) -----------------
tk.Label(
    framesOpci,
    text="Selecciona una opcion:",
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 10, "bold"),
).grid(row=0, column=0, pady=(0, 8))

opciones = tk.StringVar()
opcionesDesplegadas = ttk.Combobox(
    framesOpci,
    textvariable=opciones,
    width=28,
    values=[
        "Registrar Expedientes",
        "Buscar Expediente",
        "Ordenar Expediente por codigo",
        "Listar expedientes",
        "Guardar datos",
        "Salida",
    ],
    state="readonly",
)
opcionesDesplegadas.current(0)
opcionesDesplegadas.grid(row=1, column=0, pady=8)


def salir_aplicacion():
    confirmar = messagebox.askyesno(
        "Salir", "Deseas guardar los cambios antes de salir?"
    )
    if confirmar:
        guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)
    ventana.destroy()


def muestraElEstado():
    valorRegistro = opcionesDesplegadas.get()
    apagon()

    if valorRegistro == "Registrar Expedientes":
        registroFrame.grid(row=0, column=0, padx=20, pady=20)
    elif valorRegistro == "Buscar Expediente":
        buscarExpFrame.grid(row=0, column=0, padx=20, pady=20)
    elif valorRegistro == "Ordenar Expediente por codigo":
        lbl_estado_orden.config(
            text="Ordena de menor a mayor manteniendo los datos alineados."
        )
        ordenarCodigoFrame.grid(row=0, column=0, padx=20, pady=20)
    elif valorRegistro == "Listar expedientes":
        mostrar_lista_expedientes()
        listarExpedientesFrame.grid(row=0, column=0, padx=20, pady=20)
    elif valorRegistro == "Guardar datos":
        lbl_guardado_info.config(text=f"Expedientes listos: {len(codigos)}")
        guardaDatosFrame.grid(row=0, column=0, padx=20, pady=20)
    elif valorRegistro == "Salida":
        salir_aplicacion()


botoncito = tk.Button(
    framesOpci, text="Realizar", bg=COLOR_BOTON, width=14, command=muestraElEstado
)
botoncito.grid(row=2, column=0, pady=10)

mostrar_menu_principal()
ventana.mainloop()


# ----------------- Funciones de consola (opcionales) -----------------
def mostrar_menu():
    print("\n===== MESA DE PARTES DIGITAL =====")
    print("1. Registrar expediente")
    print("2. Buscar expediente por codigo")
    print("3. Ordenar expedientes por codigo")
    print("4. Listas expedientes")
    print("5. Guardar datos")
    print("6. Buscar por coincidencia")
    print("7. Ordenar expedientes por fecha")
    print("0. Salir")


def pausar():
    input("\nPresiona ENTER para continuar...")


def pedir_dato(mensaje, funcion_validar, mensaje_error):
    while True:
        valor = input(mensaje).strip()
        if funcion_validar(valor):
            return valor
        print("  -> " + mensaje_error)


def cortar(texto, ancho):
    if len(texto) > ancho:
        return texto[: ancho - 3] + "..."
    return texto


def opcion_registrar(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l):
    print("\n--- Registrar expediente ---")
    dni = pedir_dato(
        "DNI (8 digitos): ",
        validar_dni,
        "El DNI debe tener exactamente 8 digitos.",
    )
    nombre = pedir_dato(
        "Nombre completo: ",
        validar_nombre,
        "Solo letras y espacios, minimo 3 caracteres.",
    )
    asunto = pedir_dato(
        "Asunto: ",
        validar_asunto,
        "Minimo 5 caracteres y sin el simbolo '|'.",
    )
    fecha = pedir_dato(
        "Fecha (DD/MM/AAAA): ",
        validar_fecha,
        "Usa el formato DD/MM/AAAA con una fecha real.",
    )
    codigo = registrar_expediente(
        codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l, dni, nombre, asunto, fecha
    )
    print("\nExpediente registrado con codigo:", codigo)


def opcion_buscar(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l):
    print("\n--- Buscar expediente ---")
    if len(codigos_l) == 0:
        print("No hay expedientes registrados.")
        return
    codigo = input("Codigo a buscar (ej. EXP-001): ").strip().upper()
    pos = buscar_por_codigo(codigos_l, codigo)
    if pos == -1:
        print("No se encontro el expediente", codigo)
    else:
        print("\nExpediente encontrado:")
        print("  Codigo:", codigos_l[pos])
        print("  DNI:   ", dnis_l[pos])
        print("  Nombre:", nombres_l[pos])
        print("  Asunto:", asuntos_l[pos])
        print("  Fecha: ", fechas_l[pos])


def opcion_ordenar(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l):
    print("\n--- Ordenar expedientes ---")
    if len(codigos_l) == 0:
        print("No hay expedientes registrados.")
        return
    ordenar_por_codigo(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l)
    print("Expedientes ordenados por codigo (de menor a mayor).")


def opcion_listar(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l):
    print("\n--- Lista de expedientes ---")
    if len(codigos_l) == 0:
        print("No hay expedientes registrados.")
        return
    print(
        "\n"
        + "CODIGO".ljust(10)
        + "DNI".ljust(10)
        + "NOMBRE".ljust(22)
        + "ASUNTO".ljust(28)
        + "FECHA"
    )
    print("-" * 80)
    for i in range(len(codigos_l)):
        print(
            codigos_l[i].ljust(10)
            + dnis_l[i].ljust(10)
            + cortar(nombres_l[i], 20).ljust(22)
            + cortar(asuntos_l[i], 26).ljust(28)
            + fechas_l[i]
        )
    print("\nTotal:", len(codigos_l), "expediente(s)")


def opcion_buscar_coincidencias(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l):
    print("\n--- Buscar por coincidencia ---")
    if len(codigos_l) == 0:
        print("No hay expedientes registrados.")
        return
    print("Buscar en: 1. Codigo  2. DNI  3. Nombre  4. Asunto  5. Fecha")
    campo = input("Elige el campo: ").strip()
    if campo == "1":
        lista = codigos_l
    elif campo == "2":
        lista = dnis_l
    elif campo == "3":
        lista = nombres_l
    elif campo == "4":
        lista = asuntos_l
    elif campo == "5":
        lista = fechas_l
        print("(En fecha puedes buscar por mes y anio, ej. 09/2026)")
    else:
        print("Campo invalido.")
        return
    texto = input("Texto a buscar: ").strip()
    posiciones = buscar_coincidencias(lista, texto)
    if len(posiciones) == 0:
        print("No se encontraron coincidencias.")
        return
    print(
        "\n"
        + "CODIGO".ljust(10)
        + "DNI".ljust(10)
        + "NOMBRE".ljust(22)
        + "ASUNTO".ljust(28)
        + "FECHA"
    )
    print("-" * 80)
    for i in posiciones:
        print(
            codigos_l[i].ljust(10)
            + dnis_l[i].ljust(10)
            + cortar(nombres_l[i], 20).ljust(22)
            + cortar(asuntos_l[i], 26).ljust(28)
            + fechas_l[i]
        )
    print("\nTotal:", len(posiciones), "coincidencia(s)")


def opcion_ordenar_fecha(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l):
    print("\n--- Ordenar expedientes por fecha ---")
    if len(codigos_l) == 0:
        print("No hay expedientes registrados.")
        return
    ordenar_por_fecha(codigos_l, dnis_l, nombres_l, asuntos_l, fechas_l)
    print("Expedientes ordenados por fecha (del mas antiguo al mas reciente).")


def main():
    c_l, d_l, n_l, a_l, f_l = cargar_datos(RUTA_ARCHIVO)
    print("Bienvenido a la Mesa de Partes Digital")
    print("Expedientes cargados:", len(c_l))
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
            opcion_registrar(c_l, d_l, n_l, a_l, f_l)
        elif opcion == 2:
            opcion_buscar(c_l, d_l, n_l, a_l, f_l)
        elif opcion == 3:
            opcion_ordenar(c_l, d_l, n_l, a_l, f_l)
        elif opcion == 4:
            opcion_listar(c_l, d_l, n_l, a_l, f_l)
        elif opcion == 5:
            guardar_datos(RUTA_ARCHIVO, c_l, d_l, n_l, a_l, f_l)
            print("Datos guardados.")
        elif opcion == 6:
            opcion_buscar_coincidencias(c_l, d_l, n_l, a_l, f_l)
        elif opcion == 7:
            opcion_ordenar_fecha(c_l, d_l, n_l, a_l, f_l)
        elif opcion == 0:
            respuesta = input("Seguro que deseas salir? (s/n): ").strip().lower()
            if respuesta == "s":
                guardar_datos(RUTA_ARCHIVO, c_l, d_l, n_l, a_l, f_l)
                print("Datos guardados. Hasta luego.")
            else:
                opcion = -1
        else:
            print("Opcion invalida. Elige una opcion del menu.")
        if opcion != 0:
            pausar()


if __name__ == "__main__":
    main()