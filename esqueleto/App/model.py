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
from DataStructures import dijkstra as dj

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
    catalog= {}
    catalog['map_station']= map.newMap(numelements=11, comparefunction=compareByKey)
    catalog['list_temepratura']=lt.newList(datastructure='ARRAY_LIST')
    catalog['map_city_req2']= map.newMap(comparefunction=compareByKey)
    catalog['fecha_tally_viajes']=map.newMap(numelements=737, comparefunction=compareByKey)
    catalog['grafo']=g.newGraph(7235,compareByKey,directed=True)
    return catalog


def addstationNode (catalog, row):
    """
    Adiciona un nodo para almacenar una biblioteca
    """
    if not g.containsVertex(catalog['grafo'], row['src']):
        g.insertVertex (catalog['grafo'], row['src'])
    if not g.containsVertex(catalog['grafo'], row['dst']):
        g.insertVertex (catalog['grafo'], row['dst'])

def addstationEdge  (catalog, row):
    """
    Adiciona un enlace entre bibliotecas
    """
    g.addEdge (catalog['grafo'], row['src'], row['dst'], float(row['duration']))


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
    'temperature':row['mean_temperature_f']}
    lt.addFirst(catalog['list_temepratura'],elemento)



    

def Add_map_tree(catalogo, row):
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

def date_tally(catalog, row):
    mapa= catalog['fecha_tally_viajes']
    formato= '%m/%d/%Y'
    fecha= strToDate(row['start_date'],formato)

    date= map.get(mapa, fecha)
    if date:
        date['total']+=1
    else:
        dic={'fehca':fecha, 'total':1}
        map.put(mapa, fecha, dic)

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
        estacion=lt.getElement(ciudad,i)
        dic= {'ciudad':estacion['name'],
        'dock_count':estacion['dock_count']}
        lt.addLast(respuesta, dic)
    return respuesta

def req2(catalogo, rango):
    dat= rango.split(' ')
    respuesta={}
    fecha_1= strToDate(dat[0], '%m/%d/%Y')
    fecha_2=strToDate(dat[1],'%m/%d/%Y')
    ciudades= map.keySet(catalogo['map_city_req2'])
    for i in range (1, lt.size(ciudades)):
        arbol= lt.getElement(ciudades, i)
        rango_set= tree.valueRange(arbol, fecha_1, fecha_2, compareByKey)
        for z in range (1, lt.size(rango_set)):
            dic= lt.getElement(rango_set, z)
            respuesta[str(i)] += dic['viajes']
    return respuesta


    


def ordenar_lista_req3(catalog):
    merg.mergesort(catalog['list_temepratura'],less_fuction_req3)

def cargar_viajes_dia(catalog):
    lista_tem = catalog['list_temepratura']
    mapa= catalog['fecha_tally_viajes']
    for i in range(1, lt.size(lista_tem)):
        elemento= lt.getElement(lista_tem, i)
        fecha= elemento['dia']
        fech_map= map.get(mapa, fecha)
        elemento['total']=fech_map['total']
        

    


def req_3(catalog, dias):
    lista= catalog['list_temepratura']
    respuesta= lt.newList()

    for i in range(1, dias):
        dic= lt.getElement(lista, i)
        fecha=dic['dia']
        pos= i
        temperatura=dic['temperature']
        res={'posicion':pos, 'fecha':fecha, 'temperatura':temperatura}
        lt.addFirst(respuesta, res)

    tamaño= lt.size(lista)
    for i in range(tamaño, tamaño-int(dias)):
        dic= lt.getElement(lista, i)
        fecha=dic['dia']
        pos= -i
        temperatura=dic['temperature']
        res={'posicion':pos, 'fecha':fecha, 'temperatura':temperatura}
        lt.addFirst(respuesta, res)
    return respuesta


'''def camino_dj(catalog, start, end):
    graph= catalog['grafo']
    search= dj.newDijkstra(graph, start)
    mapa= search['visitedMap']
    lista= lt.newList()
    current= end
    while current != start:
        elemento= map.get(mapa,current)
        lt.addFirst(lista, {'vertice':elemento['edgeTo'], 'distancia':elemento['distTo'])
        current= elemento['edgeTo']
    return lista
'''



    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def less_fuction_req1(el_1, el_2):
    return el_1['dock_count'] < el_2['dock_count']
        
def less_fuction_req3(el_1, el_2):
    return el_1['temperature'] < el_2['temperature']

def strToDate(date_string, format):
    
    try:
        # date_string = '2016/05/18 13:55:26' -> format = '%Y/%m/%d %H:%M:%S')
        return datetime.strptime(date_string,format)
    except:
        return datetime.strptime('1900', '%Y')