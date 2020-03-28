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


    def comparekeys (self, key, element):
        if ( key == element['key']):
            return True
        return False


    def compareentryfunction (self, element1, element2):
        if (element1 == element2):
            return True
        return False


    def test_contains(self):
        table = ht.newMap (capacity=17, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '3', 'title3')
        ht.put (table, '4', 'title4')
        ht.put (table, '5', 'title5')
        ht.put (table, '6', 'title6')

        self.assertTrue   (ht.contains(table, '1'))
        self.assertFalse  (ht.contains(table, '15'))
        self.assertTrue   (ht.contains(table, '6'))
        self.assertEqual (ht.size(table), 6)


    def test_get(self):
        table = ht.newMap (capacity=17, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '3', 'title3')
        ht.put (table, '4', 'title4')
        ht.put (table, '5', 'title5')
        ht.put (table, '6', 'title6')
        self.assertEqual (ht.size(table), 6)

        entry = ht.get (table, '5')      
        print (entry) 



    def test_delete(self):
        table = ht.newMap (capacity=17, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '3', 'title3')
        ht.put (table, '4', 'title4')
        ht.put (table, '5', 'title5')
        ht.put (table, '6', 'title6')
        self.assertEqual (ht.size(table), 6)

        self.printTable (table)
        entry = ht.remove (table, '3')  
        self.assertEqual (ht.size(table), 5)    
        entry = ht.get (table, '3')  
        self.assertIsNone (entry)
        self.printTable (table)


    def test_getkeys (self):
        """
        """
        table = ht.newMap (capacity=17, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '3', 'title3')
        ht.put (table, '4', 'title4')
        ht.put (table, '5', 'title5')
        ht.put (table, '6', 'title6')

        ltset = lt.newList ('SINGLE_LINKED')
        ltset = ht.keySet(table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)


    def test_getvalues (self):
        """
        """
        table = ht.newMap (capacity=17, maptype='PROBING', comparefunction=self.comparekeys)

        ht.put (table, '1', 'title1')
        ht.put (table, '2', 'title2')
        ht.put (table, '3', 'title3')
        ht.put (table, '4', 'title4')
        ht.put (table, '5', 'title5')
        ht.put (table, '6', 'title6')

        ltset = lt.newList ('SINGLE_LINKED')
        ltset = ht.valueSet (table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)
            

if __name__ == "__main__":
    unittest.main()
