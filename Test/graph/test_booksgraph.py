import unittest
import config as cf
import dfs
import cc
import bfs

from DataStructures import edge as e
from DataStructures import listiterator as it
#from ADT import graph as g
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


    def test_cc (self):    
    
        graph = g.newGraph(5500,self.comparenames)
        file=cf.data_dir + 'GoodReads/book_reviews.csv'
        dialect = csv.excel()
        dialect.delimiter=";"
        with open(file, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                if not g.containsVertex(graph, row['book_id']):
                    g.insertVertex (graph, row['book_id'])
                if not g.containsVertex(graph, row['user_id']):
                    g.insertVertex (graph, row['user_id'])
                g.addEdge (graph, row['book_id'], row['user_id'], row['rating'] )
        
        print('####Test_CC_books')
        print(g.numEdges(graph), g.numVertex(graph))
        ccs=cc.newCC(graph)
        print("Componentes Conectados de libros:::",ccs)


        print('####Test_DFS_books')
        search = dfs.newDFS(graph, '1420')
        path = dfs.pathTo(search,'1519')
        print(":::Route (DSF) from 1420 to 1381:")
        print(path)


        print('####Test_BFS_books')
        search=bfs.newBFS(graph, '1420')
        path = bfs.pathTo(search,'1519')
        print(":::Route (BSF) from 1420 to 1381")
        print(path)

        


    

if __name__ == "__main__":
    unittest.main()
