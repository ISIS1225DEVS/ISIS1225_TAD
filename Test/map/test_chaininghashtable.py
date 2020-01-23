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
        print ('TEST--------------------------------')
        capacity = 3
        table = ht.newMap (capacity)

    def printTable (self, table):
        iterator = it.newIterator(table['table'])
        print ('TABLE:')
        print ('Capacity: ' + str(table['capacity']))
        print ('Scale: ' + str(table['scale']))
        print ('Shift: ' + str(table['shift']))
        print ('Prime: ' + str(table['prime']))
        while  it.hasNext(iterator):
            bucket = it.next(iterator)
            bucketiterator = it.newIterator(bucket)
            while  it.hasNext(bucketiterator):
                entry = it.next(bucketiterator)
                result = "".join(str(key) + ":" + str(value) + "," for key, value in entry.items())
                print (result)



    def comparefunction (self, element1, element2):
        if (element1['key'] == element2['key']):
            return True
        return False


    def test_hashValue (self):
        """
        """
        print ('TEST--------------------------------')
        table = ht.newMap ()
        hv = ht.hashValue (table, 'book1')

     
    def test_put (self):
        """
        """
        print ('TEST--------------------------------')
        capacity = 7
        table = ht.newMap (capacity)
        ht.put (table, 'book1', 'title1', self.comparefunction)
        ht.put (table, 'book2', 'title2', self.comparefunction)
        self.printTable (table)
        ht.put (table, 'book2', 'new-title 2', self.comparefunction)
        self.printTable (table)

if __name__ == "__main__":
    unittest.main()
