import unittest
import config
import math 
import dijsktra as dij
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
from ADT import stack as stack 
from ADT import map as m 
from ADT import list as lt
from ADT import indexminpq as iminpq
import csv



class DijkstraTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def comparekeys (self, key, element):
        if (key != None and element != None):
            if ( key == element['key']):
                return True
        return False

    def comparenames (self, searchname, element):
        return (searchname == element['key'])

    def test_dijkstra (self):

        graph = g.newGraph ( 7, self.comparenames, directed=True )
        # se inicializa el grafo
        self.loadgraph  (graph)     
        self.assertEqual (g.numVertex(graph), 7)
        self.assertEqual (g.numEdges(graph), 12)   
        # Se ejecuta dijkstra
        search = dij.newDijkstra(graph,'Bogota') 
        path = dij.pathTo(search, 'Cali' )
        while not stack.isEmpty (path):
            paso = stack.pop(path)
            print (paso['vertexA'] + "-->" + paso['vertexB'] + " costo: " + str(paso['weight']))
        print(dij.distTo(search, 'Cali' ))



    def loadgraph (self, graph):
        """
        Crea el grafo con la informacion de prueba
        """
        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Duitama')
        g.insertVertex (graph, 'Armenia')
        g.insertVertex (graph, 'Honda')
        g.insertVertex (graph, 'Espinal')
        g.insertVertex (graph, 'Florencia')
        g.insertVertex (graph, 'Cali')

        g.addEdge (graph, 'Bogota', 'Duitama', 3.5)
        g.addEdge (graph, 'Bogota', 'Honda', 3)
        g.addEdge (graph, 'Bogota', 'Espinal', 4.5)
        g.addEdge (graph, 'Duitama', 'Armenia', 1)
        g.addEdge (graph, 'Honda', 'Duitama', 1)
        g.addEdge (graph, 'Honda', 'Espinal', 1)
        g.addEdge (graph, 'Honda', 'Armenia', 2.5)
        g.addEdge (graph, 'Honda', 'Florencia', 5.5)
        g.addEdge (graph, 'Espinal', 'Florencia', 2.4)
        g.addEdge (graph, 'Honda', 'Cali', 6)
        g.addEdge (graph, 'Florencia', 'Cali', 1)
        g.addEdge (graph, 'Armenia', 'Cali', 4)
        
   

if __name__ == "__main__":
    unittest.main()
