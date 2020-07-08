import unittest
import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
from ADT import stack as s 
from ADT import map as m 
from ADT import list as lt


class KosarajuTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])

    def comparelst (self, searchname, element):
        return (searchname == element)


    def test_kosaraju (self):

        graph = g.newGraph ( 12, self.comparenames, directed=True )
        idscc = m.newMap (12, maptype= 'PROBING', comparefunction=self.comparenames)
        
        pre = q.newQueue()
        post = q.newQueue()
        reversepost = s.newStack()
        marked = m.newMap (12, comparefunction=self.comparenames)

        grmarked = m.newMap (12, maptype= 'PROBING', comparefunction=self.comparenames)
        grpre = q.newQueue()
        grpost = q.newQueue()
        grreversepost = s.newStack()
        
        # se inicializa el grafo
        self.loadgraph  (graph)                    
        self.assertEqual (g.numVertex(graph), 12)
        self.assertEqual (g.numEdges(graph), 14)
        
        # Se calcula el grafo reverso de G
        greverse = self.reverse (graph)                
        self.assertEqual (g.numVertex(greverse), 12)
        self.assertEqual (g.numEdges(greverse), 14)

        # Se recorre el grafor reverso de G, utilizando DepthFirstOrder.
        self.dfo (greverse, grmarked, grpre, grpost, grreversepost)
        lst = self.lstReversePost (grreversepost)

        #lst contiene los vertices retornados por reversepost (G-reverso) 
        #Se recorre el grafo en el orden dado por reverspost (G-reverso)
        iterlst = it.newIterator (lst)
        scc = 1
        while (it.hasNext(iterlst)):
            vert = it.next(iterlst)
            if not m.contains (marked, vert):
                self.sccCount (graph, vert, marked, idscc, scc)
                scc += 1

        self.assertTrue (self.stronglyConnected(idscc, 'Pedro', 'Maria'))
        self.assertTrue (self.stronglyConnected(idscc, 'Martin', 'Gloria'))
        self.assertTrue (self.stronglyConnected(idscc, 'Susana', 'Tere'))

        self.assertFalse (self.stronglyConnected(idscc, 'Pedro', 'Gloria'))
        self.assertFalse (self.stronglyConnected(idscc, 'Camila', 'Jose'))
        self.assertFalse (self.stronglyConnected(idscc, 'Gloria', 'Luz'))


    
    def loadgraph (self, graph):
        """
        Crea el grafo con la informacion de prueba
        """
        g.insertVertex (graph, 'Pedro')
        g.insertVertex (graph, 'Maria')
        g.insertVertex (graph, 'Carol')
        g.insertVertex (graph, 'Laura')
        g.insertVertex (graph, 'Felipe')
        g.insertVertex (graph, 'Jose')
        g.insertVertex (graph, 'Martin')
        g.insertVertex (graph, 'Camila')
        g.insertVertex (graph, 'Gloria')
        g.insertVertex (graph, 'Luz')
        g.insertVertex (graph, 'Tere')
        g.insertVertex (graph, 'Susana')
        g.addEdge (graph, 'Pedro', 'Jose')
        g.addEdge (graph, 'Jose', 'Felipe')
        g.addEdge (graph, 'Felipe', 'Laura')
        g.addEdge (graph, 'Laura', 'Carol')
        g.addEdge (graph, 'Carol', 'Maria')
        g.addEdge (graph, 'Maria', 'Pedro')
        g.addEdge (graph, 'Camila', 'Jose')
        g.addEdge (graph, 'Camila', 'Martin')
        g.addEdge (graph, 'Martin', 'Gloria')
        g.addEdge (graph, 'Gloria', 'Camila')
        g.addEdge (graph, 'Gloria', 'Luz')
        g.addEdge (graph, 'Luz', 'Tere')
        g.addEdge (graph, 'Tere', 'Susana')
        g.addEdge (graph, 'Susana', 'Luz')
        


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
       

    def sccCount (self, graph, vert, marked, idscc, scc):
        """
         Este algoritmo cuenta el número de componentes conectados.
         Deja en idscc, el número del componente al que pertenece cada vértice
        """
        m.put (marked, vert, True)
        m.put (idscc, vert, scc)
        lstadjacents = g.adjacents(graph, vert)
        adjiterator = it.newIterator (lstadjacents)
        while it.hasNext(adjiterator):
            adjvert = it.next (adjiterator)
            if not m.contains (marked, adjvert):
                self.sccCount (graph, adjvert, marked, idscc, scc)


    def stronglyConnected (self, idscc, verta, vertb):
        """
         Dados dos vértices, informa si están fuertemente conectados o no.
        """
        if m.get(idscc, verta)['value'] == m.get(idscc, vertb)['value']:
            return True
        return False



    def reverse (self, graph):
        """
         Retornar el reverso del grafo graph
        """
        greverse = g.newGraph ( 12, self.comparenames, directed=True )

        lstvert = g.vertices (graph)
        itervert = it.newIterator (lstvert)
        while it.hasNext (itervert) :
            vert = it.next (itervert)
            g.insertVertex(greverse,vert)
        
        itervert = it.newIterator (lstvert)
        while it.hasNext (itervert) :
            vert = it.next (itervert)
            lstadj = g.adjacents (graph, vert)
            iteradj = it.newIterator(lstadj)
            while it.hasNext (iteradj) :
                adj = it.next (iteradj)
                g.addEdge (greverse, adj, vert)
        return greverse
    

    def lstReversePost (self,reversepost):
        """
        Retorna una lista con el orden dado por la pila reversepost
        """
        lstrp = lt.newList ()
        while not s.isEmpty(reversepost):
            lt.addLast (lstrp, s.pop (reversepost))
        return lstrp


if __name__ == "__main__":
    unittest.main()
