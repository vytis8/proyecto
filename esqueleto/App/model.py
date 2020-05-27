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
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime
from Sorting import mergesort as merg
from ADT import orderedmap as tree

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    libgraph = g.newGraph(7235,compareByKey,directed=True)
    catalog = {'librariesGraph':libgraph}    
    catalog['map_station']= map.newMap(numelements=11, comparefunction=compareByKey)
    catalog['list_temepratura']=lt.newList()
    catalog['map_city_req2']= map.newMap(comparefunction=compareByKey)
    return catalog


def addLibraryNode (catalog, row):
    """
    Adiciona un nodo para almacenar una biblioteca
    """
    if not g.containsVertex(catalog['librariesGraph'], row['ID_src']):
        g.insertVertex (catalog['librariesGraph'], row['ID_src'])
    if not g.containsVertex(catalog['librariesGraph'], row['ID_dst']):
        g.insertVertex (catalog['librariesGraph'], row['ID_dst'])

def addLibraryEdge  (catalog, row):
    """
    Adiciona un enlace entre bibliotecas
    """
    g.addEdge (catalog['librariesGraph'], row['ID_src'], row['ID_dst'], float(row['dist']))


def Add_station_list(catalog, row):
    if map.contains(catalog['map_station'], row['city']) == None:
        value= lt.newList()
        map.put(catalog['map_station'],row['city'],value)
        dic={'city_id':row['id'],'dock_count':row['dock_count'], 'city':row['city']}
        lista= map.get(catalog['map_station'],row['city'])
        lt.addFirst(lista, dic)
    else:
        lista= map.get(catalog['map_station'],row['city'])
        dic={'city_id':row['id'],'dock_count':row['dock_count'], 'city':row['city']}
        lt.addFirst(lista,dic)

def add_day_temperature(catalog, row):
    elemento= {'dia':row['date'],
    'mean_temperature_f':row['mean_temperature_f']}
    lt.addFirst(catalog['list_temepratura'],elemento)

def Add_map_tree(catlog, row):
    city_zipc= row['zip_code']
    lista_zip= city_zipc.split()
    city= lista_zip[2]
    city += lista_zip[3]

    formato= '%m/%d/%Y'
    fecha= strToDate(row['start_date'],formato)

    ciudad_arbol=map.get(catlog['map_city_req2'],city)
    if ciudad_arbol:
        arbol= tree.get(ciudad_arbol,fecha, compareByKey)
        if arbol:
            arbol['viajes']+=1
        else:
            dic= {'date': fecha,
            'viajes':1}
            tree.put(ciudad_arbol,dic['date'],dic, compareByKey)
    else:
        value= tree.newMap()
        dic= {'date': fecha,
        'viajes':1}
        tree.put(value, dic['date'], dic, compareByKey)
        map.put(catalog['map_city_req2'],city, value)

def ordenar_listas_req1(catalog):
    ciudades= map.keySet(catalog['map_station'])
    for i in range(1,lt.size(ciudades)+1):
        key= lt.getElement(ciudades, i)
        lista= map.get(catalog['map_station'],key)
        merg.mergesort(lista, less_fuction_req1)

def get_first_3(catalog, city_code):
    ciudad = map.get(catalog['map_station'], city_code)
    respuesta = lt.newList()
    for i in range (1, 3):
        stacion=lt.getElement(catalog['map_sation'],i)
        dic= {'ciudad':satcion['name'],
        'dock_count':stacion['dock_count']}
        lt.addLast(respuesta, dic)
    return respuesta



def ordenar_lista_req3(catalog):
    merg.mergesort(catalog['list_temepratura'],less_fuction_req3)

def cargar_viajes_dia():
    pass


def req_3(catalog, dias):
    lista= catalog['list_temepratura']
    size 
    first= lt.subList(lista, 1, dias)
    last= l




    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def less_fuction_req1(el_1, el_2):
    return el_1['dock_count'] < el_2['dock_count']
        
def less_fuction_req3(el_1, el_2):
    return el_1['mean_temperature_f'] < el_2['mean_temperature_f']

def strToDate(date_string, format):
    
    try:
        # date_string = '2016/05/18 13:55:26' -> format = '%Y/%m/%d %H:%M:%S')
        return datetime.strptime(date_string,format)
    except:
        return datetime.strptime('1900', '%Y')