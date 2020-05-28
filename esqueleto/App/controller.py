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
import model
import csv
from ADT import list as lt
from ADT import map as map


from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)


# Funciones para la carga de datos 

def loadLibraries (catalog, sep=','):
    """
    Carga las bibliotecas del archivo.
    Por cada para de bibliotecas, se almacena la distancia en kilometros entre ellas.
    """
    libsFile = cf.data_dir + 'GoodReads/station.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(libsFile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            model.Add_station_list(catalog,row)
    model.ordenar_listas_req_1(catalog) 

def load_weather(catalog, sep=','):
    libsFile = cf.data_dir + 'GoodReads/weather.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(libsFile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            model.add_day_temperature(catalog,row)
    model.ordenar_lista_req3(catalog)
    model.cargar_viajes_dia(catalog)
    
def load_dates(catalog, sep=','):
    libsFile = cf.data_dir + 'GoodReads/trip.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(libsFile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            model.Add_map_tree(catalog, row)
            model.date_tally(catalog, row)


def load_graph(catalog, sep=','):
    libsFile = cf.data_dir + 'GoodReads/tripday_edges.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(libsFile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            model.addstationNode(catalog, row)
            model.addstationEdge(catalog, row)
            
    
    
def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



def loadData (catalog):
    """
    Carga los datos de los archivos en la estructura de datos
    """
    t1_start = process_time() #tiempo inicial
    loadLibraries(catalog)
    load_dates(catalog)
    load_weather(catalog)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga es de:",t1_stop-t1_start," segundos") 
    pass    

def req_1(catalog, ciudad):
    t1_start = process_time()
    respuesta =model.get_first_3(catalog, ciudad)
    t1_stop = process_time() #tiempo final
    print("la consulta se demoro:",t1_stop-t1_start," segundos")
    return respuesta



def req_2(catalog,fechas):
    t1_start = process_time()
    respuesta =model.req2(catalogo, fechas)
    t1_stop = process_time() #tiempo final
    print("la consulta se demoro:",t1_stop-t1_start," segundos")
    return respuesta

def req_3(catalog, day):
    t1_start = process_time()
    respuesta =model.req_3(catalog, day)
    t1_stop = process_time() #tiempo final
    print("la consulta se demoro:",t1_stop-t1_start," segundos")
    return respuesta

def req_4(catlog, start, end):
    t1_start = process_time()
    respuesta =model.camino_dj(catalog, start, end)
    t1_stop = process_time() #tiempo final
    print("la consulta se demoro:",t1_stop-t1_start," segundos")
    return respuesta


