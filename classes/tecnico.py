# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:39:43 2022

@author: Paula Insuasty
"""
import datetime
#def registrar_entrega():

def equipos_mantenimiento_en_fechas():
    print("Equipos para mantenimiento en un rango de fechas:")
    date1 =input("Ingresa la primera fecha para revisar el intervalo: (d/m/y) ")
    date2 = input("Ingresa la segunda fecha para reisar el intervalo: (d/m/y)")
    #fecha_inicio = input("fecha inicio de registro de información (d/m/y)")
    #fecha_fin = input("fecha fin de registro de información (d/m/y)")

    date1 = datetime.datetime.strptime(date1, "%d/%m/%y")
    date2 = datetime.datetime.strptime(date2, "%d/%m/%y")

    dif = (date2 - date1).days # Para ver num dias:

    fecha = date1
    # encabezado.append(fecha.strftime("%d/%m/%y"))
    for i in range(0, dif):
        fecha = fecha + datetime.timedelta(days=1)
        #encabezado.append(fecha.strftime("%d/%m/%y"))
