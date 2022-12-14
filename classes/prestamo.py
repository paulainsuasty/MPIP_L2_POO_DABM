# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:39:36 2022
@author: Paula Insuasty
"""
from classes.equipo import *
from tabulate import tabulate
from main import *

global datos_prestamos
global p
global prestamos_registrados
global equipos_registrados
global datos
prestamos_registrados = []
equipos_registrados = []

class Prestamo:
    file_prestamo = "database/prestamos_registrados.csv"
    file_prestamo_modificado = "database/prestamos_registrados_modificados.csv"

    def __init__(self,nombre_estudiante, carnet, nombre_equipo_prestamo, referencia_prestamo, fecha_prestamo, fecha_entrega):
        self.nombre_estudiante = nombre_estudiante
        self.carnet = carnet
        self.nombre_equipo_prestamo = nombre_equipo_prestamo
        self.referencia_prestamo = referencia_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega

    def ver_prestamos(self):
        header = ["Nombre del estudiante", "Numero de carnet", "Nombre del equipo en prestamo", "Numero de referencia del equipo", "Fecha de prestamo", "Fecha de entrega"]
        datos = [[self.nombre_estudiante, self.carnet, self.nombre_equipo_prestamo, self.referencia_prestamo, self.fecha_prestamo, self.fecha_entrega]]
        print(tabulate(datos, header, tablefmt = "grid"))
    def save_prestamos(self):
        f_prestamo = open(self.file_prestamo, "a")
        linea = ";".join([self.nombre_estudiante, self.carnet, self.nombre_equipo_prestamo, self.referencia_prestamo, self.fecha_prestamo, self.fecha_entrega])
        f_prestamo.write(linea + "\n")
        f_prestamo.close()
    def consulta_prestamos(self):
        archivo = open("prestamos_registrados.csv", "r")
        lineas = archivo.readlines()
        header = ["Nombre del estudiante", "Numero de carnet", "Nombre del equipo en prestamo", "Numero de referencia del equipo", "Fecha de prestamo", "Fecha de entrega"]
        datos = []
        datos.append(lineas)
        for l in (lineas):
            # print(l)
            l = l.replace("\n", "")
            l = l.split(";")
            datos.append(l)
        print(tabulate(datos, header, tablefmt="grid"))
# *********************************************************************************************************************
def consultar_equipo():
    print("Opci??n para verificar si el equipo est?? registrado")
    #print("Consulta de equipos registrados:")
    nombre_equipo = input("Ingresa el nombre del equipo: ")
    archivo = open("database/equipos_registrados.csv", "r")
    lineas = archivo.readlines()
    datos = []
    #datos.append(lineas)
    for l in (lineas):
        # print(l)
        l = l.replace("\n", "")
        l = l.split(";")
        datos.append(l)
    datos_nuevos = []
    q = 0
    hay_equipo = 0
    equipo_existe = 0
    print("datos es: ", datos)

    for q in range(len(datos)):
        # print("Para un q de: ", q, " en 1 se tienen datos: ", datos[q][1])
        if datos[q][0] == nombre_equipo:
            equipo_existe = equipo_existe + 1
    if equipo_existe >= 1:
        print("El equipo existe y est?? disponible en el laboratorio")
    else:
        print("El equipo no est?? registrado en el inventario del laboratorio")
        #main()
# *********************************************************************************************************************
def verificando_disponibilidad():
    print("Verificando la cantidad de un equipo:")
    nombre_equipo = input("Ingresa el nombre del equipo:")
    archivo = open("database/equipos_registrados.csv", "r")
    lineas = archivo.readlines()
    datos = []
    datos.append(lineas)
    for l in (lineas):
        # print(l)
        l = l.replace("\n", "")
        l = l.split(";")
        datos.append(l)
    datos_nuevos = []
    q = 0
    hay_equipo = 0
    equipo_existe = 0
    for q in range(len(datos)):
        # print("Para un q de: ", q, " en 1 se tienen datos: ", datos[q][1])
        if datos[q][0] == nombre_equipo:
            #print("DATO ACTUAL DE CANTIDAD ES:", q,  int(datos[q][4]))
            #print("Tipo de datos es: ", type(datos[q][4]))
            if int(datos[q][4]) >= 1:
                print("Si se puede hacer el prestamo!")
                print("La cantidad actual del equipo es de: ", datos[q][4])
            else:
                print("cantidad actual ser??a:", datos[q][4], "por tanto, no se puede realizar el prestamo")
                main()
# *********************************************************************************************************************
def actualizando_disponibilidad():
    nombre_equipo = input("Ingresa el nombre del equipo para actualizar la cantidad del equipo: ")
    #archivo = open("database/equipos_registrados.csv", "r")
    archivo = open("database/equipos_registrados_modificados.csv", "r")
    lineas = archivo.readlines()
    datos = []
    datos.append(lineas)
    for l in (lineas):
        # print(l)
        l = l.replace("\n", "")
        l = l.split(";")
        datos.append(l)
    q = 0
    lista_equipos = get_all_equipos()
    for q in range(len(datos)):
        if datos[q][0] == nombre_equipo:
            print("Dato actual de cantidad es:", int(datos[q][4]))
            datos[q][4]= (int(datos[q][4])-1)
            print("Nuevo dato de cantidad es:", datos[q][4])
            #print("Equipo encontrado")
            pos = 0
            i = 0
            for e in lista_equipos:
                datos = e.split(";")
                datos[4] = int(datos[4]) - 1
                #print("El val de cantidad es: ", datos[4], "y el tipo es: ", type(datos[4]))
                datos[4] = str(datos[4])
                lista_equipos[pos] = ";".join((datos))
                print("Revisando nueva version de lista de equipos: ", lista_equipos[pos])
                print("Informaci??n actualizada!")
                pos = pos + 1
                i = i + 1

            lista_prestamos = get_all_prestamos()
            # a = open("database/prestamos_registrados_modificados.csv", "w")
            # for e in lista_prestamos:
            #     a.write(p)
            # a.close()
            #
            # b = open("database/equipos_registrados_modificados.csv", "w")
            # for e in lista_equipos:
            #     b.write(p)
            # b.close()

            #c = open("database/prestamos_pr3_registrados_modificados.csv", "w")
            # for e in lista_equipos:
            #     for i in range (len(lista_equipos)):
            #         c.write(lista_prestamos[i])
            #         i = i+1
            # c.close()

            print("Viendo la lista actualizada con cantidad de todos los equipos: ", lista_equipos)
            #save_all_equipos_modificados(lista_equipos)

    lista_prestamos = get_all_prestamos()
    a = open("database/equipos_registrados_modificados.csv", "w")
    for e in lista_equipos:
        a.write(e) # lista_equipos
    a.close()
    #save_all_equipos(lista_prestamos)
    save_all_equipos() #lista_equipos
# *********************************************************************************************************************
def crear_prestamos():
    print("Primero se debe consultar si el equipo existe")
    consultar_equipo()
    print("Ahora se debe consultar la disponibilidad del equipo")
    verificando_disponibilidad()
    print("Se verific?? correctamente la informaci??n!")

    print("Ahora por favor diligencia la siguiente informaci??n para crear el prestamo")
    #print("Informaci??n para crear prestamo a un estudiante:")
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    carnet = input("Ingrese el numero del carnet: ")
    nombre_equipo_prestamo = input("Ingrese el nombre del equipo en prestamo")
    referencia_prestamo = input("Ingrese el numero de referencia del equipo en prestamo")
    fecha_prestamo = input("Ingrese la fecha del prestamo: ")
    fecha_entrega = input("Ingrese la fecha de entrega: ")

    #print("Finalmente, se debe actualizar disponibilidad del equipo:")
    #actualizando_disponibilidad()

    p = Prestamo(nombre_estudiante, carnet, nombre_equipo_prestamo, referencia_prestamo, fecha_prestamo, fecha_entrega)
    return p

    lista_prestamos = get_all_prestamos()
    save_all_prestamos(lista_prestamos)
    #save_all_prestamos()

#***********************************************************************************************************************
#                               !!! INICIO DE REPITIENDO PARA SAVE ALL Y GET ALL EQUIPOS!!!
#***********************************************************************************************************************
def save_all_equipos():
    #a = open("database/equipos_registrados.csv", "w")
    a = open("database/equipos_registrados.csv", "a")
    for e in equipos_registrados:
        a.write(e)
    a.close()
#***********************************************************************************************************************
def get_all_equipos():
    a = open("database/equipos_registrados.csv", "r")
    datos= a.readlines()
    return datos
# ***********************************************************************************************************************
#                               !!! FIN DE REPITIENDO PARA SAVE ALL Y GET ALL EQUIPOS!!!
# ***********************************************************************************************************************
def save_all_prestamos():
    #a = open("database/prestamos_registrados.csv")
    a = open("database/prestamos_registrados.csv","a")
    #a = open("database/prestamos_registrados_modificaciones.csv", "w")
    for p in prestamos_registrados:
        a.write(p)
    a.close()
# **********************************************************************************************************************
#def save_all_prestamos_modificados():
    #a = open("database/prestamos_registrados.csv")
    #a = open("database/prestamos_registrados.csv","a")
    # a = open("database/AA_prestamos_registrados_modificaciones.csv", "a")
    #
    # a.write(datos_prestamos)
    # #for p in prestamos_registrados:
    # #    a.write(datos_prestamos)
    # a.close()
# **********************************************************************************************************************
def get_all_prestamos():
    a = open("database/prestamos_registrados.csv", "r")
    datos = a.readlines()
    header = ["Nombre del estudiante", "Numero de carnet", "Nombre del equipo en prestamo",
              "Numero de referencia del equipo", "Fecha de prestamo", "Fecha de entrega"]
    print(tabulate(datos, header, tablefmt="grid"))
    return datos
# **********************************************************************************************************************

def consultar_prestamos_por_estudiante():
    print("Opci??n para verificar tus prestamos:")
    #print("Consulta de equipos registrados:")
    numero_carnet = input("Ingresa el numero del carnet del estudiante:")
    #print("PENDIENTE esta parte")
    archivo = open("database/prestamos_registrados.csv", "r")
    lineas = archivo.readlines()
    #header = ["nombre", "proveedor", "ciclo", "cantidad", "fecha ultimo mantenimiento"]
    # datos = [[self.nombre, self.referencia, self.cantidad, self.proveedor, self.ciclo, self.fum]]
    datos = []
    datos.append(lineas)
    for l in (lineas):
        # print(l)
        l = l.replace("\n", "")
        l = l.split(";")
        datos.append(l)
    #print("Cuanto es len datos?", len(datos))
    #print("Viendo los nuevos datos despues del split: ", datos)
    datos_nuevos = []
    q = 0
    tiene_prestamo = 0
    equipo_en_prestamo = 0
    for q in range (len(datos)):
        #print("Para un q de: ", q, " en 1 se tienen datos: ", datos[q][1])
        if datos[q][1] == numero_carnet:
            tiene_prestamo = tiene_prestamo +1

    if tiene_prestamo >= 1:
        print("Tiene un total de: ", tiene_prestamo, "prestamos registrados")
        for q in range(len(datos)):
            if datos[q][1] == numero_carnet:
                equipo_en_prestamo = datos[q][2]
                referencia_equipo_en_prestamo = datos[q][3]
                fecha_entrega_equipo_en_prestamo = datos[q][5]
                #print("**")
                print("** Un equipo que tiene es prestamo es: **")
                print("Tiene en prestamo el equipo: ", equipo_en_prestamo)
                print("La referencia del equipo es: ", referencia_equipo_en_prestamo)
                print("La fecha de entrega del equipo en prestamo es: ", fecha_entrega_equipo_en_prestamo)
                #print("**")
    else:
        print("No tiene equipos en prestamo")

    #header = ["Nombre del estudiante", "Numero de carnet", "Nombre del equipo en prestamo","Numero de referencia del equipo", "Fecha de prestamo", "Fecha de entrega"]

##### **** PRUEBA 2 ****
def registro_entrega():
    print("Opci??n para registrar la entrega de un equipo: ")
    numero_carnet = input("Ingresa el numero de carnet del estudiante: ")
    nombre_equipo = input("Ingresa el nombre del equipo para actualizar la cantidad del equipo:")
    archivo = open("database/equipos_registrados.csv", "r")
    archivo_prestamos = open("database/prestamos_registrados.csv", "r")
    lineas = archivo.readlines()
    lineas_prestamos = archivo_prestamos.readlines()
    datos = []
    datos_prestamos = []
    # datos.append(lineas)
    # datos_prestamos.append(lineas_prestamos)
    ### ****
    lista_equipos = get_all_equipos()
    pos = 0
    i = 0
    for l in (lineas):
        # print(l)
        l = l.replace("\n", "")
        l = l.split(";")
        datos.append(l)
    #
    for l_prestamos in (lineas_prestamos):
        l_prestamos = l_prestamos.replace("\n", "")
        l_prestamos = l_prestamos.split(";")
        datos_prestamos.append(l_prestamos)
    # print("Los datos en datos prestamos en y son: ", datos_prestamos)
    y = 0
    for y in range(len(datos_prestamos)):
        #print("ronda en y: ", y)
        # SI HAY UN PRESTAMO CONESE NUM CARNET:
        #print("presentando datos en y 1: ", datos_prestamos[y][1])   # DESCOMENTAR PARA VER LOS NUM DE CARNETS!
        if (datos_prestamos[y][1] == numero_carnet):
            print("El estudiante con numero de carnet: ", numero_carnet, "Si tiene prestamos en el sistema")
            for q in range(len(datos)):
                if (datos_prestamos[y][1] == numero_carnet) and datos[q][0] == nombre_equipo:
                    print("La cantidad actual de equipos ", nombre_equipo, "en el sistema en este momento son: ", datos[q][4])
                    #print("NO SE ENCUENTRA NUM CARNET Y NOMBRE DE EQUIPO COMO COINCIDENCIA DE PRESTAMO")
                    #exit()
            for e in lista_equipos:
                datos = e.split(";")
                datos[4] = int(datos[4]) + 1
                #print("El nuevo valor de cantidad para el equipo: ", nombre_equipo, "es: ", datos[4])
                datos[4] = str(datos[4])
                lista_equipos[pos] = ";".join((datos))
                #print("Revisando nueva version de lista de equipos: ", lista_equipos[pos])
                #print("DESPUES DE ELIMINARLO: Informaci??n actualizada!")
                pos = pos + 1
                i = i + 1
            #print("Confirmando")
            print("***")
            print("Visualizando datos previo a intentar eliminar: ")
            print(datos_prestamos)
            print("** ELIMINANDO INFORMACI??N **")
            datos_prestamos.remove(datos_prestamos[y])
            #print("Visualizando datos de prestamos despu??s de eliminar el prestamo")
            print("Nueva informaci??n de prestamos: ")
            print(datos_prestamos)
            print("La informaci??n ha sido actualizada exitosamente!, se ha eliminado la informaci??n relacionada a este prestamo")
        #else:
            #print("El equipo no se encuentra en prestamo o el estudiante no tiene prestamos registrados")
            #print("El estudiante con el numero de carnet: ", datos_prestamos[y][1] , "no tiene prestamos registrados")
            # print("Por favor registra el equipo o verifica si escribiste el nombre correo y vuelve a intentarlo")
            # exit()
            #print("FIN DE IFs Viendo la lista actualizada con cantidad de todos los equipos: ", lista_equipos)
        y = y + 1
    print("******************************************************")
    print("Datos de equipos en prestamo son: ")
    print(datos_prestamos)
    print("******************************************************")
    #save_all_prestamos_modificados()
    print("Viendo lista de equipos: ")
    print(lista_equipos)
    #print("Viendo lista de prestamos: ", lista_prestamos)
    print("******************************************************")
    print("El nuevo datos de prestamo es:")
    print(datos_prestamos)
    print("******************************************************")
    #print("ronda en y abajo: ", y)
    #save_all_prestamos()
    #save_all_prestamos_modificados(datos_prestamos)

    a = open("database/prestamos_registrados_modificaciones.csv", "w")
    for i in range(len(datos_prestamos)):
        print("presentando los datos actuales asociadas a los prestamos son: ")
        print(" ' ",i, " ' ", datos_prestamos[i])
        # nuevo_orden = datos_prestamos[i][0]
        my_string = ";".join(datos_prestamos[i])
        # print("Para",  my_string)
        a.write(my_string)
        #a.write(my_string+ "\n")  # LAS MUESTRA EN UNA SOLA LINEA, PERO SI LO ELIMINA!! (en csv en AA_prestamos)
        # a.write(datos_prestamos[i])
        # a.close()
        i = i + 1
    # print("FIN REGISTRO ENTREGA")
    w = 0
    regis = 0
    no_regis = 0
    for w in range (len(datos_prestamos)):
        if datos_prestamos[w][1] == numero_carnet:
            regis = regis +1
            exit()
        else:
            no_regis = no_regis +1

    if regis >=1:
        print("El prestamo sigue vigente para el usuario con carnet: ", numero_carnet)
    if no_regis >= 1:
        print("El prestamo ya no est?? registrado para el usuario con num de carnet: ", numero_carnet)
        print("!!")

    #exit()

# def registro_entrega():
#     print("Opci??n para registrar la entrega de un equipo: ")
#     numero_carnet =input("Ingresa el numero de carnet del estudiante: ")
#     nombre_equipo = input("Ingresa el nombre del equipo para actualizar la cantidad del equipo:")
#     archivo = open("database/equipos_registrados.csv", "r")
#     archivo_prestamos = open("database/prestamos_registrados.csv", "r")
#     lineas = archivo.readlines()
#     lineas_prestamos = archivo_prestamos.readlines()
#     datos = []
#     datos_prestamos = []
#     #datos.append(lineas)
#     #datos_prestamos.append(lineas_prestamos)
#     ### ****
#     lista_equipos = get_all_equipos()
#     pos = 0
#     i = 0
#
#     for l in (lineas):
#         # print(l)
#         l = l.replace("\n", "")
#         l = l.split(";")
#         datos.append(l)
#     #
#     for l_prestamos in (lineas_prestamos):
#         l_prestamos = l_prestamos.replace("\n", "")
#         l_prestamos = l_prestamos.split(";")
#         datos_prestamos.append(l_prestamos)
#
#     #print("Los datos en datos prestamos en y son: ", datos_prestamos)
#
#     y = 0
#     for y in range (len(datos_prestamos)):
#         print("ronda en y: ", y)
#         # SI HAY UN PRESTAMO CONESE NUM CARNET:
#         print("presentando datos en y 1: ",  datos_prestamos[y][1])
#         if datos_prestamos[y][1] == numero_carnet:
#             print("El estudiante con numero de carnet: ", numero_carnet, "Si tiene prestamos en el sistema")
#             for q in range(len(datos)):
#                 if datos[q][0] == nombre_equipo:
#                     print("La cantidad actual de equipos:", nombre_equipo, "en el sistema en este momento son: ", datos[q][4])
#                     for e in lista_equipos:
#                         datos = e.split(";")
#                         datos[4] = int(datos[4]) + 1
#                         print("El nuevo valor de cantidad para el equipo: ", nombre_equipo , "es: ", datos[4])
#                         datos[4] = str(datos[4])
#                         lista_equipos[pos] = ";".join((datos))
#                         print("Revisando nueva version de lista de equipos: ", lista_equipos[pos])
#
#                         print("Previo a intentar eliminar: ", datos_prestamos)
#                         datos_prestamos.remove(datos_prestamos[y])
#                         print("AHORA VIENDO DATOS PRESTAMOS,DESPUES DE ELIMINAR EL NUM DE CARNET:")
#                         print(datos_prestamos)
#                         print("DESPUES DE ELIMINARLO: Informaci??n actualizada!")
#
#                         pos = pos + 1
#                         i = i + 1
#
#                 else:
#                     print("El equipo no se encuentra en prestamo")
#                     print("Por favor registra el equipo o verifica si escribiste el nombre correo y vuelve a intentarlo")
#                     # exit()
#
#             print("FIN DE IFs Viendo la lista actualizada con cantidad de todos los equipos: ", lista_equipos)
#
#         else:
#             print("El estudiante con el numero de carnet: ", numero_carnet , "no tiene prestamos registrados")
#
#
#     print("El final y nuevo datos de prestamo es:", datos_prestamos)
#     print("ronda en y abajo: ", y)
#     y = y+1
#
#     main()

# ***********************************************************************************************************************
# ************************************* INTENTOS  PREVIOS ***************************************************************
# ***********************************************************************************************************************
    ### ****
    #print("A ORIGINALES DE DATOS PRESTAMOS: ", datos_prestamos)
    #print("A ORIGINALES DE DATOS:", datos)

    #pos = 0

    # print("len de datos prestamos: ", len(datos_prestamos))
    # print("len de datos: ", len(datos))
    #
    # print("DATOS DESPUES DE SPLIT:", datos)
    # print("DATOS PRESTAMOS DESPUES DE SPLIT: ", datos_prestamos)
    #
    # q = 0
    # y = 0
    # lista_equipos = get_all_equipos()
    #
    # print("con intento en e de lista equipos")
    # print("Aumentando en 1 la cantidad del equipo:")
    #
    # for e in lista_equipos:
    #     datos = e.split(";")
    #     datos[4] = int(datos[4]) +1
    #     print("El val de cantidad es: ", datos[4], "y el tipo es: ", type(datos[4]))
    #     datos[4] = str(datos[4])
    #     lista_equipos[pos] = ";".join((datos))
    #     print("Revisando nueva version de lista de equipos: ", lista_equipos[pos])
    #     print("Informaci??n actualizada!")
    #     pos = pos + 1
    #
    # print("fin intento en e de lista equipos")


    ## ** P2:

# print("**Intentando con codigo previo:**")
# lista_equipos = get_all_equipos()
# pos = 0
# i = 0
# for e in lista_equipos:
#     print("* INCIO DE RONDA *")
#     if nombre_equipo in e:
#         print("Equipo encontrado")
#         datos = e.split(";")
#         datos[4] = int(datos[4])-1
#         print("El val de cantidad es: ", datos[4], "y el tipo es: ", type(datos[4]))
#         datos[4] = str(datos[4])
#         lista_equipos[pos] = ";".join((datos))
#         print("Revisando nueva version de lista de equipos: ", lista_equipos[pos])
#         print("Informaci??n actualizada!")
#     else:
#         print("El equipo no se encuentra registrado")
#         print("Por favor registra el equipo o verifica si escribiste el nombre correo y vuelve a intentarlo")
#         exit()
#     pos = pos + 1
#     i = i + 1
#     print("* FIN DE RONDA*")
#     print(" ")
# print("Viendo la lista actualizada con cantidad de todos los equipos: ", lista_equipos)
# save_all_equipos()