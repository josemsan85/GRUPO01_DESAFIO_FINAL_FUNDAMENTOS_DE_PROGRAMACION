# Datos ficticios de prueba para la mesa de partes digital.


lista_dni = ["72345678", "48123987", "70589123", "45678912", "71234569",
             "49876543", "73456789", "46789123", "74567890", "44332211",
             "75123456", "42987654", "76543210", "43219876", "47654321",
             "72987341", "40871234", "77123450", "41562387", "78234561"]

lista_nombres = ["Juan Carlos", "María Alejandra", "Luis Alberto", "Ana Sofía", "Carlos Enrique",
                 "Rosa Elena", "Jorge Luis", "Lucía Beatriz", "Miguel Ángel", "Carmen Rosa",
                 "Pedro Pablo", "Sofía Valentina", "Diego Armando", "Patricia Milagros", "Víctor Hugo",
                 "Elena Marisol", "Raúl Fernando", "Daniela Alexandra", "Héctor Manuel", "Gabriela Fernanda"]

lista_ape_paterno = ["Pérez", "Quispe", "Sánchez", "Huamán", "Ramos",
                     "Flores", "Castillo", "Vargas", "Romero", "Díaz",
                     "Mamani", "Gutiérrez", "Cárdenas", "Rivera", "Chávez",
                     "Muñoz", "Ccama", "Peña", "Zamora", "Rodríguez"]

lista_ape_materno = ["Gómez", "Rojas", "Torres", "Castro", "Mendoza",
                     "Medina", "Paredes", "Silva", "Espinoza", "Morales",
                     "Huanca", "Ríos", "Salazar", "Ponce", "Ortiz",
                     "Vega", "Cruz", "Aguilar", "Delgado", "Navarro"]

lista_correo = ["juan.perez@gmail.com", "maria.quispe@outlook.com", "luis.sanchez@yahoo.com",
                "ana.huaman@hotmail.com", "carlos.ramos@gmail.com", "rosa.flores@outlook.com",
                "jorge.castillo@gmail.com", "lucia.vargas@gmail.com", "miguel.romero@gmail.com",
                "carmen.diaz@gmail.com", "pedro.mamani@gmail.com", "sofia.gutierrez@hotmail.com",
                "diego.cardenas@outlook.com", "patricia.rivera@yahoo.com", "victor.chavez@gmail.com",
                "elena.munoz@outlook.com", "raul.ccama@gmail.com", "daniela.pena@hotmail.com",
                "hector.zamora@yahoo.com", "gabriela.rodriguez@gmail.com"]

# Asuntos variados (minimo 5 caracteres y sin el simbolo '|')
lista_asuntos = ["Solicitud de licencia", "Reclamo por demora en la atención",
                 "Solicitud de constancia de estudios", "Pedido de copia de expediente",
                 "Queja por mala atención", "Solicitud de duplicado de carné",
                 "Reclamo de nota", "Solicitud de reincorporación",
                 "Pedido de cambio de turno", "Solicitud de beca",
                 "Constancia de matrícula", "Reclamo por cobro indebido",
                 "Solicitud de retiro de curso", "Pedido de certificado de notas",
                 "Solicitud de traslado interno", "Consulta sobre trámite de grado",
                 "Solicitud de prórroga de pago", "Reclamo por error en boleta",
                 "Solicitud de reserva de matrícula", "Pedido de información de horarios"]

# Fechas en formato DD/MM/AAAA
lista_fechas = ["01/09/2026", "04/09/2026", "09/09/2026", "15/09/2026", "22/09/2026",
                "28/09/2026", "02/10/2026", "05/10/2026", "07/10/2026", "12/10/2026",
                "14/10/2026", "19/10/2026", "21/10/2026", "26/10/2026", "28/10/2026",
                "30/10/2026", "03/11/2026", "04/11/2026", "05/11/2026", "06/11/2026"]


if __name__ == "__main__":
    # Comprobacion rapida de este modulo (python Simulacion_de_datos_ficticios_lista.py)
    from validaciones import validar_dni, validar_nombre, validar_asunto, validar_fecha

    listas = [lista_dni, lista_nombres, lista_ape_paterno, lista_ape_materno,
              lista_correo, lista_asuntos, lista_fechas]

    # Todas las listas deben tener el mismo largo
    alineadas = all(len(lista) == len(lista_dni) for lista in listas)
    print("Registros:", len(lista_dni))
    print("Listas alineadas:", alineadas)
    print("DNI sin repetir:", len(set(lista_dni)) == len(lista_dni))

    errores = 0
    for i in range(len(lista_dni)):
        nombre_completo = lista_nombres[i] + " " + lista_ape_paterno[i] + " " + lista_ape_materno[i]
        if not (validar_dni(lista_dni[i])
                and validar_nombre(nombre_completo)
                and validar_asunto(lista_asuntos[i])
                and validar_fecha(lista_fechas[i])):
            print("Registro con problemas:", i + 1)
            errores += 1
    print("Registros con errores:", errores)
