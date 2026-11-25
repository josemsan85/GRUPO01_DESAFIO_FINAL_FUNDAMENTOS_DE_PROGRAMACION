import os
#comiteado a las 22:34
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from enum import Enum
#from datos datos datos datos
from validaciones import (validar_dni, validar_nombre,
                          validar_asunto, validar_fecha)
from registro import registrar_expediente
from busqueda_orden import buscar_por_codigo, ordenar_por_codigo
from busqueda_orden import buscar_coincidencias, ordenar_por_fecha
from archivos import guardar_datos, cargar_datos 
#nuevo Commitsssss
#otro nuevoComiits 22:22
##otr nuievo comits 22:29
#<<<<<<< HEAD

#nuevo inicio de nuevo 
#12345678899 1234567890


#RUTA_ARCHIVO = "datos/expedientes.txt"

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "datos", "expedientes.txt")

#datos del archivo (secargan una vez al abrir)
codigos, dnis, nombres, asuntos, fechas = cargar_datos(RUTA_ARCHIVO)

class Estados(Enum):
    nombre =1
    dni =2
    estado = 3

#tiposAtaque = Estados.escudo

#if tiposAtaque == Estados.escudo:
print("estas con un escudo")
ventana = tk.Tk()
ventana.title ("Mesa de partes virtual")
ventana.config(bg="yellow")
ventana.minsize (200,200)
ventana.maxsize(400,400)
ventana.geometry("350x350")

#tk.Label(ventana, )

#manejo de frames de expedientes

todosLosFrames = []

registroFrame = tk.Frame(ventana)

buscarExpFrame = tk.Frame(ventana)

buscarExpFrame2 = tk.Frame(ventana)
ordenarCodigoFrame = tk.Frame(ventana)
listarExpedientesFrame = tk.Frame(ventana)
guardaDatosFrame = tk.Frame(ventana)

"""
todosLosFrames.append(registroFrame, buscarExpFrame, 
                      ordenarCodigoFrame,listarExpedientesFrame, 
                      guardaDatosFrame)"""

todosLosFrames.append(registroFrame)
todosLosFrames.append(buscarExpFrame)
todosLosFrames.append(ordenarCodigoFrame)
todosLosFrames.append(listarExpedientesFrame)
todosLosFrames.append(guardaDatosFrame)

def apagon():
    for abc in todosLosFrames:
        abc.grid_remove() 
#----------Registrar expediente----------

def labelsMuestra(registroFrame):
    tk.Label(registroFrame, text="DNI").grid (row=0, column=0, padx = 5, pady=5)
    tk.Label(registroFrame, text="Nombres Completos").grid (row=1, column=0, padx = 5, pady=5)
    tk.Label(registroFrame, text="Asuntos ").grid (row=2, column=0, padx = 5, pady=5)
    tk.Label(registroFrame, text="Fecha").grid (row=3, column=0, padx = 5, pady=5)


labelsMuestra(registroFrame)
#tk.Label(registroFrame, text="DNI").grid (row=0, column=0, padx = 5, pady=5)
entradaDNI = tk.Entry(registroFrame)
entradaDNI.grid(row=0, column=1, padx = 5, pady=5)


entradaNombre = tk.Entry(registroFrame)
entradaNombre.grid(row=1, column=1, padx = 5, pady=5)


entradaAsuntos = tk.Entry(registroFrame)
entradaAsuntos.grid(row=2, column=1, padx = 5, pady=5)


entradaFecha = tk.Entry(registroFrame)
entradaFecha.grid(row=3, column=1, padx = 5, pady=5)


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

    codigo = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                                  dni, nombre, asunto, fecha)
    guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)

    for caja in (entradaDNI, entradaNombre, entradaAsuntos, entradaFecha):
        caja.delete(0, tk.END)
    messagebox.showinfo("Registro exitoso", "Expediente registrado con codigo " + codigo)


def consultax ():

    guardarRegistro()
    buscarExpFrame.grid_remove()
    registroFrame.grid(row=5, column=0, columnspan=2, pady=10)
    #btnRegreso = tk.Button()

