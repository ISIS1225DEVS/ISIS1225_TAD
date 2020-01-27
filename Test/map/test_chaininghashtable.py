import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import chaininghashtable as ht
from DataStructures import listiterator as it
from ADT import list as lt


class EntryMapTest (unittest.TestCase):
    
    capacity = 5
    table = ht.newMap (capacity)



    def compareentryfunction (self, element1, element2):
        if (element1['key'] == element2['key']):
            return True
        return False



    def setUp (self):
        ht.put (self.table, 'book1', 'title1', self.compareentryfunction)
        ht.put (self.table, 'book2', 'title2', self.compareentryfunction)
        ht.put (self.table, 'book3', 'title3', self.compareentryfunction)
        ht.put (self.table, 'book4', 'title4', self.compareentryfunction)
        ht.put (self.table, 'book5', 'title5', self.compareentryfunction)
        ht.put (self.table, 'book6', 'title6', self.compareentryfunction)

    def tearDown (self):
        pass


    def printTable (self, table):
        print ('TABLE:')
        print ('Capacity: ' + str(table['capacity']))
        print ('Scale: ' + str(table['scale']))
        print ('Shift: ' + str(table['shift']))
        print ('Prime: ' + str(table['prime']))
        iterator = it.newIterator(table['table'])
        pos = 1
        while  it.hasNext(iterator):
            bucket = it.next(iterator)
            bucketiterator = it.newIterator(bucket)
            print ("[ " + str(pos) + " ]-->", end="")
            while  it.hasNext(bucketiterator):
                entry = it.next(bucketiterator)
                print (entry, end="")
                print ("-->",end="")
            print ("None")
            pos += 1



    def test_put (self):
        """
        """
        ht.put (self.table, 'book2', 'new-title 2', self.compareentryfunction)
        self.printTable (self.table)
        self.assertEqual (ht.size(self.table), 6)



    def comparekeyfunction (self, key, element):
        if ( key  == element['key']):
            return True
        return False



    def test_delete (self):
        """
        """
        self.printTable (self.table)
        ht.remove (self.table, 'book1', self.comparekeyfunction)
        self.printTable (self.table)



    def test_getkeys (self):
        """
        """
        ltset = ht.keySet(self.table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)



    def test_getvalues (self):
        """
        """
        ltset = lt.newList ('SINGLE_LINKED_LIST')
        ltset = ht.valueSet (self.table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)



if __name__ == "__main__":
    unittest.main()
