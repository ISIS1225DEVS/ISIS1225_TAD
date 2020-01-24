import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import chaininghashtable as ht
from DataStructures import listiterator as it
from ADT import list as lt


class EntryMapTest (unittest.TestCase):

    def setUp (self):
        pass


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



    def compareentryfunction (self, element1, element2):
        if (element1['key'] == element2['key']):
            return True
        return False


    def comparekeyfunction (self, key, element):
        if ( key  == element['key']):
            return True
        return False

     
    def test_put (self):
        """
        """
        print ('TEST put--------------------------------')
        capacity = 5
        table = ht.newMap (capacity)
        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title1', self.compareentryfunction)
        ht.put (table, 'book5', 'title2', self.compareentryfunction)
        ht.put (table, 'book6', 'title3', self.compareentryfunction)
        self.printTable (table)

    def test_delete (self):
        """
        """
        print ('TEST delete--------------------------------')
        capacity = 5
        table = ht.newMap (capacity)
        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title1', self.compareentryfunction)
        ht.put (table, 'book5', 'title2', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)
        self.printTable (table)
        ht.remove (table, 'book5', self.comparekeyfunction)
        self.printTable (table)

    def test_getkeys (self):
        """
        """
        print ('TEST getkeys--------------------------------')
        capacity = 5
        table = ht.newMap (capacity)
        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title1', self.compareentryfunction)
        ht.put (table, 'book5', 'title2', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)
        ltset = lt.newList ()
        ltset = ht.keySet(table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)


    def test_getvalues (self):
        """
        """
        print ('TEST values--------------------------------')
        capacity = 5
        table = ht.newMap (capacity)
        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title4', self.compareentryfunction)
        ht.put (table, 'book5', 'title5', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)
        ltset = lt.newList ()
        ltset = ht.valueSet (table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)


if __name__ == "__main__":
    unittest.main()
