import unittest 
import config 
from DataStructures import bstnode as node
from DataStructures import bst as bst
from DataStructures import listiterator as it
from ADT import list as lt

class EntryMapTest (unittest.TestCase):

    


    def setUp (self):
        pass



    def tearDown (self):
        pass


    def comparekeys (self, key1, key2):
        if ( int(key1) == int(key2)):
            return 0
        elif (int(key1) < int(key2)):
            return -1
        else:
            return 1


    def test_BST (self):
        """
        """
        tree = bst.newMap ( )
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'title8', self.comparekeys)
        bst.put (tree, '70', 'Title10', self.comparekeys)
        bst.put (tree, '30', 'Title 6', self.comparekeys)
        bst.put (tree, '80', 'Title 3', self.comparekeys)
        bst.put (tree, '60', 'Title10', self.comparekeys)
        bst.put (tree, '40', 'Title 6', self.comparekeys)
        bst.put (tree, '20', 'Title 3', self.comparekeys)
        bst.put (tree, '10', 'Title10', self.comparekeys)
        bst.put (tree, '25', 'Title 6', self.comparekeys)
        bst.put (tree, '6', 'Title 3', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        self.assertTrue (bst.contains (tree, '6',self.comparekeys))
        self.assertFalse (bst.contains (tree, '16',self.comparekeys))
        self.assertEqual ( bst.min (tree)['key'], '6' )
        self.assertEqual ( bst.max (tree)['key'], '80' )
        bst.deleteMin (tree)
        self.assertEqual ( bst.min (tree)['key'], '7' )
        bst.deleteMin (tree)
        self.assertEqual ( bst.min (tree)['key'], '10' )
        bst.deleteMax (tree)
        self.assertEqual ( bst.max (tree)['key'], '70' )
        bst.deleteMax (tree)
        self.assertEqual ( bst.max (tree)['key'], '60' )


if __name__ == "__main__":
    unittest.main()
