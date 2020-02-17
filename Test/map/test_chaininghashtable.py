import unittest 
import config 
from DataStructures import mapentry as me
from DataStructures import mapstructure as ht
from DataStructures import listiterator as it
from ADT import list as lt


class EntryMapTest (unittest.TestCase):
    
    

    def compareentryfunction (self, element1, element2):
        if (element1 == element2['key']):
            return True
        return False



    def setUp (self):
        pass


    def tearDown (self):
        pass


    def comparekeyfunction (self, key, element):
        if ( key  == element['key']):
            return True
        return False

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
        table = ht.newMap (capacity= 7, maptype='CHAINING')

        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title4', self.compareentryfunction)
        ht.put (table, 'book5', 'title5', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)
        ht.put (table, 'book2', 'new-title 2', self.compareentryfunction)
        self.printTable (table)
        self.assertEqual (ht.size(table), 6)



    def test_get (self):
        """
        """
        table = ht.newMap (capacity= 7, maptype='CHAINING')

        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title4', self.compareentryfunction)
        ht.put (table, 'book5', 'title5', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)
        
        book = ht.get (table, 'book2', self.compareentryfunction)
        print (book)
        self.assertEqual (ht.size(table), 6)



    def test_delete (self):
        """
        """
        table = ht.newMap (capacity= 7, maptype='CHAINING')

        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title4', self.compareentryfunction)
        ht.put (table, 'book5', 'title5', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)
        self.printTable (table)
        ht.remove (table, 'book1', self.comparekeyfunction)
        self.printTable (table)



    def test_getkeys (self):
        """
        """
        table = ht.newMap (capacity= 7, maptype='CHAINING')

        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title4', self.compareentryfunction)
        ht.put (table, 'book5', 'title5', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)

        ltset = ht.keySet(table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)



    def test_getvalues (self):
        """
        """
        table = ht.newMap (capacity= 7, maptype='CHAINING')
        
        ht.put (table, 'book1', 'title1', self.compareentryfunction)
        ht.put (table, 'book2', 'title2', self.compareentryfunction)
        ht.put (table, 'book3', 'title3', self.compareentryfunction)
        ht.put (table, 'book4', 'title4', self.compareentryfunction)
        ht.put (table, 'book5', 'title5', self.compareentryfunction)
        ht.put (table, 'book6', 'title6', self.compareentryfunction)

        ltset = lt.newList ('SINGLE_LINKED_LIST')
        ltset = ht.valueSet (table)
        iterator = it.newIterator (ltset)
        while it.hasNext (iterator):
            info = it.next (iterator)
            print (info)



if __name__ == "__main__":
    unittest.main()
