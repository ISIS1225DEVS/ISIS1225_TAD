import unittest 
import config 
from DataStructures import mapentry as me


class EntryMapTest (unittest.TestCase):

    def setUp (self):
        pass


    def tearDown (self):
        pass

    def test_MapEntry (self):
        """
         
        """
        key = 'book1'
        value = 'Title 1'
        entry = me.newMapEntry(key, value)

        print (entry)
        print (me.getKey(entry))
        print (me.getValue(entry))
     

if __name__ == "__main__":
    unittest.main()
