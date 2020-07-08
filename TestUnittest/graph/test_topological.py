import unittest
import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
from ADT import stack as s 
from ADT import map as m 
from ADT import list as lt


class DigraphTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])

    def comparelst (self, searchname, element):
        return (searchname == element)


    def test_topological (self):

        graph = g.newGraph ( 10, self.comparenames, directed=True )
        pre = q.newQueue()
        post = q.newQueue()
        reversepost = s.newStack()
        marked = m.newMap (10, comparefunction=self.comparenames)
    

        g.insertVertex (graph, 'Calculo1')
        g.insertVertex (graph, 'Calculo2')
        g.insertVertex (graph, 'Diseno1')
        g.insertVertex (graph, 'Diseno2')
        g.insertVertex (graph, 'Electiva')
        g.insertVertex (graph, 'Fisica1')
        g.insertVertex (graph, 'Ingles')
        g.insertVertex (graph, 'IP1')
        g.insertVertex (graph, 'IP2')
        g.insertVertex (graph, 'ProyectoFinal')

        g.addEdge (graph, 'Calculo1', 'Calculo2')
        g.addEdge (graph, 'Calculo2', 'IP2')
        g.addEdge (graph, 'Calculo2', 'Fisica1')
        g.addEdge (graph, 'Diseno1', 'Diseno2')
        g.addEdge (graph, 'Diseno2', 'ProyectoFinal')
        g.addEdge (graph, 'Electiva', 'ProyectoFinal')
        g.addEdge (graph, 'Fisica1', 'Diseno2')
        g.addEdge (graph, 'Ingles', 'ProyectoFinal')
        g.addEdge (graph, 'IP1', 'Diseno1')
        g.addEdge (graph, 'IP1', 'IP2')

        self.assertEqual (g.numEdges(graph), 10)
        self.assertEqual (g.numVertex(graph), 10)

        #DFO 

        lstvert = g.vertices (graph)
        vertiterator = it.newIterator (lstvert)
        while it.hasNext (vertiterator):
            vert = it.next (vertiterator)
            if not (m.contains (marked,vert)):
                self.dfs (graph, vert, marked, pre, post, reversepost)
        self.printTopological (reversepost)
        

    def dfs (self, graph, vert, marked, pre, post, reversepost):
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


    def printTopological (self,reversepost):
        print ('se pueden ver los cursos en el siguiente orden:')
        while not s.isEmpty(reversepost):
            print (s.pop (reversepost))



if __name__ == "__main__":
    unittest.main()
