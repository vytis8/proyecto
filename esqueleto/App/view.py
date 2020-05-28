"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import stack as stk
from ADT import orderedmap as map
from DataStructures import listiterator as it

import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 9")
    print("1- Cargar información")
    print("2- Req1")
    print("3- Req2")
    print("4- Req3")
    print("5- Req4")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las bibliotecas en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    while True: 
        printMenu()
        inputs =input("Seleccione una opción para continuar\n")
        if int(inputs[0])==1:
            print("Cargando información de los archivos ....")
            catalog = initCatalog ()
            loadData (catalog)
        elif int(inputs[0])==2:
            pass
        elif int(inputs[0]) == 3:
            fecha1 = input("Ingrese la fecha de inicio: ")
            fecha2 = input("Ingrese la fecha de terminación: ")
        elif int(inputs[0]) == 4:
            dia = input("Ingrese la fecha de inicio: ")
            cantidad_dias = input("Ingrese la cantidad de días a consultar: ")
            temp = input("Ingrese la temperatura a consultar: ")
        elif int(inputs[0]) == 5:
            estacion1 = input("Ingrese la estación de origen: ")
            estacion2 = input("Ingrese la estación destino: ")
            fecha = input("Ingrese la fecha a consultar: ")
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    main()