btnBusqueda = tk.Button(registroFrame, text="Registrar", command=consultax)
btnBusqueda.grid(row=4, column=0, padx=5, pady=5)

def regresox():
      registroFrame.grid_remove()
      framesOpci.grid(row=5, column=0, columnspan=2, pady=10)

btnAtras = tk.Button(registroFrame, text="Atras", command=regresox)
btnAtras.grid(row=4, column=1, padx=5, pady=5)


#-----------------FinRegistro expediente-----------

#-----------------Buscar Expediente--------
tk.Label(buscarExpFrame , text="Busca Por Expediente").grid (row=0, column=0, padx = 5, pady=5)
entradaBusquedaExpediente = tk.Entry(buscarExpFrame)
entradaBusquedaExpediente.grid(row=0, column=1, padx = 5, pady=5)

#el primero es la carga
def opcibus(codigoFramenput, codigos, dnis, nombres, asuntos, fechas):

     
    
    print("\n--- Buscar expediente ---")
    if len(codigos) == 0:
        #messagebox.showerror("Asunto invalido", "No se ha encontrado expediente'|'.")
        #return
        print("No hay expedientes registrados.")
        return
    #codigoxxxx = input("Codigo a buscar (ej. EXP-001): ").strip().upper()
    pos = buscar_por_codigo(codigos, codigoFramenput)
    if pos == -1:
        messagebox.showerror("Asunto invalido", "No se ha encontrado expediente'|'.")
        return
        print("No se encontro el expediente", codigoFramenput)
    else:
        print("\nExpediente encontrado:")
        print("  Codigo:", codigos[pos])
        resultadoExp.config(text=codigos[pos])
       # resultadoExp.config(text=codigos[pos])

        print("  DNI:   ", dnis[pos])
        resultadoDNI.config(text=dnis[pos])
        #resultadoDNI.config(text=dnis[pos])

        print("  Nombre:", nombres[pos])
        resultadoNombre.config(text = nombres[pos])

        print("  Asunto:", asuntos[pos])
        resultadoAsunto.config(text = asuntos[pos])


        print("  Fecha: ", fechas[pos])
        resultadoFecha.config(text=fechas[pos])


def busqueExpMetod():
    #codigos, dnis, nombres, asuntos, fechas = cargar_datos(RUTA_ARCHIVO)
    expi = entradaBusquedaExpediente.get().strip()
    opcibus(expi,codigos, dnis, nombres, asuntos, fechas)
    
def busquedaButton ():
    busqueExpMetod()
    buscarExpFrame.grid_remove()
    buscarExpFrame2.grid(row=0, column=1, padx = 5, pady=5)
   # opcion_buscar(entradaBusquedaExpediente) 

def regresoPrincipal():
      buscarExpFrame.grid_remove()
      framesOpci.grid(row=0, column=1, columnspan=2, pady=10)

btnAtras = tk.Button(buscarExpFrame, text="Atras", command=regresoPrincipal)
btnAtras.grid(row=2, column=0, padx=5, pady=5)


btnBusqueda = tk.Button(buscarExpFrame, text="Busqueda", command=busquedaButton)
btnBusqueda.grid(row=2, column=1, padx = 15, pady=5)


labelsMuestra(buscarExpFrame2)

resultadoDNI = tk.Label(buscarExpFrame2, text="")
resultadoDNI.config(text="vacio")
resultadoDNI.grid(row=0, column=1, padx = 15, pady=5)

resultadoNombre = tk.Label(buscarExpFrame2, text="")
resultadoNombre.config(text="vacio")
resultadoNombre.grid(row=1, column=1, padx = 15, pady=5)

resultadoAsunto = tk.Label(buscarExpFrame2, text="")
resultadoAsunto.config(text="vacio")
resultadoAsunto.grid(row=2, column=1, padx = 15, pady=5)

