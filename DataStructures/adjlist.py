"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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

import config
import math
from ADT import map as map 
from DataStructures import liststructure as lt
from DataStructures import listiterator as it
from DataStructures import edge as e


def newGraph( size, cmpfunction, directed ):
    """
    Crea un grafo vacio. Los vertices son guardados en un map de tipo linear probing
    """
    try:
        graph = {'vertices':None,  
                'edges':0,  
                'type':'ADJ_LIST', 
                'comparefunction':cmpfunction, 
                'directed':directed,
                'indegree':None}

        graph ['vertices'] = map.newMap(numelements=size, maptype='PROBING',comparefunction=cmpfunction)

        if (directed):
            graph ['indegree'] = map.newMap(numelements=size, maptype='PROBING',comparefunction=cmpfunction)

        return graph

    except Exception as e:
        return None



def insertVertex ( graph, vertex ):
    """
    Inserta el vertice vertex en el grafo graph
    :param graph: El grafo sobre el que se ejecuta la operacion
    :param vertex: El vertice que se desea insertar
    """ 
    try:
        edges = lt.newList()
        map.put (graph['vertices'], vertex, edges)
        if (graph['directed']):
            map.put (graph['indegree'], vertex, 0)
        return graph
    except:
        return None



def removeVertex ( graph, vertex):
    """
    Remueve el vertice vertex del grafo graph
    """ 
    # TODO
    pass



def numVertex (graph):
    """
    Retorna el numero de vertices en el  grafo graph
    """ 
    return map.size(graph['vertices'])



def numEdges (graph):
    """
    Retorna el numero de arcos en el  grafo graph
    """ 
    return (graph['edges'])



def vertices (graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    """ 
    try:
        lstmap = map.keySet(graph['vertices'])
        return lstmap
    except:
        return None



def edges (graph):
    """
    Retorna una lista con todos los arcos del grafo graph
    """ 
    try:
        lstmap = map.valueSet(graph['vertices'])
        itervertex = it.newIterator (lstmap)
        lstresp = lt.newList ()

        while it.hasNext (itervertex):
            lstedge = it.next (itervertex)
            iteredge = it.newIterator (lstedge)

            while (it.hasNext (iteredge)):
                edge = it.next (iteredge)
                if (graph['directed']):
                    lt.addLast (lstresp,edge)
                elif (not lt.isPresent (lstresp,edge, e.compareedges)):
                    lt.addLast (lstresp,edge)
        return lstresp
    except:
        return None
    


def degree (graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex
    """ 
    try:
        element = map.get (graph['vertices'], vertex)
        lst = element['value']
        return (lt.size(lst))
    except:
        return None



def indegree (graph, vertex):
    """
    Retorna el numero de arcos que llegan al vertice vertex
    """ 
    try:
        if (graph['directed']):
            degree = map.get (graph['indegree'], vertex)
            return degree ['value']
        return 0
    except:
        return None




def outdegree (graph, vertex):
    """
    Retorna el numero de arcos que salen del grafo vertex
    """ 
    try:
        if (graph['directed']):
            element = map.get (graph['vertices'], vertex)
            lst = element['value']
            return (lt.size(lst))
        return 0
    except:
        return None




def getEdge (graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb
    """ 
    try:
        element = map.get (graph['vertices'], vertexa)
        lst = element['value']
        itvertex = it.newIterator (lst)
        while (it.hasNext(itvertex)):
            edge = it.next (itvertex)
            if ( e.either(edge) == vertexa or (e.other(edge,e.either(edge) )== vertexa ) ):
                if ( e.either(edge) == vertexb or (e.other(edge,e.either(edge) )== vertexb ) ):
                    return edge
        return None
    except:
        return None



def containsVertex (graph, vertex):
    """
    Verifica si el grafo contiene un vertice
    """ 
    try:
        return map.get (graph['vertices'], vertex)!= None
    except:
        return None



def addEdge (graph, vertexa, vertexb, weight=0):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight.
    Si el grafo es no dirigido se adiciona dos veces el mismo arco, en el mismo orden
    Si el grafo es dirigido se adiciona solo el arco vertexa --> vertexb
    """ 
    try:
        # Se crea el arco
        edge =  e.newEdge (vertexa,vertexb, weight)

        #Se obtienen las listas de adyacencias de cada vertice
        #Se anexa a cada lista el arco correspondiente
        entrya = map.get (graph['vertices'], vertexa)
        lt.addLast (entrya['value'], edge)

        if (not graph['directed']):
            entryb = map.get (graph['vertices'], vertexb)
            lt.addLast (entryb['value'], edge)
        else:
            degree = map.get (graph['indegree'], vertexb)
            map.put (graph['indegree'], vertexb, degree['value']+1)

        graph['edges'] += 1

        return graph
    except:
        return None



def adjacents (graph, vertex ):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex
    """ 
    try:
        element = map.get (graph['vertices'], vertex)
        lst = element['value']
        lstresp = lt.newList()
        iter=it.newIterator (lst)
        while (it.hasNext(iter)):
            edge = it.next (iter)
            v = e.either(edge)
            if (v == vertex):
                lt.addLast (lstresp, e.other(edge, v))
            else:
                lt.addLast (lstresp, v)
        return lstresp
    except:
        return None

