import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import mapstructure as ht
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
        print ('Size: ' + str(table['size']))
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
        table = ht.newMap (capacity=17, maptype='PROBING')

        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '3', 'title3', self.comparekeys)
        ht.put (table, '4', 'title4', self.comparekeys)
        ht.put (table, '5', 'title5', self.comparekeys)
        ht.put (table, '6', 'title6', self.comparekeys)

        self.assertTrue   (ht.contains(table, '1', self.comparekeys))
        self.assertFalse  (ht.contains(table, '15', self.comparekeys))
        self.assertTrue   (ht.contains(table, '6', self.comparekeys))
        self.assertEqual (ht.size(table), 6)


    def test_get(self):
        table = ht.newMap (capacity=17, maptype='PROBING')

        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '3', 'title3', self.comparekeys)
        ht.put (table, '4', 'title4', self.comparekeys)
        ht.put (table, '5', 'title5', self.comparekeys)
        ht.put (table, '6', 'title6', self.comparekeys)
        self.assertEqual (ht.size(table), 6)

        entry = ht.get (table, '5', self.comparekeys)      
        print (entry) 



    def test_delete(self):
        table = ht.newMap (capacity=17, maptype='PROBING')

        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '3', 'title3', self.comparekeys)
        ht.put (table, '4', 'title4', self.comparekeys)
        ht.put (table, '5', 'title5', self.comparekeys)
        ht.put (table, '6', 'title6', self.comparekeys)
        self.assertEqual (ht.size(table), 6)

        self.printTable (table)
        entry = ht.remove (table, '3', self.comparekeys)  
        self.assertEqual (ht.size(table), 5)    
        entry = ht.get (table, '3', self.comparekeys)  
        self.assertIsNone (entry)
        self.printTable (table)


    def test_getkeys (self):
        """
        """
        table = ht.newMap (capacity=17, maptype='PROBING')

        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '3', 'title3', self.comparekeys)
        ht.put (table, '4', 'title4', self.comparekeys)
        ht.put (table, '5', 'title5', self.comparekeys)
        ht.put (table, '6', 'title6', self.comparekeys)

        ltset = lt.newList ('SINGLE_LINKED')
        ltset = ht.keySet(table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)


    def test_getvalues (self):
        """
        """
        table = ht.newMap (capacity=17, maptype='PROBING')

        ht.put (table, '1', 'title1', self.comparekeys)
        ht.put (table, '2', 'title2', self.comparekeys)
        ht.put (table, '3', 'title3', self.comparekeys)
        ht.put (table, '4', 'title4', self.comparekeys)
        ht.put (table, '5', 'title5', self.comparekeys)
        ht.put (table, '6', 'title6', self.comparekeys)

        ltset = lt.newList ('SINGLE_LINKED')
        ltset = ht.valueSet (table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)
            

if __name__ == "__main__":
    unittest.main()
