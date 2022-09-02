# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:38:54 2022
@author: Paula Insuasty
"""
from tabulate import tabulate
from classes.menu import *
from main import *

global e
global equipos_registrados
global datos
global datos_separados
equipos_registrados = []
datos_separados= []

class Equipo:
    file = "database/equipos_registrados.csv"
    file_equipos_modificado = "database/prestamos_equipos_modificado.csv"
    def __init__(self,nombre_equipo,referencia, proveedor, ciclo_mantenimiento, cantidad, ultima_fecha_mantenimiento = ""):
        self.nombre_equipo = nombre_equipo
        self.referencia = referencia
        self.proveedor = proveedor
        self.ciclo_mantenimiento = ciclo_mantenimiento
        self.cantidad = (cantidad)
        self.ultima_fecha_mantenimiento = ultima_fecha_mantenimiento

    def ver_datos(self):
        #nombre_equipo, referencia, proveedor, ciclo_mantenimiento, cantidad, ultima_fecha_mantenimiento
        header = ["Nombre del equipo", "Referencia", "Proveedor", "Ciclo de mantenimiento", "Cantidad", "Ultima fecha de mantenimiento"]
        datos = [[self.nombre_equipo, self.referencia,self.proveedor,self.ciclo_mantenimiento, self.cantidad, self.ultima_fecha_mantenimiento]]
        print(tabulate(datos, header, tablefmt = "grid"))
    def save(self):
        f = open(self.file, "a")
        linea = ";".join([self.nombre_equipo, self.referencia,self.proveedor,self.ciclo_mantenimiento, self.cantidad, self.ultima_fecha_mantenimiento])
        f.write(linea + "\n")
        f.close()
    def consulta (self,nombre):
        archivo = open("equipos_registrados.csv", "r")
        lineas = archivo.readlines() 
        header = ["nombre", "proveedor", "ciclo", "cantidad", "fecha ultimo mantenimiento"]
        # datos = [[self.nombre, self.referencia, self.cantidad, self.proveedor, self.ciclo, self.fum]]
        datos = []
        datos.append(lineas)
        for l in (lineas):
            # print(l)
            l = l.replace("\n", "")
            l = l.split(";")
            datos.append(l)
        print(tabulate(datos, header, tablefmt="grid"))
#***********************************************************************************************************************
def crear_equipo():
    print("Registrar nuevo equipo:")
    nombre_equipo = input(("Ingresa el nombre del equipo: "))
    referencia = input(("Ingresa la referencia del equipo: "))
    proveedor = input(("Ingresa el proveedor del equipo: "))
    ciclo_mantenimiento = input(("Ingresa el ciclo de mantenimiento en dias para el equipo "))
    cantidad = input(("Ingresa la cantidad de este equipo"))
    ultima_fecha_mantenimiento = input(("Ingresa la ultima fecha de mantenimiento"))
    e = Equipo(nombre_equipo, referencia, proveedor, ciclo_mantenimiento, cantidad, ultima_fecha_mantenimiento)
    return e
    save_all_equipos(e)
#***********************************************************************************************************************
def consultar_equipo():
    print("Opción para verificar si el equipo está registrado")
    print("Consulta de equipos registrados:")
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
            equipo_existe = equipo_existe + 1
    if equipo_existe >= 1:
        print("El equipo existe y está disponible en el laboratorio")
    else:
        print("Disculpa, el equipo no existe o no está disponible")
        #exit()
    
#***********************************************************************************************************************
def registro_mantenimiento():
    lista_equipos = get_all_equipos()
    equipo = input("Ingresa el nombre del equipo a registrar el mantenimiento: ")
    fecha_ultimo_mantenimiento = input("Ingresa la fecha del ultimo mantenimiento:")
    pos = 0
    #datos_equipo = []
    #i = 0
    #print("Viendo equipos en lista equipos:", lista_equipos)
    for e in lista_equipos:
        #print("* INCIO DE RONDA *")
        print("e es:" ,e)
        if equipo in e:
            print("Equipo encontrado")
            datos_equipo = e.split(";")
            #print("Previo de datos equipo pos 5: ", datos_equipo[5] )
            datos_equipo[5] = fecha_ultimo_mantenimiento + "\n"
            lista_equipos[pos] = ";".join(datos_equipo)
            #print("Posterior de datos equipo pos 5: ", datos_equipo[5])
            print("Revisando nueva version de lista de equipos: ", lista_equipos[pos])
            print("Información actualizada!")
        else:
            print("El equipo no se encuentra registrado")
            #print("Por favor registra el equipo o verifica si escribiste el nombre correo y vuelve a intentarlo")
            #main()

        pos = pos+1
        #print("TODA LA NUEVA VERSIÓN DE LISTA EQUIPOS ES: ", lista_equipos)
        #print("* FIN DE RONDA*")
        #print(" ")
        #pos == 1
    print("Viendo la lista actualizada con fum de todos los equipos: ", lista_equipos)
    #save_all_equipos(lista_equipos)

    ##
    a = open("database/equipos_registrados_modificados.csv", "w")
    for e in lista_equipos:
        a.write(e)
    a.close()

    save_all_equipos()
    #save_all_equipos_modificados(lista_equipos)

    #print("Final TODA LA NUEVA VERSIÓN DE LISTA EQUIPOS ES: ", lista_equipos)
#   Equipo.save()
#   print(lista_equipos)
    #print_all_equipos()
#***********************************************************************************************************************
def save_all_equipos_modificados():
    #a = open("database/equipos_registrados.csv","w")
    a = open("database/equipos_registrados_modificados.csv", "a")
    for e in equipos_registrados:
        a.write(e)
    a.close()
#***********************************************************************************************************************
def save_all_equipos():
    #a = open("database/equipos_registrados.csv","w")
    a = open("database/equipos_registrados.csv", "a")
    for e in equipos_registrados:
        a.write(e)
    a.close()
#***********************************************************************************************************************
def get_all_equipos():
    a = open("database/equipos_registrados.csv", "r")
    datos= a.readlines()
    return datos
#***********************************************************************************************************************
def evaluando_cantidad():
    print("Opción para verificar la cantidad de equipos")
    nombre_equipo = input("Ingresa el nombre del equipo a evaluar su disponibilidad actual")
    archivo = open("database/equipos_registrados.csv", "r")
    lineas = archivo.readlines()
    datos = []
    datos.append(lineas)
    for l in (lineas):
        # print(l)
        l = l.replace("\n", "")
        l = l.split(";")
        datos.append(l)
    #datos_nuevos = []
    h = 0
    tiene_prestamo = 0
    equipo_en_prestamo = 0

    #nueva_cantidad = (datos[h][4])
    nueva_cantidad = 0

    for h in range(len(datos)):
        if datos[h][1] == nombre_equipo :
            print("Si encontré coincidencia")
            print("El dato que estoy viendo es: ", datos[h])
            print("Viendo la cantidad actual del equipo (datos(4)): ", datos[h][4])

            # AQUI ESTOY ACTUALIZANDO CANTIDAD DE EQUIPOS COMO SI FUERA PRESTAMO!
            #nueva_cantidad = datos[h][4] - 1
            #nueva_cantidad = nueva_cantidad - 1
            #print("Actualizando cantidad del equipo! ")

        if int(datos[h][4]) <= 0:
        #if int(nueva_cantidad) <= 0:
            print("No hay más disponibilidad de equipos, no se puede realizar el prestamo")

    else:
        print("Queda un total de: ", nueva_cantidad, "del equipo: ", nombre_equipo)
        print("Por tanto, si se puede realizar el prestamo")
        # print("Para un q de: ", q, " en 1 se tienen datos: ", datos[q][1])
        #if datos[h][1] == cantidad:
        #    tiene_prestamo = tiene_prestamo + 1
#***********************************************************************************************************************
def print_all_equipos_originales():
    a = open("database/equipos_registrados.csv", "r")
    datos= a.readlines()
    #print("Viendo lista actualizada de todos los equipos: ")
    header = ["nombre", "proveedor", "ciclo", "cantidad", "fecha ultimo mantenimiento"]
    print(tabulate(datos, header, tablefmt="grid"))
    return datos

#***********************************************************************************************************************
#************************************* INTENTOS  PREVIOS ***************************************************************
# ***********************************************************************************************************************
    # if tiene_prestamo >= 1:
    #     print("Tiene un total de: ", tiene_prestamo, "prestamos registrados")
    #     for q in range(len(datos)):
    #         if datos[q][1] == numero_carnet:
    #             equipo_en_prestamo = datos[q][2]
    #             referencia_equipo_en_prestamo = datos[q][3]
    #             fecha_entrega_equipo_en_prestamo = datos[q][5]

# *************************** PRUEBAS PREVIAS **********************************************************
# def save(self):
#     # **** Prueba guardando los equipos en un .csv ****
#     file = open("equipos_registrados.csv", "a")
#     #header = ["Nombre del equipo", "Referencia", "Proveedor", "Ciclo de mantenimiento", "Cantidad", "Ultima fecha de mantenimiento"]
#     datos = [[self.nombre_equipo, self.referencia,self.proveedor,self.ciclo_mantenimiento, self.cantidad, self.ultima_fecha_mantenimiento]]
#     for i in range (len(datos)):
#         datos_separados[i] = datos[i]

#     print(datos_separados)

# equipos_registrados = []
# equipos_registrados.append(datos) # datos me da todos los datos en forma de lista, separados por comas
# header = ["Nombre del equipo", "Referencia", "Proveedor", "Ciclo de mantenimiento", "Cantidad", "Ultima fecha de mantenimiento"]
# datos = [[self.nombre_equipo, self.referencia,self.proveedor,self.ciclo_mantenimiento, self.cantidad, self.ultima_fecha_mantenimiento]]
# #print(tabulate(datos, header, tablefmt = "grid"))
# #equipo2 = "sensor cardiaco; xxxx; 10 ; 15; 2022-07-30 "
# file.write(equipos_registrados + "\n")
# #file.write(equipo2 + "\n")
# ## para que queden en lineas separadas:
# # escribir datos:
# # file.write("Hola, este es mi primer archivo")
# # cerrar el archivo:
# file.close()

###

# file = open("datos.csv", "a")
# equipo = "multimetro; general ; 10; 20; 2022-08-20 "
# file.write(equipo + "\n")
# file.close()

# 		archivo = open("equipos_registrados.csv", "r")
# 		lineas = archivo.readlines()

# 		header = ["nombre", "proveedor", "ciclo", "cantidad", "fum"]
# 		# datos = [[self.nombre, self.referencia, self.cantidad, self.proveedor, self.ciclo, self.fum]]
# 		datos = []
# 		datos.append(lineas)

# 		for l in (lineas):
# 			# print(l)
# 			l = l.replace("\n", "")
# 			l = l.split(";")
# 			datos.append(l)

# 		print(tabulate(datos, header, tablefmt="grid"))

# 	def save(self): # rear metodo save, crear metodo para consultador uno en especifico, que me datos de un equipo en especifico
# 		# **** PRUEBA CON EJERCICIO EN CLASE ****
# 		file = open("datos.csv", "w")
# 		equipo = "Impresora 3D;general electric;2;30;2022-08-20"
# 		equipo2 = "sensor cardiaco; xxxx; 10 ; 15; 2022-07-30 "
# 		file.write(equipo + "\n")
# 		file.write(equipo2 + "\n")
# 		## para que queden en lineas separadas:
# 		# escribir datos:
# 		# file.write("Hola, este es mi primer archivo")
# 		# cerrar el archivo:
# 		file.close()

# 		###

# 		file = open("datos.csv", "a")
# 		equipo = "multimetro; general ; 10; 20; 2022-08-20 "
# 		file.write(equipo + "\n")
# 		file.close()

# 		archivo = open("datos.csv", "r")
# 		lineas = archivo.readlines()

# 		header = ["nombre", "proveedor", "cantidad", "ciclo", "fum"]
# 		# datos = [[self.nombre, self.referencia, self.cantidad, self.proveedor, self.ciclo, self.fum]]
# 		datos = []
# 		datos.append(lineas)

# 		for l in (lineas):
# 			# print(l)
# 			l = l.replace("\n", "")
# 			l = l.split(";")
# 			datos.append(l)

# 		print(tabulate(datos, header, tablefmt="grid"))

# *****+

# if opcion_menu_tecnico == "1":
# def __init__(self,nombre_equipo,referencia, proveedor, ciclo_mantenimiento, ultima_fecha_mantenimiento, cantidad):
# print("Creando equipos: ...")
# print("Por favor ingresa las caracterÃ­sticas del equipo: ")
# nombre_equipo = input(print("Ingresa el nombre del equipo: "))
# nombre_equipo = self.nombre_equipo
# referencia = input(print("Ingresa la referencia del equipo: "))
# referencia = self.referencia
# proveedor = input(print("Ingresa el proveedor del equipo: "))
# proveedor = self.proveedor
# ciclo_mantenimiento = input(print("Ingresa el ciclo de mantenimiento en dias para el equipo "))
# ciclo_mantenimiento = self.ciclo_mantenimiento
# ultima_fecha_mantenimiento = input(print("Ingresa la ultima fecha de mantenimiento"))
# ultima_fecha_mantenimiento = self.ultima_fecha_mantenimiento
# cantidad = input(print("Ingresa la cantidad de este equipo"))
# cantidad = self.cantidad

# if opcion_menu_tecnico == "2":
#	print("Registrando prestamo: ...")

# *******************

# if equipo in lista_equipos:
    #     print("Equipo encontrado")
    #     for e in lista_equipos:
    #         datos_equipo = e.split(";")
    #         datos_equipo[5] = fecha_ultimo_mantenimiento + "\n"
    #         lista_equipos[pos] = ";".join(datos_equipo)
    #         pos = pos+1
    #     print("Información actualizada!")
    # else:
    #     print("El equipo no se encuentra registrado")
