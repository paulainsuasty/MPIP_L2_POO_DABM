# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:37:21 2022
@author: Paula Insuasty
"""
from classes.menu import *
from classes.equipo import *
from classes.prestamo import *

def main():
    menu = Menu("Escuela Colombiana de Ingeniería")
    opcion_menu= menu.ver()
    
    if opcion_menu == "1":
        menu2 = MenuTecnicos()
        opcion_menu2 = menu2.ver()
        if opcion_menu2 == "1":
            e = crear_equipo()
            e.save()
            main()
            #menu2.ver()
            #exit()
        elif opcion_menu2 == "2":
            p = crear_prestamos()
            p.save_prestamos()
            print("Viendo todos los prestamos registrados:")
            get_all_prestamos()
            main()
            #exit()
        elif opcion_menu2 == "3":
            registro_mantenimiento()
            main()
            #print("Viendo la lista actualizada con fum de todos los equipos: ")
            #print_all_equipos()

        elif opcion_menu2 == "4":
            print("Revisando la cantidad de prestamos por el estudiante")
            consultar_prestamos_por_estudiante()
            print("Realizando el registro de entrega")
            registro_entrega()
            main()
            #exit()
        elif opcion_menu2 == "5":
            print_all_equipos_originales()
            main()
        elif opcion_menu2 == "6":
            get_all_prestamos()
            main()
        else:
            print("La opción que seleccionaste es invalida")
            main()
            
    elif opcion_menu == "2":
        menu2 = MenuEstudiantes()
        opcion_menu2 = menu2.ver()
        if opcion_menu2 == "1":
            #ver_prestamos()
            consultar_prestamos_por_estudiante()
            main()
        elif opcion_menu2 == "2":
            consultar_equipo()
            main()
        elif opcion_menu2 == "3":
            print("Evaluando cantidad")
            evaluando_cantidad()
            #print("Consultar equipo")
            #consultar_equipo()
            main()

    elif opcion_menu == "3":
        #print("Gracias")
        exit()

    #elif opcion_menu == "4":
        #actualizando_disponibilidad()
    #    verificando_disponibilidad()
    #    main()

if __name__ == "__main__":
    main()