resultadoFecha = tk.Label(buscarExpFrame2, text="")
resultadoFecha.config(text="vacio")
resultadoFecha.grid(row=3, column=1, padx = 15, pady=5)

resultadoExp = tk.Label(buscarExpFrame2, text="")
resultadoExp.config(text="vacio")
resultadoExp.grid(row=4, column=0, padx = 15, pady=5)

def retrocede ():
    buscarExpFrame2.grid_remove()
    buscarExpFrame.grid(row=5, column=1, padx=5, pady=5)


btnAtras = tk.Button(buscarExpFrame2, text="Atras", command=retrocede)
btnAtras.grid(row=4, column=1, padx = 15, pady=5)

#----------------Fin de busquea expediente---------

#-----------------Listar Expdeientes-------------
tk.Label(listarExpedientesFrame, text="Lista de expedientes").grid(
    row=0, column=0, columnspan=2, padx=5, pady=5
)

columnas_exp = ("Codigo", "DNI", "Nombre", "Asunto", "Fecha")
tabla_expedientes = ttk.Treeview(
    listarExpedientesFrame, columns=columnas_exp, show="headings", height=6
)
for col in columnas_exp:
    tabla_expedientes.heading(col, text=col)
    tabla_expedientes.column(col, width=65)
tabla_expedientes.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

lbl_total_exp = tk.Label(listarExpedientesFrame, text="Total: 0")
lbl_total_exp.grid(row=2, column=0, columnspan=2, padx=5, pady=2)


def mostrar_lista_expedientes():
    for item in tabla_expedientes.get_children():
        tabla_expedientes.delete(item)
    for i in range(len(codigos)):
        tabla_expedientes.insert(
            "",
            tk.END,
            values=(codigos[i], dnis[i], nombres[i], asuntos[i], fechas[i]),
        )
    lbl_total_exp.config(text=f"Total: {len(codigos)}")


def regresar_desde_listar():
    listarExpedientesFrame.grid_remove()
    framesOpci.grid(row=2, column=0, columnspan=2, pady=5)


tk.Button(listarExpedientesFrame, text="Actualizar", command=mostrar_lista_expedientes).grid(
    row=3, column=0, padx=5, pady=5
)
tk.Button(listarExpedientesFrame, text="Atras", command=regresar_desde_listar).grid(
    row=3, column=1, padx=5, pady=5
)
#-----------------Fin de listas expedientes------

#-----------------Guardar Datos------------------
tk.Label(guardaDatosFrame, text="Guardar expedientes en archivo").grid(
    row=0, column=0, columnspan=2, padx=5, pady=5
)
lbl_guardado_info = tk.Label(guardaDatosFrame, text="")
lbl_guardado_info.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


def guardar_datos_gui():
    guardar_datos(RUTA_ARCHIVO, codigos, dnis, nombres, asuntos, fechas)
    lbl_guardado_info.config(text=f"Guardados: {len(codigos)} expediente(s)")
    messagebox.showinfo("Guardar datos", "Datos guardados correctamente.")


def regresar_desde_guardar():
    guardaDatosFrame.grid_remove()
    framesOpci.grid(row=2, column=0, columnspan=2, pady=5)


tk.Button(guardaDatosFrame, text="Guardar", command=guardar_datos_gui).grid(
    row=2, column=0, padx=5, pady=5
)
tk.Button(guardaDatosFrame, text="Atras", command=regresar_desde_guardar).grid(
    row=2, column=1, padx=5, pady=5
)
#-----------------Fin Guardar Datos--------------

framesOpci = tk.Frame()
framesOpci.grid(row=2, column=0, columnspan=2, pady=5)

#despliega las opciones usando el comboBox
opciones= tk.StringVar()
opcionesDesplegadas = ttk.Combobox(framesOpci, textvariable=opciones, 
                                   values= ["Registrar Expedientes", "Buscar Expediente", 
                                            "Ordenar Expediente por codigo", "Listar expedientes",
                                            "Guardar datos", "Salida"], state="readonly")

opcionesDesplegadas.current(0)
opcionesDesplegadas.grid(row=0, column=0, pady=10)

