import os 
#la extension de cada array es 7 porque representa a cada persona 

codigos = ["00001A", "00001B", "00001C", "00001D", "00001E", "00001F", "00001G"]
dnis    = ["72345678", "48123987", "70589123", "45678912", "71234569", 
             "49876543", "73456789"]

nombres = ["Juan Perez", "María Fernandez", "Luis Sera", "Ana Cordero", "Carlos Manrique", 
                 "Rosa Bartra","Jorge Chabelo"]
asuntos = ["No me carga","No me viene","No me llama","No me paga","No me cancela","No contesta","No me entrega"]

fechas  = ["01/10/2026", "02/10/2026","03/10/2026","04/10/2026","05/10/2026","06/10/2026","07/10/2026" ]
archivo =""
ruta = r"D:\Nueva carpeta\miArchivo.txt"
def guardar_datos(ruta, codigos, dnis, nombres, asuntos, fechas):
    # TODO (YNUMA): escribir un expediente por linea, separado por "|"

    archivo = open ("miArchivo.txt", "w")
    with open (ruta, "w", encoding="utf-8") as archivo: 
        archivo.write("el delegampi, el terror de las enfermeras\n")

        for i in range(0, len (fechas)):
            archivo.write(codigos[i] + "|" + dnis[i] + "|" + nombres[i] + "|" + asuntos[i] + "|" + fechas[i] + "\n")

    #archivo.Close()
    # Ej: EXP-001|12345678|Ana Perez|Solicitud|10/10/2026


#guardar_datos(ruta, codigos, dnis, nombres, asuntos, fechas)


def cargar_datos(ruta):
    #TODO (YNUMA): leer el archivo y devolver las 5 listas en este orden:
   
    #print ("lalalalalalalal")

    try:
     with open (ruta, "r", encoding="utf-8") as archivo:

          
            #print("yayayayayayaya")
            return codigos, dnis, nombres, fechas , asuntos 


    except FileNotFoundError: 
        
        return [],[],[],[],[]


print (cargar_datos(ruta))
"""
if __name__ == "__main__":
    ruta = "datos/prueba.txt"
    guardar_datos(ruta, ["EXP-001"], ["12345678"], ["Ana Perez"],
                  ["Solicitud"], ["10/10/2026"])
    print(cargar_datos(ruta))"""
