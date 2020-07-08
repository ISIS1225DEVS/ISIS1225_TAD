import unittest
import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
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


    def test_newEdge (self):
        edge = e.newEdge (1,1,1)


    def test_edgeMethods (self):
        edge = e.newEdge ('Bogota','Cali')

        edge = e.newEdge ('Bogota','Cali')
        self.assertEqual ('Bogota', e.either(edge))
        self.assertEqual ('Cali', e.other(edge, e.either(edge)))
        self.assertEqual  (e.weight(edge), 0)



    def test_insertVertex (self):

        graph = g.newGraph(7,self.comparenames,directed=True)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')
        self.assertEqual (g.numVertex(graph),7)



    def test_addEdges (self):
        graph = g.newGraph(7, self.comparenames, directed=True)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal')
        g.addEdge (graph, 'Bogota', 'Medellin')
        g.addEdge (graph, 'Bogota', 'Pasto')
        g.addEdge (graph, 'Bogota', 'Cali')
        g.addEdge (graph, 'Yopal', 'Medellin')
        g.addEdge (graph, 'Medellin', 'Pasto')
        g.addEdge (graph, 'Cali', 'Pasto')
        g.addEdge (graph, 'Cali', 'Barranquilla')
        g.addEdge (graph, 'Barranquilla','Manizales')
        g.addEdge (graph, 'Pasto','Manizales')

        self.assertEqual (g.numEdges(graph), 10)
        self.assertEqual (g.numVertex(graph), 7)

        lst = g.vertices (graph)
        self.assertEqual (lt.size (lst), 7)

        lst = g.edges (graph)
        self.assertEqual (lt.size (lst), 10)

        degree = g.degree (graph, 'Bogota')
        self.assertEqual (degree, 4)

        edge = g.getEdge (graph, 'Bogota', 'Medellin')

        lst = g.adjacents (graph, 'Bogota')
        self.assertEqual (lt.size (lst), 4)
    

    def test_insertVertex (self):

        graph = g.newGraph(7,self.comparenames,directed=True)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')
        self.assertEqual (g.numVertex(graph),7)



    def test_degrees (self):
        graph = g.newGraph(7, self.comparenames, directed=True)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal')
        g.addEdge (graph, 'Bogota', 'Medellin')
        g.addEdge (graph, 'Bogota', 'Pasto')
        g.addEdge (graph, 'Bogota', 'Cali')
        g.addEdge (graph, 'Cali', 'Bogota')
        g.addEdge (graph, 'Yopal', 'Medellin')
        g.addEdge (graph, 'Medellin', 'Pasto')
        g.addEdge (graph, 'Pasto', 'Bogota')
        g.addEdge (graph, 'Cali', 'Pasto')
        g.addEdge (graph, 'Cali', 'Barranquilla')
        g.addEdge (graph, 'Barranquilla','Manizales')
        g.addEdge (graph, 'Pasto','Manizales')

        self.assertEqual (g.numEdges(graph), 12)
        self.assertEqual (g.numVertex(graph), 7)

        degree = g.indegree (graph, 'Bogota')
        self.assertEqual (degree, 2)

        degree = g.indegree (graph, 'Barranquilla')
        self.assertEqual (degree, 1)

        degree = g.outdegree (graph, 'Barranquilla')
        self.assertEqual (degree, 1)

        degree = g.outdegree (graph, 'Bogota')
        self.assertEqual (degree, 4)

        degree = g.outdegree (graph, 'Manizales')
        self.assertEqual (degree, 0)


    def test_adjacents (self):
        graph = g.newGraph(7, self.comparenames, directed=True)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal')
        g.addEdge (graph, 'Bogota', 'Medellin')
        g.addEdge (graph, 'Bogota', 'Pasto')
        g.addEdge (graph, 'Bogota', 'Cali')
        g.addEdge (graph, 'Cali', 'Bogota')
        g.addEdge (graph, 'Yopal', 'Medellin')
        g.addEdge (graph, 'Medellin', 'Pasto')
        g.addEdge (graph, 'Pasto', 'Bogota')
        g.addEdge (graph, 'Cali', 'Pasto')
        g.addEdge (graph, 'Cali', 'Barranquilla')
        g.addEdge (graph, 'Barranquilla','Manizales')
        g.addEdge (graph, 'Pasto','Manizales')

        self.assertEqual (g.numEdges(graph), 12)
        self.assertEqual (g.numVertex(graph), 7)

        lst = g.adjacents (graph, 'Bogota')
        self.assertEqual (lt.size(lst), 4)

        self.assertTrue (lt.isPresent (lst, 'Cali', self.comparelst))
        self.assertTrue (lt.isPresent (lst, 'Yopal', self.comparelst))
        self.assertTrue (lt.isPresent (lst, 'Pasto', self.comparelst))
        self.assertTrue (lt.isPresent (lst, 'Medellin', self.comparelst))
        self.assertFalse (lt.isPresent (lst, 'Barranquilla', self.comparelst))

        lst = g.adjacents (graph, 'Manizales')
        self.assertEqual (lt.size(lst), 0)


if __name__ == "__main__":
    unittest.main()
