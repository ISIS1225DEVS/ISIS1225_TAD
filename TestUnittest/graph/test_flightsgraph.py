import unittest
import config as cf
import dfs
import cc
import bfs

from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
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


    #Funciones para probar los datos de vuelos


    def test_cc_flights (self):    
    
        graph = g.newGraph(111353,self.comparenames)
        nodes =  cf.data_dir + 'flights/flights_nodes.csv'    
        dialect = csv.excel()
        dialect.delimiter=";"
        with open(nodes, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                g.insertVertex (graph, row['VERTEX'])
        
        flights =  cf.data_dir + 'flights/flights_edges.csv'
        with open(flights, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                g.addEdge (graph, row['SOURCE'], row['DEST'], row['ARRIVAL_DELAY'] )
        
        print('####Test_CC_flights')
        print(g.numEdges(graph), g.numVertex(graph))
        ccs=cc.newCC(graph)
        print("Componentes Conectados de Vuelos:::",ccs)


        print('####Test_DFS_flights')
        search = dfs.newDFS(graph, 'ALB-11-5')
        routeALB_SMF = dfs.pathTo(search,'SMF-11-5')
        print(":::Route (DSF) from ALB-11-5 to SMF-11-5:")
        print(routeALB_SMF)


        print('####Test_BFS_flights')
        search=bfs.newBFS(graph, 'ALB-11-5')
        routeALB_SMF = bfs.pathTo(search,'SMF-11-5')
        print(":::Route (BSF) from ALB-11-5 to SMF-11-5")
        print(routeALB_SMF)

        


    

if __name__ == "__main__":
    unittest.main()
