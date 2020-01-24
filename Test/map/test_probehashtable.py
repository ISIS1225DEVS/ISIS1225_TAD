import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import probehashtable as ht
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
            print ("[ " + str(pos) + " ]-->", end="")
            entry = it.next(iterator)
            print (entry)
            pos += 1



    def comparekeys (self, key1, key2):
        if ( key1 == key2):
            return True
        return False

    def compareentryfunction (self, element1, element2):
        if (element1['key'] == element2['key']):
            return True
        return False


    def test_probeHashTable (self):
        """
        """
        print ('TEST--------------------------------')
        capacity = 7
        table = ht.newMap (capacity)
        self.printTable (table)


    def test_put (self):
      
        print ('TEST put--------------------------------')
        capacity = 10
        table = ht.newMap (capacity)
        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '11', 'title3', self.comparekeys)
        ht.put (table, '3', 'title4', self.comparekeys)
        ht.put (table, '12', 'title5', self.comparekeys)
        ht.put (table, '5', 'title6', self.comparekeys)
        self.printTable (table)

    def test_contains(self):
        print ('TEST Contains--------------------------------')
        capacity = 10
        table = ht.newMap (capacity)
        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '11', 'title3', self.comparekeys)
        ht.put (table, '3', 'title4', self.comparekeys)
        ht.put (table, '12', 'title5', self.comparekeys)
        ht.put (table, '5', 'title6', self.comparekeys)
        print (ht.contains(table, '1', self.comparekeys))
        print (ht.contains(table, '15', self.comparekeys))
        print (ht.contains(table, '11', self.comparekeys))


    def test_get(self):
        print ('TEST get--------------------------------')
        capacity = 10
        table = ht.newMap (capacity)
        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '11', 'title3', self.comparekeys)
        ht.put (table, '3', 'title4', self.comparekeys)
        ht.put (table, '12', 'title5', self.comparekeys)
        ht.put (table, '5', 'title6', self.comparekeys)
        entry = ht.get (table, '5', self.comparekeys)      
        print (entry) 


    def test_delete(self):
        print ('TEST remove--------------------------------')
        capacity = 10
        table = ht.newMap (capacity)
        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '11', 'title3', self.comparekeys)
        ht.put (table, '3', 'title4', self.comparekeys)
        ht.put (table, '12', 'title5', self.comparekeys)
        ht.put (table, '5', 'title6', self.comparekeys)
        self.printTable (table)
        entry = ht.remove (table, '3', self.comparekeys)      
        self.printTable (table)


    def test_getkeys (self):
        """
        """
        print ('TEST getkeys--------------------------------')
        capacity = 10
        table = ht.newMap (capacity)
        ht.put (table, '1', 'title1', self.compareentryfunction)
        ht.put (table, '2', 'title2', self.compareentryfunction)
        ht.put (table, '3', 'title3', self.compareentryfunction)
        ht.put (table, '4', 'title1', self.compareentryfunction)
        ht.put (table, '5', 'title2', self.compareentryfunction)
        ht.put (table, '6', 'title6', self.compareentryfunction)
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
        capacity = 10
        table = ht.newMap (capacity)
        ht.put (table, '1', 'title1', self.compareentryfunction)
        ht.put (table, '2', 'title2', self.compareentryfunction)
        ht.put (table, '3', 'title3', self.compareentryfunction)
        ht.put (table, '4', 'title4', self.compareentryfunction)
        ht.put (table, '5', 'title5', self.compareentryfunction)
        ht.put (table, '6', 'title6', self.compareentryfunction)
        ltset = lt.newList ()
        ltset = ht.valueSet (table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)

if __name__ == "__main__":
    unittest.main()
