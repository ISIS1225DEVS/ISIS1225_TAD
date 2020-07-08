import unittest 
import config 
from DataStructures import rbtnode as node
from DataStructures import listiterator as it
from ADT import list as lt
from ADT import orderedmap as omap

class RBTreeTest (unittest.TestCase):


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


    def comparestrkeys (self, key1, key2):
        if ( key1 == key2):
            return 0
        elif ( key1 < key2):
            return -1
        else:
            return 1


    def test_RBT (self):
        """
        """
        tree = omap.newMap ()
      
        tree = omap.put (tree, 'S', 'Title 50', self.comparestrkeys)
        tree = omap.put (tree, 'E', 'Title 70', self.comparestrkeys)
        tree = omap.put (tree, 'A', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'R', 'Title 80', self.comparestrkeys)        
        tree = omap.put (tree, 'C', 'Title 80', self.comparestrkeys)
        tree = omap.put (tree, 'H', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'X', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'M', 'Title 80', self.comparestrkeys)
        tree = omap.put (tree, 'P', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'L', 'Title 30', self.comparestrkeys)
        print("RBT Aleatorio")
        print (tree)

    
    def test_RBT2 (self):
        """
        """
        tree = omap.newMap ()
      
        tree = omap.put (tree, 'A', 'Title 50', self.comparestrkeys)
        tree = omap.put (tree, 'C', 'Title 70', self.comparestrkeys)
        tree = omap.put (tree, 'E', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'H', 'Title 80', self.comparestrkeys)        
        tree = omap.put (tree, 'L', 'Title 80', self.comparestrkeys)
        tree = omap.put (tree, 'M', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'P', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'R', 'Title 80', self.comparestrkeys)
        tree = omap.put (tree, 'S', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'X', 'Title 30', self.comparestrkeys)
        print("\nRBT Ordenado")
        print (tree)



    def test_keys (self):
        """
        """
        tree = omap.newMap ()
      
        tree = omap.put (tree, 'A', 'Title 50', self.comparestrkeys)
        tree = omap.put (tree, 'C', 'Title 70', self.comparestrkeys)
        tree = omap.put (tree, 'E', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'H', 'Title 80', self.comparestrkeys)        
        tree = omap.put (tree, 'L', 'Title 90', self.comparestrkeys)
        tree = omap.put (tree, 'M', 'Title 20', self.comparestrkeys)
        tree = omap.put (tree, 'P', 'Title 50', self.comparestrkeys)
        tree = omap.put (tree, 'R', 'Title 60', self.comparestrkeys)
        tree = omap.put (tree, 'S', 'Title 10', self.comparestrkeys)
        tree = omap.put (tree, 'X', 'Title 40', self.comparestrkeys)
        kList = omap.keys (tree, 'R', 'X', self.comparestrkeys) 
        print("\nRBT keys between R and X")
        print (kList)


def test_valueRange (self):
        """
        """
        tree = omap.newMap ()
      
        tree = omap.put (tree, 'A', 'Title 50', self.comparestrkeys)
        tree = omap.put (tree, 'C', 'Title 70', self.comparestrkeys)
        tree = omap.put (tree, 'E', 'Title 30', self.comparestrkeys)
        tree = omap.put (tree, 'H', 'Title 80', self.comparestrkeys)        
        tree = omap.put (tree, 'L', 'Title 90', self.comparestrkeys)
        tree = omap.put (tree, 'M', 'Title 20', self.comparestrkeys)
        tree = omap.put (tree, 'P', 'Title 50', self.comparestrkeys)
        tree = omap.put (tree, 'R', 'Title 60', self.comparestrkeys)
        tree = omap.put (tree, 'S', 'Title 10', self.comparestrkeys)
        tree = omap.put (tree, 'X', 'Title 40', self.comparestrkeys)
        kList = omap.valueRange (tree, 'R', 'X', self.comparestrkeys)  
        print("\nRBT values between R and X")
        print (kList)

    


if __name__ == "__main__":
    unittest.main()
