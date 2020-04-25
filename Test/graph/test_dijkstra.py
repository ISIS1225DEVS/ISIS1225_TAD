import unittest
import config
import math 
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
from ADT import stack as s 
from ADT import map as m 
from ADT import list as lt
from ADT import indexminpq as iminpq


class DijkstraTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])

    def comparelst (self, searchname, element):
        return (searchname == element)


    def test_dijkstra (self):

        graph = g.newGraph ( 7, self.comparenames, directed=True )
        distTo = m.newMap (7, maptype= 'PROBING', comparefunction=self.comparenames)
        edgeTo = m.newMap (7, maptype= 'PROBING', comparefunction=self.comparenames)
        pq = iminpq.newIndexMinPQ (7)
        
        
        # se inicializa el grafo
        self.loadgraph  (graph)     
        self.assertEqual (g.numVertex(graph), 7)
        self.assertEqual (g.numEdges(graph), 12)               

        

    
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
        


    def dfo (self, graph, marked, pre, post, reversepost):
        """
         Implementación del recorrido Depth First Order
        """
        lstvert = g.vertices (graph)
        vertiterator = it.newIterator (lstvert)
        while it.hasNext (vertiterator):
            vert = it.next (vertiterator)
            if not (m.contains (marked,vert)):
                self.dfs (graph, vert, marked, pre, post, reversepost)
        
        

    def dfs (self, graph, vert, marked, pre, post, reversepost):
        """
          Implementación del recorrido Depth First Search
        """
        q.enqueue (pre, vert)
        m.put (marked, vert, True)
        lstadjacents = g.adjacents(graph, vert)
        adjiterator = it.newIterator (lstadjacents)
        while it.hasNext(adjiterator):
            adjvert = it.next (adjiterator)
            if not m.contains (marked, adjvert):
                self.dfs (graph, adjvert, marked, pre, post, reversepost)
        q.enqueue (post, vert)
        s.push (reversepost, vert)
       

if __name__ == "__main__":
    unittest.main()
