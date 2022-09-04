# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:39:18 2022
@author: Paula Insuasty
"""
class Menu:
    def __init__(self,laboratorio): 
        self.laboratorio = laboratorio

    def ver(self):
        print("Bienvenido al sistema".center(50,"*"))
        print("laboratorio: " + self.laboratorio)
        print("1. Tecnico")
        print("2. Estudiante")
        print("3. Salir del programa")
        #print("4. Pruebas para actualizando disponibilidad")
        #print("AA")
        opcion_menu =input(">>>")

        return opcion_menu

class MenuTecnicos:
        def ver(self):
            print("Menu tecnicos de laboratorio".center(50,"*"))
            #print("laboratorio: " + self.laboratorio)
            print("1. Registrar equipos")
            print("2. Registrar prestamo")
            print("3. Registrar mantenimiento")
            print("4. Registrar entrega")
            print("5. Ver el inventario de los equipos registrados")
            print("6. Ver todos los prestamos de equipos registrados")
            #print("3. ")
            #opcion_menu2 =(input(">>>"))
            opcion_menu = input(">>>")
            return opcion_menu
            #return opcion_menu2

class MenuEstudiantes:
    def ver(self):
        print("Menu estudiantes:".center(50,"*"))
        print("1. Consultar los equipos que tiene en prestamo")
        print("2. Consultar los equipos disponibles en el laboratorio")
        print("3. Consultar la disponibilidad de los equipos")


        opcion_menu = input(">>>")
        return opcion_menu

if __name__ == "__main__":
    m = Menu("xxxx") # nombre del lb
    m.ver()