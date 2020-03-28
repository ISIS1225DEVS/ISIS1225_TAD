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
from DataStructures import liststructure as lt
from ADT import map as map 

def newGraph( size, cmpfunction ):
    """
    Crea un grafo vacio. Los vertices son guardados en un map de tipo linear probing
    """
    prime = nextPrime (size * 2)
    graph = {'vertices':None, 'edges':0, 'type':'ADJ_LIST' }
    #graph ['vertices'] = lt.newList()
    graph ['vertices'] = map.newMap(capacity=prime, maptype='PROBING',comparefunction=cmpfunction)

    return graph



def insertVertex ( graph, vertex ):
    """
    Inserta el vertice vertex en el grafo graph
    """ 
    edges = lt.newList()
    map.put (graph['vertices'], vertex, edges)
    return graph



def removeVertex ( graph, vertex, comparefunction):
    """
    Remueve el vertice vertex del grafo graph
    """ 
    #revisar
    present = lt.isPresent (graph['vertices'], vertex, comparefunction )
    if present: 
        lt.deleteElement (graph['vertices'], present)
    return graph


def numVertex (graph):
    """
    Retorna el numero de vertices en el  grafo graph
    """ 
    return lt.size (graph['vertices'])


def numEdges (graph):
    """
    Retorna el numero de arcos en el  grafo graph
    """ 
    return (graph['edges'])


def vertices (graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    """ 
    pass


def edges (graph):
    """
    Retorna una lista con todos los arcos del grafo graph
    """ 
    pass


def degree (graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.degree (graph, vertex)


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

    return alt.addEdge (graph, vertexa, vertexb, weight)



def adjacents (graph, vertex ):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex
    """ 
    if (graph['type'] == "ADJ_LIST"):
        return alt.adjacents(graph, vertex)



# ====================
#  Funciones Helper
# ====================


# Function that returns True if n  
# is prime else returns False 
# This code is contributed by Sanjit_Prasad  
def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
      
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True
  
# Function to return the smallest  
# prime number greater than N 
# # This code is contributed by Sanjit_Prasad  
def nextPrime(N): 
  
    # Base case  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
  
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 

    