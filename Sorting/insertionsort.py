
import config as cf
from TAD import list as lt
from DataStructures import listnode as node

def insertionSort (lst, lessfunction): 
    size = lst['size']
    pos1 = 1
    while pos1 < size:
        pos2 = pos1
        while (pos2 >1):
            if (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, pos2-1))):
                lt.exchange (lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
