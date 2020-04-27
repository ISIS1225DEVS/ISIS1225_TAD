import unittest
import config
import math 
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
from ADT import stack as stack 
from ADT import map as m 
from ADT import list as lt
from ADT import indexminpq as iminpq


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
        distTo = m.newMap (7, maptype= 'PROBING', comparefunction=self.comparekeys)
        edgeTo = m.newMap (7, maptype= 'PROBING', comparefunction=self.comparekeys)
        pq = iminpq.newIndexMinPQ (7, self.comparekeys)

        # se inicializa el grafo
        self.loadgraph  (graph)     
        self.assertEqual (g.numVertex(graph), 7)
        self.assertEqual (g.numEdges(graph), 12)    

        self.dijkstraSP (graph, 'Bogota', distTo, edgeTo, pq)           

        

    def dijkstraSP (self, graph, s, distTo, edgeTo, pq):
        vertices = g.vertices (graph)
        itvertices = it.newIterator (vertices)
        while (it.hasNext (itvertices)):
            vert =  it.next (itvertices)
            m.put (distTo, vert, math.inf)
        m.put (distTo, s, 0.0)
        iminpq.insert (pq,s, 0.0)
        while (not iminpq.isEmpty(pq)):
            self.relax (graph, iminpq.delMin(pq)['key'], distTo, edgeTo, pq)


        self.assertTrue (self.hasPathTo ('Bogota', 'Cali', distTo))
        self.assertEqual (self.distTo ('Bogota', 'Cali', distTo), 7.4)

        path = self.pathTo ('Bogota','Cali', edgeTo)
        print ("El camino de costo minimo es: ")
        suma = 0
        while not stack.isEmpty (path):
            paso = stack.pop(path)
            suma += paso['weight']
            print (paso['vertexA'] + "-->" + paso['vertexB'] + " costo: " + str(paso['weight']))
        print ("Total: " + str (suma))

    

    def relax (self, graph, v, distTo, edgeTo, pq):
        adjacents = g.adjacentEdges (graph, v)
        itadjacents = it.newIterator (adjacents)
        while (it.hasNext(itadjacents)):
            edge = it.next (itadjacents)
            w = e.other (edge, v)
            distw = m.get (distTo, w)['value']
            distv = m.get (distTo, v)['value']
            if (distw > distv + e.weight (edge)):
                m.put (distTo, w, distv + e.weight (edge))
                m.put (edgeTo, w, edge)
                if (iminpq.contains (pq, w)):
                    iminpq.changeKeyIndex (pq, w, distv + e.weight (edge))
                else:
                    iminpq.insert (pq, w, distv + e.weight (edge))
        return graph



    def hasPathTo (self, source, dest, distTo):
        element = m.get (distTo, dest)
        return (element['value'] != math.inf)



    def distTo (self, source, dest, distTo):
        element = m.get (distTo, dest)
        return (element['value'])


    def pathTo (self, source, dest, edgeTo):
        path = stack.newStack()
        finish = False
        while (not finish):
            edge = m.get (edgeTo,  dest)
            stack.push (path, edge['value'])
            if (e.either(edge['value']) == source):
                finish = True
            dest = e.either(edge['value'])
        return path







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
