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
from DataStructures import adjlist as alt 

"""
  Este módulo implementa el tipo abstracto de datos (TAD) Graph. 
  Se puede implementar sobre una lista de adyacencias (ADJ_LIST) o una matriz de adyacencias (ADJ_MATRIX)
"""


def newGraph(size, comparefunction, directed, datastructure):
    """
    Crea un grafo vacio.
    """
    if (datastructure == "ADJ_LIST"):
        graph = alt.newGraph(size, comparefunction, directed)
        return graph
    else:
        return None


def insertVertex ( graph, vertex ):
    """
    Inserta el vertice vertex en el grafo graph
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.insertVertex (graph, vertex )


def removeVertex ( graph, vertex):
    """
    Remueve el vertice vertex del grafo graph
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.removeVertex (graph, vertex )


def numVertex (graph):
    """
    Retorna el numero de vertices en el  grafo graph
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.numVertex (graph)


def numEdges (graph):
    """
    Retorna el numero de arcos en el  grafo graph
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.numEdges (graph)


def vertices (graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.vertices (graph)


def edges (graph):
    """
    Retorna una lista con todos los arcos del grafo graph
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.edges (graph)


def degree (graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.degree (graph, vertex)




def outdegree (graph, vertex):
    """
    Retorna el numero de arcos que salen del grafo vertex
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.outdegree (graph, vertex)




def indegree (graph, vertex):
    """
    Retorna el numero de arcos que llegan al vertice vertex
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.indegree (graph, vertex)




def getEdge (graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.getEdge (graph, vertexa, vertexb)


def addEdge (graph, vertexa, vertexb, weight):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.addEdge (graph, vertexa, vertexb, weight)

def containsVertex (graph, vertex):
    """
    Verifica si el grafo contiene un vertice
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.containsVertex (graph, vertex)




def adjacents (graph, vertex ):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.adjacents(graph, vertex)


