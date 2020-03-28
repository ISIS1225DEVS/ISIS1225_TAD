import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import mapstructure as ht
from DataStructures import listiterator as it
from ADT import list as lt

class EntryMapTest (unittest.TestCase):

    

    def comparekeys (self, key, element):
        if ( key == element['key']):
            return True
        return False


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


    def test_contains(self):

        capacity = 10
        table = ht.newMap (capacity, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '11', 'title3')
        ht.put (table, '3', 'title4')
        ht.put (table, '12', 'title5')
        ht.put (table, '5', 'title6')

        self.assertTrue   (ht.contains(table, '1'))
        self.assertFalse  (ht.contains(table, '15'))
        self.assertTrue   (ht.contains(table, '11'))


    def test_get(self):
        capacity = 10
        table = ht.newMap (capacity, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '11', 'title3')
        ht.put (table, '3', 'title4')
        ht.put (table, '12', 'title5')
        ht.put (table, '5', 'title6')

        entry = ht.get (table, '5')      
        print (entry) 


    def test_delete(self):
        capacity = 10
        table = ht.newMap (capacity, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '11', 'title3')
        ht.put (table, '3', 'title4')
        ht.put (table, '12', 'title5')
        ht.put (table, '5', 'title6')
        self.printTable (table)
        entry = ht.remove (table, '3')      
        self.printTable (table)


    def test_getkeys (self):
        """
        """
        capacity = 10
        table = ht.newMap (capacity, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '11', 'title3')
        ht.put (table, '3', 'title4')
        ht.put (table, '12', 'title5')
        ht.put (table, '5', 'title6')

        ltset = lt.newList ('SINGLE_LINKED_LIST')
        ltset = ht.keySet(table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)


    def test_getvalues (self):
        """
        """
        capacity = 10
        table = ht.newMap (capacity, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '11', 'title3')
        ht.put (table, '3', 'title4')
        ht.put (table, '12', 'title5')
        ht.put (table, '5', 'title6')

        ltset = lt.newList ('SINGLE_LINKED_LIST')
        ltset = ht.valueSet (table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)
            

if __name__ == "__main__":
    unittest.main()
