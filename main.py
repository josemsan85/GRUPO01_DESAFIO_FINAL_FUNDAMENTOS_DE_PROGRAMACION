import os
#comiteado a las 22:34
import tkinter as tk
from tkinter import ttk 
from enum import Enum
#from datos datos datos datos
from validaciones import (validar_dni, validar_nombre,
                          validar_asunto, validar_fecha)
from registro import registrar_expediente, ESTADOS
from busqueda_orden import buscar_por_codigo, ordenar_por_codigo
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


def consultax ():

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

def busquedaButton ():
    buscarExpFrame.grid_remove()
    buscarExpFrame2.grid(row=0, column=1, padx = 5, pady=5)


btnBusqueda = tk.Button(buscarExpFrame, text="Busqueda", command=busquedaButton)
btnBusqueda.grid(row=2, column=1, padx = 15, pady=5)


labelsMuestra(buscarExpFrame2)

resultadoDNI = tk.Label(buscarExpFrame2, text="")
resultadoDNI.config(text="DNI")
resultadoDNI.grid(row=0, column=1, padx = 15, pady=5)

resultadoNombre = tk.Label(buscarExpFrame2, text="")
resultadoNombre.config(text="Nombre")
resultadoNombre.grid(row=1, column=1, padx = 15, pady=5)

resultadoAsunto = tk.Label(buscarExpFrame2, text="")
resultadoAsunto.config(text="Asunto")
resultadoAsunto.grid(row=2, column=1, padx = 15, pady=5)

resultadoFecha = tk.Label(buscarExpFrame2, text="")
resultadoFecha.config(text="Fecha")
resultadoFecha.grid(row=3, column=1, padx = 15, pady=5)

def retrocede ():
    buscarExpFrame2.grid_remove()
    buscarExpFrame.grid(row=4, column=1, padx=5, pady=5)


btnAtras = tk.Button(buscarExpFrame2, text="Atras", command=retrocede)
btnAtras.grid(row=4, column=1, padx = 15, pady=5)




#----------------Fin de busquea expediente---------

#-----------------Listar Expdeientes-------------
#-----------------Fin de listas expedientes------

framesOpci = tk.Frame()
framesOpci.grid(row=2, column=0, columnspan=2, pady=5)

#despliega las opciones usando el comboBox
opciones= tk.StringVar()
opcionesDesplegadas = ttk.Combobox(framesOpci, textvariable=opciones, 
                                   values= ["Registrar Expedientes", "Buscar Expediente", 
                                            "Ordenar Expediente por codigo", "Listar expedientes",
                                            "Guardar datos", "Sumar"], state="readonly")

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
# Mensajes que explican que se esperaba en cada dato (HU-07)
ERROR_DNI = "El DNI debe tener exactamente 8 digitos."
ERROR_NOMBRE = "Solo letras y espacios, minimo 3 caracteres."
ERROR_ASUNTO = "Minimo 5 caracteres y sin el simbolo '|'."
ERROR_FECHA = "Usa el formato DD/MM/AAAA con una fecha real."


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


def pedir_dato(mensaje, funcion_validar, mensaje_error):
    """Pide un dato hasta que sea valido y explica que se esperaba."""
    while True:
        valor = input(mensaje).strip()
        if funcion_validar(valor):
            return valor
        print("Dato invalido. " + mensaje_error)


def pedir_dato_o_mantener(mensaje, funcion_validar, valor_actual, mensaje_error):
    """Igual que pedir_dato, pero si presionan ENTER se queda el valor actual."""
    while True:
        valor = input(f"{mensaje} [{valor_actual}]: ").strip()
        if valor == "":
            return valor_actual
        if funcion_validar(valor):
            return valor
        print("Dato invalido. " + mensaje_error)


def cortar(texto, ancho):
    """Recorta el texto con '...' si es mas largo que el ancho de la columna."""
    if len(texto) > ancho:
        return texto[:ancho - 3] + "..."
    return texto


