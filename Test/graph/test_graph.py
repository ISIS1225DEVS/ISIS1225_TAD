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


    def test_newEdge (self):
        edge = e.newEdge (1,1,1)
        print (edge)

    def test_edgeMethods (self):
        edge = e.newEdge ('Bogota','Cali',4)

        print (e.either(edge))
        print (e.other(edge))
        print (e.weight(edge))


    def test_newGrapgh (self):
        graph = g.newGraph()

        print (graph)



if __name__ == "__main__":
    unittest.main()
