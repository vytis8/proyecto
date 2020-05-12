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

def ordenar_listas(catalog):
    ciudades= map.keySet(catalog['map_station'])
    for i in range(1,lt.size(ciudades)+1):
        key= lt.getElement(ciudades, i)
        lista= map.get(catalog['map_station'],key)
        merg.mergesort(lista, less_fuction)





    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def less_fuction(el_1, el_2):

    return el_1['dock_count'] < el_2['dock_count']
        
    

