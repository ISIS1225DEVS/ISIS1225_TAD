import config
import math
from DataStructures import adjlist as g
from DataStructures import listiterator as it
from ADT import queue as q
from ADT import map as map
from DataStructures import edge as e
from ADT import stack as stk
from ADT import list as lt




def newDFS(graph, source):
    """
    Crea una busqueda DFS para un grafo y un vertice origen
    """
    prime = nextPrime (g.numVertex(graph) * 2)
    search={'graph':graph, 's':source, 'visitedMap':None}   
    search['visitedMap'] = map.newMap(capacity=prime, maptype='PROBING', comparefunction=graph['comparefunction'])
    map.put(search['visitedMap'],source, {'marked':True,'edgeTo':None})
    dfs(search, source)
    return search

def dfs (search, v):
    adjs = g.adjacents(search['graph'],v)
    adjs_iter = it.newIterator (adjs)
    while (it.hasNext(adjs_iter)):
        w = it.next (adjs_iter)
        visited_w = map.get(search['visitedMap'], w)
        if visited_w == None:
            map.put(search['visitedMap'], w, {'marked':True, 'edgeTo':v})
            dfs(search, w)


def hasPathTo(search, v):
    element = map.get(search['visitedMap'],v)
    if element and element['value']['marked']==True:
        return True
    return False



def pathTo(search, v):
    if hasPathTo(search, v)==False:
        return None
    path= stk.newStack()
    while v != search['s']:
        stk.push(path,v)
        v = map.get(search['visitedMap'],v)['value']['edgeTo']
    stk.push(path,search['s'])
    return path



# Function to return the smallest  
# prime number greater than N 
# # This code is contributed by Sanjit_Prasad  

def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
      
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True

def nextPrime(N): 
  
    # Base case  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
  
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 


def comparenames (searchname, element):
    return (searchname == element['key'])


if __name__ ==  "__main__" :
    graph = g.newGraph(7,comparenames)

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

    search = newDFS(graph,'Bogota')


    print ('A Cali', hasPathTo(search, 'Cali'))
    print ('A Cucuta', hasPathTo(search,'Cucuta'))
    pathManizales= pathTo(search,'Manizales')
    print('DSF::roadToManizales',pathManizales)