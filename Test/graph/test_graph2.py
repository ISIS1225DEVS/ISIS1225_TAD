import unittest
import config
from DataStructures import edge as e
from DataStructures import listiterator as it
#from ADT import graph as g
from DataStructures import adjlistV2 as g
from ADT import queue as q
from ADT import map as map

from ADT import stack as stk
from ADT import list as lt
import csv


class GraphTest (unittest.TestCase):

    def setUp (self):
        pass



    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])

    def comparelst (self, searchname, element):
        return (searchname == element)


    def atest_newEdge (self):
        edge = e.newEdge (1,1,1)
        print (edge)


    def atest_edgeMethods (self):
        edge = e.newEdge ('Bogota','Cali',4)

        print (e.either(edge))
        print (e.other(edge, e.either(edge)))
        print (e.weight(edge))


    def atest_insertVertex (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')


    def atest_addEdges (self):
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

        degree = g.degree (graph, 'Bogota')
        self.assertEqual (degree, 4)


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
        print ('DSF:',marked)

    def test_BSF2 (self):

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
        
        self.bfs2 (graph, 'Bogota')
        print ('::BFS2: A Cali', self.hasPathTo(graph, 'Cali'))
        print ('::BFS2: A Cucuta', self.hasPathTo(graph, 'Cucuta'))   
        pathManizales = self.pathTo(graph, 'Bogota', 'Manizales')
        print('::BFS2: pathToManizales:',pathManizales)

    def dfs (self, graph, vertex, marked):
        
        lt.addLast (marked, vertex)

        lst = g.adjacents (graph, vertex)
        iter = it.newIterator (lst)
        while (it.hasNext(iter)):
            adjacent = it.next (iter)
            if not (lt.isPresent (marked, adjacent, self.comparelst)):
                #Aca se visita el vertice y se realiza alguna operación de interes
                self.dfs (graph, adjacent,marked)




    def atest_BSF (self):

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


    

    def test_dfs2 (self):

        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')
        
        g.insertVertex (graph, 'Cucuta')
        g.insertVertex (graph, 'Bucaramanga')


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
        g.addEdge (graph, 'Cucuta','Bucaramanga', 1 )

        
        self.dfs2 (graph, 'Bogota')
        print ('A Cali', self.hasPathTo(graph, 'Cali'))
        print ('A Cucuta', self.hasPathTo(graph, 'Cucuta'))
        pathManizales=self.pathTo(graph, 'Bogota', 'Manizales')
        print('DSF2::roadToManizales',pathManizales)


    def atest_failed_dfs (self):

        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')
        
        g.insertVertex (graph, 'Cucuta')
        g.insertVertex (graph, 'Bucaramanga')


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
        g.addEdge (graph, 'Cucuta','Bucaramanga', 1 )

        
        self.dfs2 (graph, 'Bogota')
        pathCucuta=self.pathTo(graph, 'Bogota', 'Cucuta')
        print('roadToCucuta',pathCucuta)


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


    def atest_cc2 (self):

        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')
        
        g.insertVertex (graph, 'Cucuta')
        g.insertVertex (graph, 'Bucaramanga')


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
        g.addEdge (graph, 'Cucuta','Bucaramanga', 1 )

        
        cc = self.cc(graph)
        print ('Connected Components: ', cc)


    #Funciones para probar los datos de vuelos


    def atest_cc_flights (self):    
    
        graph = g.newGraph(111353,self.comparenames)
        nodes = '/Users/kmilo/Documents/PhD/Sem8/Docencia/flights_nodes.csv'    
        dialect = csv.excel()
        dialect.delimiter=";"
        with open(nodes, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                g.insertVertex (graph, row['VERTEX'])
        
        flights = '/Users/kmilo/Documents/PhD/Sem8/Docencia/flights_edges.csv'
        with open(flights, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                info = {'dist':row['DISTANCE'], 'delay':row['ARRIVAL_DELAY']}
                g.addEdge (graph, row['SOURCE'], row['DEST'], info )
        print('####test_flights')
        print(g.numEdges(graph), g.numVertex(graph))
        self.assertEqual (lt.size (g.adjacents(graph,'EWR-11-5')), 71)

        ccs=self.cc(graph)
        print("Componentes Conectados de Vuelos:::",ccs)
        

        #print()


    def atest_dfs2_flights (self):    
        graph = g.newGraph(111353,self.comparenames)
        nodes = '/Users/kmilo/Documents/PhD/Sem8/Docencia/flights_nodes.csv'    
        dialect = csv.excel()
        dialect.delimiter=";"
        with open(nodes, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                g.insertVertex (graph, row['VERTEX'])
        
        flights = '/Users/kmilo/Documents/PhD/Sem8/Docencia/flights_edges.csv'
        with open(flights, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                info = {'dist':row['DISTANCE'], 'delay':row['ARRIVAL_DELAY']}
                g.addEdge (graph, row['SOURCE'], row['DEST'], info )
        print('####test_flights')
        print(g.numEdges(graph), g.numVertex(graph))
        self.dfs2(graph, 'ALB-11-5')
        routeALB2SMF = self.pathTo(graph,'ALB-11-5', 'SMF-11-5')
        print("Route from ALB-11-5 to SMF-11-5")
        print(routeALB2SMF)
        #print()

    def atest_bfs_flights (self):
        graph = g.newGraph(111353,self.comparenames)
        nodes = '/Users/kmilo/Documents/PhD/Sem8/Docencia/flights_nodes.csv'    
        dialect = csv.excel()
        dialect.delimiter=";"
        with open(nodes, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                g.insertVertex (graph, row['VERTEX'])
        
        flights = '/Users/kmilo/Documents/PhD/Sem8/Docencia/flights_edges.csv'
        with open(flights, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                info = {'dist':row['DISTANCE'], 'delay':row['ARRIVAL_DELAY']}
                g.addEdge (graph, row['SOURCE'], row['DEST'], info )
        print('####test_flights')
        print(g.numEdges(graph), g.numVertex(graph))
        self.bfs(graph, 'ALB-11-5')
        routeALB2SMF = self.pathTo(graph,'ALB-11-5', 'SMF-11-5')
        print("Route from ALB-11-5 to SMF-11-5")
        print(routeALB2SMF)
    
    

    def hasPathTo(self, graph, vertex):
        element = map.get(graph['vertices'],vertex)
        if element and element['value']['marked']==True:
            return True
        return False



    def pathTo(self, graph, source, vertex):
        if self.hasPathTo(graph, vertex)==False:
            return None
        path= stk.newStack()
        step = vertex
        while step != source:
            stk.push(path,step)
            step=map.get(graph['vertices'],step)['value']['edgeTo']
        stk.push(path,source)
        return path


    def dfs2 (self, graph, vertex):                
        curr_vertex = map.get(graph['vertices'],vertex)
        curr_vertex['value']['marked']=True
        map.put(graph['vertices'],curr_vertex['key'],curr_vertex['value'])
        lst = curr_vertex['value']['edges']
        edge_iter = it.newIterator (lst)
        while (it.hasNext(edge_iter)):
            adj_ed = it.next (edge_iter)
            adj_vert = map.get(graph['vertices'], adj_ed['vertexB'])
            if adj_vert['value']['marked']==False:
                adj_vert['value']['edgeTo']=vertex
                map.put(graph['vertices'],adj_vert['key'],adj_vert['value'])
                self.dfs2(graph, adj_vert['key'])

    def bfs2(self, graph, vertex):
        #marked = lt.newList ()
        queue =  q.newQueue()
        s = map.get(graph['vertices'],vertex)
        s['value']['marked']=True
        s['value']['distTo']=0
        map.put(graph['vertices'],s['key'],s['value'])
        #lt.addLast (marked, vertex)
        q.enqueue (queue, s)
     
        while not (q.isEmpty(queue)):
            v = q.dequeue (queue)
            lstadj = g.adjacents (graph, v['key'])
            #lstadj = v['value']['edges']

            iter = it.newIterator (lstadj)
            while (it.hasNext(iter)):
                adj = it.next(iter)
                w = map.get(graph['vertices'], adj)
                if w['value']['marked']==False:
                    w['value']['edgeTo']=v['key']
                    w['value']['distTo']=v['value']['distTo']+1
                    w['value']['marked']=True
                    map.put(graph['vertices'],w['key'],w['value'])
                    q.enqueue (queue, w)

    def cc(self, graph):
        #size = new int[G.V()]
        #for (int v = 0; v < G.V(); v++):
        vertices = g.vertices(graph)
        ccount=0
        viter = it.newIterator (vertices)
        while (it.hasNext(viter)):
            v = it.next(viter)
            vertex=map.get(graph['vertices'],v)
            if vertex['value']['marked']==False:
                self.dfs2(graph, vertex['key'])
                ccount+=1
        return ccount
            
        
    



if __name__ == "__main__":
    unittest.main()
