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
from DataStructures import graphstructure as gr

"""
Este archivo contiene la implementacióndel TAD grafo no dirigido
"""  


def newGraph( size, comparefunction, directed = False, datastructure = "ADJ_LIST" ):
    """
     Crea un grafo vacio.
    """   
    return gr.newGraph( size, comparefunction,  directed, datastructure )


def insertVertex ( graph, vertex ):
    """
    Inserta el vertice vertex en el grafo graph
    """ 
    return gr.insertVertex (graph, vertex )


def removeVertex ( graph, vertex):
    """
    Remueve el vertice vertex del grafo graph
    """ 
    return gr.removeVertex (graph, vertex )


def numVertex (graph):
    """
    Retorna el numero de vertices en el  grafo graph
    """ 
    return gr.numVertex (graph)


def numEdges (graph):
    """
    Retorna el numero de arcos en el  grafo graph
    """ 
    return gr.numEdges (graph)


def vertices (graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    """ 
    return gr.vertices (graph)


def edges (graph):
    """
    Retorna una lista con todos los arcos del grafo graph
    """ 
    return gr.edges (graph)


def degree (graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex
    """ 
    return gr.degree (graph, vertex)


def outdegree (graph, vertex):
    """
    Retorna el numero de arcos que salen del grafo vertex
    """ 
    return gr.outdegree (graph, vertex)



def indegree (graph, vertex):
    """
    Retorna el numero de arcos que llegan al vertice vertex
    """ 
    return gr.indegree (graph, vertex)



def getEdge (graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb
    """ 
    return gr.getEdge (graph, vertexa, vertexb)


def addEdge (graph, vertexa, vertexb, weight=0):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight
    """ 
    return gr.addEdge (graph, vertexa, vertexb, weight)

def containsVertex (graph, vertex):
    """
    Verifica si el grafo contiene un vertice
    """ 
    return gr.containsVertex (graph, vertex)


def adjacents (graph, vertex ):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex
    """ 
    return gr.adjacents(graph, vertex)

def adjacentEdges (graph, vertex ):
    """
    Retorna una lista con todos los arcos asociados a los vértices adyacentes de vertex
    """ 
    return gr.adjacentEdges(graph, vertex)
