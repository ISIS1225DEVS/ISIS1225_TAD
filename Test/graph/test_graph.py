import unittest
import config
from DataStructures import edge as e
from ADT import graph as g
from DataStructures import listiterator as it
from ADT import list as lt


class GraphTest (unittest.TestCase):

    def setUp (self):
        pass



    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])


    def test_newEdge (self):
        edge = e.newEdge (1,1,1)
        print (edge)


    def test_edgeMethods (self):
        edge = e.newEdge ('Bogota','Cali',4)

        print (e.either(edge))
        print (e.other(edge, e.either(edge)))
        print (e.weight(edge))


    def test_insertVertex (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        print (graph)

    def test_addEdges (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal', 1 )
        g.addEdge (graph, 'Bogota', 'Medellin', 1 )
        g.addEdge (graph, 'Bogota', 'Pasto', 1 )
        g.addEdge (graph, 'Bogota', 'Cali', 1 )
        g.addEdge (graph, 'Yopal', 'Medellin', 1 )
        g.addEdge (graph, 'Medellin', 'Pasto', 1 )
        g.addEdge (graph, 'Cali', 'Pasto', 1 )
        g.addEdge (graph, 'Cali', 'Barranquilla', 1 )
        g.addEdge (graph, 'Barranquilla','Manizales', 1 )
        g.addEdge (graph, 'Pasto','Manizales', 1 )

        print (graph)


if __name__ == "__main__":
    unittest.main()