def pedir_posicion(codigos, mensaje):
    """Pide un codigo y devuelve su posicion en la lista (-1 si no existe)."""
    codigo = input(mensaje).strip().upper()
    pos = buscar_por_codigo(codigos, codigo)
    if pos == -1:
        print(f"No se encontro el expediente {codigo}.")
    return pos


# ---------------------------------------------------------------- HU-02: CRUD

def opcion_registrar(codigos, dnis, nombres, asuntos, fechas, estados):
    print("\n--- Registrar expediente ---")
    dni = pedir_dato("DNI (8 digitos): ", validar_dni, ERROR_DNI)
    nombre = pedir_dato("Nombre completo: ", validar_nombre, ERROR_NOMBRE)
    asunto = pedir_dato("Asunto: ", validar_asunto, ERROR_ASUNTO)
    fecha = pedir_dato("Fecha (DD/MM/AAAA): ", validar_fecha, ERROR_FECHA)
    codigo = registrar_expediente(codigos, dnis, nombres, asuntos, fechas,
                                  estados, dni, nombre, asunto, fecha)
    print(f"\nExpediente registrado con codigo: {codigo} (estado: Pendiente)")


def opcion_buscar(codigos, dnis, nombres, asuntos, fechas, estados):
    print("\n--- Buscar expediente ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    pos = pedir_posicion(codigos, "Codigo a buscar (ej. EXP-001): ")
    if pos != -1:
        print("\nExpediente encontrado:")
        print(f"  Codigo: {codigos[pos]}")
        print(f"  DNI:    {dnis[pos]}")
        print(f"  Nombre: {nombres[pos]}")
        print(f"  Asunto: {asuntos[pos]}")
        print(f"  Fecha:  {fechas[pos]}")
        print(f"  Estado: {estados[pos]}")


def opcion_ordenar(codigos, dnis, nombres, asuntos, fechas, estados):
    print("\n--- Ordenar expedientes ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    ordenar_por_codigo(codigos, dnis, nombres, asuntos, fechas, estados)
    print("Expedientes ordenados por codigo (de menor a mayor).")


def opcion_listar(codigos, dnis, nombres, asuntos, fechas, estados):
    """Muestra todos los expedientes en una tabla usando f-strings."""
    print("\n--- Lista de expedientes ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    print()
    print(f"{'CODIGO':<10}{'DNI':<10}{'NOMBRE':<22}{'ASUNTO':<28}"
          f"{'FECHA':<12}{'ESTADO'}")
    print("-" * 92)
    for i in range(len(codigos)):
        # cortar() acorta los textos largos para que la tabla no se descuadre
        print(f"{codigos[i]:<10}{dnis[i]:<10}{cortar(nombres[i], 20):<22}"
              f"{cortar(asuntos[i], 26):<28}{fechas[i]:<12}{estados[i]}")
    print(f"\nTotal: {len(codigos)} expediente(s)")


def opcion_editar(codigos, dnis, nombres, asuntos, fechas, estados):
    """Busca un expediente por su codigo y cambia sus datos."""
    print("\n--- Editar expediente ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    pos = pedir_posicion(codigos, "Codigo del expediente a editar: ")
    if pos == -1:
        return
    print("Presiona ENTER sin escribir nada para conservar el valor actual.")
    dnis[pos] = pedir_dato_o_mantener("DNI (8 digitos)", validar_dni,
                                      dnis[pos], ERROR_DNI)
    nombres[pos] = pedir_dato_o_mantener("Nombre completo", validar_nombre,
                                         nombres[pos], ERROR_NOMBRE)
    asuntos[pos] = pedir_dato_o_mantener("Asunto", validar_asunto,
                                         asuntos[pos], ERROR_ASUNTO)
    fechas[pos] = pedir_dato_o_mantener("Fecha (DD/MM/AAAA)", validar_fecha,
                                        fechas[pos], ERROR_FECHA)
    print(f"Expediente {codigos[pos]} actualizado.")


def opcion_cambiar_estado(codigos, dnis, nombres, asuntos, fechas, estados):
    """Cambia el estado de un expediente (Pendiente, En proceso, ...)."""
    print("\n--- Cambiar estado ---")
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
