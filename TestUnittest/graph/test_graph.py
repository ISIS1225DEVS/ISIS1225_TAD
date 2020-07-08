import unittest
import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
from ADT import list as lt


class GraphTest (unittest.TestCase):

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
        self.assertEqual ('Bogota', e.either(edge))
        self.assertEqual ('Cali', e.other(edge, e.either(edge)))
        self.assertEqual  (e.weight(edge), 0)


    def test_insertVertex (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')
        self.assertEqual (g.numVertex(graph),7)


    def test_addEdges (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')
        self.assertEqual (g.numVertex(graph),7)

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
        

        lst = g.vertices (graph)
        self.assertEqual (lt.size (lst), 7)

        lst = g.edges (graph)
        self.assertEqual (lt.size (lst), 10)

        degree = g.degree (graph, 'Bogota')
        self.assertEqual (degree, 4)

        edge = g.getEdge (graph, 'Bogota', 'Medellin')

        lst = g.adjacents (graph, 'Bogota')
        self.assertEqual (lt.size (lst), 4)

        num = g.degree (graph, 'Bogota')
        self.assertEqual (num, 4)
    
        resp = g.containsVertex (graph,'Bogota')
        self.assertTrue(resp)
        resp = g.containsVertex (graph,'Pereira' )
        self.assertFalse(resp)





    def test_DSF (self):

        graph = g.newGraph(7,self.comparenames)

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
        
        marked = lt.newList ()
        self.dfs (graph, 'Bogota', marked)


    def dfs (self, graph, vertex, marked):
        
        lt.addLast (marked, vertex)

        lst = g.adjacents (graph, vertex)
        iter = it.newIterator (lst)
        while (it.hasNext(iter)):
            adjacent = it.next (iter)
            if not (lt.isPresent (marked, adjacent, self.comparelst)):
                #Aca se visita el vertice y se realiza alguna operación de interes
                self.dfs (graph, adjacent,marked)




    def test_BSF (self):

        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal' )
        g.addEdge (graph, 'Bogota', 'Medellin' )
        g.addEdge (graph, 'Bogota', 'Pasto' )
        g.addEdge (graph, 'Bogota', 'Cali')
        g.addEdge (graph, 'Yopal', 'Medellin' )
        g.addEdge (graph, 'Medellin', 'Pasto' )
        g.addEdge (graph, 'Cali', 'Pasto')
        g.addEdge (graph, 'Cali', 'Barranquilla')
        g.addEdge (graph, 'Barranquilla','Manizales')
        g.addEdge (graph, 'Pasto','Manizales')
        
        lst = self.bfs (graph, 'Bogota')


    def bfs (self, graph, vertex):
        marked = lt.newList ()
        queue =  q.newQueue()

        lt.addLast (marked, vertex)
        q.enqueue (queue, vertex)
     
        while not (q.isEmpty(queue)):
            v = q.dequeue (queue)
            lstadj = g.adjacents (graph, v)
            iter = it.newIterator (lstadj)
            while (it.hasNext(iter)):
                adj = it.next(iter)
                if not (lt.isPresent (marked, adj, self.comparelst)):
                    lt.addLast (marked, adj)
                    #Aca se visita el vertice y se realiza alguna operación de interes
                    q.enqueue (queue, adj)
        return marked


if __name__ == "__main__":
    unittest.main()
