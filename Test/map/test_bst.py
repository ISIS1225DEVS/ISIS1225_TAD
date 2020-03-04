import unittest
import config
from DataStructures import bstnode as node
from DataStructures import listiterator as it
from ADT import list as lt
from ADT import orderedmap as bst

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


    def test_DisorderedBST (self):
        """
        """
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 6', self.comparekeys)
        bst.put (tree, '6', 'Title 3', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)
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




    def test_BSTRemove (self):
        """
        """
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 6', self.comparekeys)
        bst.put (tree, '6', 'Title 3', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)

        bst.remove (tree, '20', self.comparekeys)
        self.assertIsNone( bst.get (tree, '20', self.comparekeys) )


    def test_BSTFloor (self):
        """
        """
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 6', self.comparekeys)
        bst.put (tree, '6', 'Title 3', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)

        node = bst.floor (tree, '18', self.comparekeys)
        self.assertEqual ( node['key'], '12' )




    def test_BSTCeiling (self):
        """
        """
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 6', self.comparekeys)
        bst.put (tree, '6', 'Title 3', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)

        node = bst.ceiling (tree, '29', self.comparekeys)
        self.assertEqual ( node['key'], '30' )

        node = bst.ceiling (tree, '28', self.comparekeys)
        self.assertEqual ( node['key'], '28' )

        node = bst.ceiling (tree, '30', self.comparekeys)
        self.assertEqual ( node['key'], '30' )

        node = bst.ceiling (tree, '72', self.comparekeys)
        self.assertEqual ( node['key'], '80' )




    def test_BSTSelect (self):
        """
        """
        print ('Test select')
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 25', self.comparekeys)
        bst.put (tree, '6', 'Title 6', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)

        node = bst.select (tree, 1)
        #assert ??
        print ("select 1:",node['key'])


    def test_BSTRank (self):
        """
        """
        print ('Test rank')
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 25', self.comparekeys)
        bst.put (tree, '6', 'Title 6', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)

        rank = bst.rank (tree, '30', self.comparekeys)
        print ("rank 30: ",rank)

        #assert ??


    def test_BSTKeySet (self):
        """
        """
        print ('Test key')
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 25', self.comparekeys)
        bst.put (tree, '6', 'Title 6', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)

        lt = bst.keySet (tree)

        print (lt)



    def test_BSTValueSet (self):
        """
        """
        print ('Test value')
        tree = bst.newMap ('BST')
        self.assertTrue (bst.isEmpty(tree))
        bst.put (tree, '50', 'Title 50', self.comparekeys)
        bst.put (tree, '70', 'Title 70', self.comparekeys)
        bst.put (tree, '30', 'Title 30', self.comparekeys)
        bst.put (tree, '80', 'Title 80', self.comparekeys)
        bst.put (tree, '60', 'Title 60', self.comparekeys)
        bst.put (tree, '40', 'Title 40', self.comparekeys)
        bst.put (tree, '20', 'Title 20', self.comparekeys)
        bst.put (tree, '10', 'Title 10', self.comparekeys)
        bst.put (tree, '25', 'Title 25', self.comparekeys)
        bst.put (tree, '6', 'Title 6', self.comparekeys)
        bst.put (tree, '12', 'Title 12', self.comparekeys)
        bst.put (tree, '7', 'Title 7', self.comparekeys)
        bst.put (tree, '28', 'Title 28', self.comparekeys)

        lt = bst.valueSet (tree)

        print (lt)


if __name__ == "__main__":
    unittest.main()