opcionesDesplegadas.current(0)

def muestraElEstado():

    #a = int (entrada1.get())
    #b = int (entrada2.get())

    valorRegistro = opcionesDesplegadas.get()
    
    
    if (valorRegistro == "Registrar Expedientes"):
    # framesOpci.pack_forget()
     
     registroFrame.grid(row=5, column=0, columnspan=2, pady=10)
     framesOpci.grid_remove()
     #framesOpci.pack_forget()
     
    elif(valorRegistro == "Buscar Expediente"):
     buscarExpFrame.grid(row=5, column=0, columnspan=2, pady=10)
     framesOpci.grid_remove()

     print ("a registrar")

    elif(valorRegistro == "Listar expedientes"):
     mostrar_lista_expedientes()
     listarExpedientesFrame.grid(row=5, column=0, columnspan=2, pady=10)
     framesOpci.grid_remove()

    elif(valorRegistro == "Guardar datos"):
     lbl_guardado_info.config(text=f"Expedientes listos: {len(codigos)}")
     guardaDatosFrame.grid(row=5, column=0, columnspan=2, pady=10)
     framesOpci.grid_remove()
  
    #resultadoOpera.config(f"resultado: {resultado}")
    #resultadoOpera.config(text=f"resultado: {resultado}")
    
botoncito = tk.Button(framesOpci, text="Realizar", command=muestraElEstado)

botoncito.grid(row=1, column=0, pady=10)
"""
resultadoOpera = ttk.Label(framesOpci, text="resultado")
resultadoOpera.grid(row=2, column=0, pady=10)
"""
ventana.mainloop()
#>>>>>>> main
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
    #Pide un dato hasta que sea valido y muestra que se esperaba"""
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

    #el parametro codigo es que ya viene precargado y se tiene que 
    #comparar con el codigoQue es inpput
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
       # resultadoExp.config(text=codigos[pos])

        print("  DNI:   ", dnis[pos])
        resultadoDNI.config(text="DNI22")
        #resultadoDNI.config(text=dnis[pos])

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
def opcion_buscar_coincidencias(codigos, dnis, nombres, asuntos, fechas):
    print("\n--- Buscar por coincidencia ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    print("Buscar en: 1. Codigo  2. DNI  3. Nombre  4. Asunto  5. Fecha")
    campo = input("Elige el campo: ").strip()
    if campo == "1":
        lista = codigos
    elif campo == "2":
        lista = dnis
    elif campo == "3":
        lista = nombres
    elif campo == "4":
        lista = asuntos
    elif campo == "5":
        lista = fechas
        print("(En fecha puedes buscar por mes y anio, ej. 09/2026)")
    else:
        print("Campo invalido.")
        return
    texto = input("Texto a buscar: ").strip()
    posiciones = buscar_coincidencias(lista, texto)
    if len(posiciones) == 0:
        print("No se encontraron coincidencias.")
        return
    print("\n" + "CODIGO".ljust(10) + "DNI".ljust(10) + "NOMBRE".ljust(22)
          + "ASUNTO".ljust(28) + "FECHA")
    print("-" * 80)
    for i in posiciones:
        print(codigos[i].ljust(10) + dnis[i].ljust(10)
              + cortar(nombres[i], 20).ljust(22)
              + cortar(asuntos[i], 26).ljust(28) + fechas[i])
    print("\nTotal:", len(posiciones), "coincidencia(s)")
def opcion_ordenar_fecha(codigos, dnis, nombres, asuntos, fechas):
    print("\n--- Ordenar expedientes por fecha ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    ordenar_por_fecha(codigos, dnis, nombres, asuntos, fechas)
    print("Expedientes ordenados por fecha (del mas antiguo al mas reciente).")
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
        elif opcion == 6:
            opcion_buscar_coincidencias(codigos, dnis, nombres, asuntos, fechas)
        elif opcion == 7:
            opcion_ordenar_fecha(codigos, dnis, nombres, asuntos, fechas)
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