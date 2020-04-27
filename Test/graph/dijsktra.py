import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import indexminpq as minpq
from ADT import map as map
from ADT import graph as g
from ADT import stack as stk
import math


def comparenames (searchname, element):
    return (searchname == element['key'])

def newDijkstra(graph, s):
    """
    Crea una busqueda Dijkstra para un digrafo y un vertice origen
    """
    prime = nextPrime (g.numVertex(graph) * 2)
    search = {'graph':graph, 's':s, 'visitedMap':None, 'minpq':None}
    search['visitedMap'] = map.newMap(numelements=prime, maptype='PROBING', comparefunction=graph['comparefunction'])
    vertices = g.vertices (graph)
    itvertices = it.newIterator (vertices)
    while (it.hasNext (itvertices)):
        vert =  it.next (itvertices)
        map.put (search['visitedMap'], vert, {'marked':False,'edgeTo':None,'distTo':math.inf})
    map.put(search['visitedMap'], s, {'marked':True,'edgeTo':None,'distTo':0})
    pq = minpq.newIndexMinPQ(g.numVertex(graph), comparenames)
    search['minpq'] = pq
    minpq.insert(search['minpq'], s, 0)
    while not minpq.isEmpty(search['minpq']):
        v = minpq.delMin(pq)
        if not g.containsVertex(graph,v):
            raise Exception("Vertex ["+v+"] is not in the graph")
        edges = g.adjacentEdges(graph, v)
        if edges != None:
            edges_iter = it.newIterator (edges)
            while (it.hasNext(edges_iter)):
                edge = it.next (edges_iter)
                relax(search, edge)
    return search


def relax(search, edge):
    v = e.either(edge)
    w = e.other(edge, v)
    visited_v = map.get(search['visitedMap'], v)['value']
    visited_w = map.get(search['visitedMap'], w)
    if visited_w is None or (visited_w['value']['distTo'] > visited_v['distTo'] + e.weight(edge)):
        distToW = visited_v['distTo'] + e.weight(edge)
        map.put(search['visitedMap'], w, {'marked':True,'edgeTo':edge,'distTo':distToW})
        if minpq.contains(search['minpq'], w): 
            minpq.decreasePriority(search['minpq'], w, distToW)
        else:
            minpq.insert(search['minpq'], w, distToW)

def distTo(search, v):
    visited_v = map.get(search['visitedMap'], v)
    if visited_v==None:
        return math.inf
    return visited_v['value']['distTo']

def hasPathTo(search, v):
    visited = map.get(search['visitedMap'], v)
    if visited != None and visited['value']['marked']:
        return True
    return False

def pathTo(search, v):
    if hasPathTo(search, v)==False:
        return None
    path = stk.newStack()
    while v != search['s']:
        visited_v = map.get(search['visitedMap'],v)['value']
        edge = visited_v['edgeTo']
        stk.push(path, edge)
        v = e.either(edge)
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

