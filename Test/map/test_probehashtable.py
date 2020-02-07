import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import mapstructure as ht
from DataStructures import listiterator as it
from ADT import list as lt

class EntryMapTest (unittest.TestCase):

    capacity = 10
    table = ht.newMap (capacity, maptype='PROBING')


    def setUp (self):
        ht.put (self.table, '1', 'title1', self.comparekeys)
        ht.put (self.table, '2', 'title2', self.comparekeys)
        ht.put (self.table, '11', 'title3', self.comparekeys)
        ht.put (self.table, '3', 'title4', self.comparekeys)
        ht.put (self.table, '12', 'title5', self.comparekeys)
        ht.put (self.table, '5', 'title6', self.comparekeys)


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


    def test_contains(self):
        self.assertTrue   (ht.contains(self.table, '1', self.comparekeys))
        self.assertFalse  (ht.contains(self.table, '15', self.comparekeys))
        self.assertTrue   (ht.contains(self.table, '11', self.comparekeys))


    def test_get(self):
        entry = ht.get (self.table, '5', self.comparekeys)      
        print (entry) 


    def test_delete(self):
        self.printTable (self.table)
        entry = ht.remove (self.table, '3', self.comparekeys)      
        self.printTable (self.table)


    def test_getkeys (self):
        """
        """
        ltset = lt.newList ('SINGLE_LINKED_LIST')
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
