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
    

    def test_DSF (self):

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
        
        marked = lt.newList ()
        self.dfs (graph, 'Bogota', marked)
        print (marked)


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
        
        lst = self.bfs (graph, 'Bogota')
        print (lst)


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
