import config as cf
from TAD import list as lt
from DataStructures import listnode as node


def shellSort(lst, lessfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:
        h = 3*h + 1
    while (h >= 1):
        for i in range (h,n):
            j = i
            while (j>=h) and lessfunction (lt.getElement(lst,j+1),lt.getElement(lst,j-h+1)):
                lt.exchange (lst, j+1, j-h+1)
                j -=h
        h //=3