import config as cf
from TAD import list as lt
from DataStructures import listnode as node

def selectionSort (lst, lessfunction): 
    size = lst['size']
    pos1 = 1
    while pos1 < size:
        minimum = pos1
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, minimum))):
                minimum = pos2
            pos2 += 1
        lt.exchange (lst, pos1, minimum)
        pos1 += 1