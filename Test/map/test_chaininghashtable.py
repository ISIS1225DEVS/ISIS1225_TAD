import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import chaininghashtable as ht
from DataStructures import listiterator as it


class EntryMapTest (unittest.TestCase):

    def setUp (self):
        pass


    def tearDown (self):
        pass

    def test_chainingHashTable (self):
        """
        """
        print ('--------------------------------')
        capacity = 3
        table = ht.newMap (capacity)
        print (table)

    def printTable (self, table):
        iterator = it.newIterator(table)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)



    def test_hashValue (self):
        """
        """
        print ('--------------------------------')
        table = ht.newMap ()
        hv = ht.hashValue (table, 'book1')
        print (hv)    
     
    def test_put (self):
        """
        """
        print ('--------------------------------')
        capacity = 7
        table = ht.newMap (capacity)
        ht.put (table, 'book1', 'title1')
        ht.put (table, 'book2', 'title2')
        print (table)

if __name__ == "__main__":
    unittest.main()
