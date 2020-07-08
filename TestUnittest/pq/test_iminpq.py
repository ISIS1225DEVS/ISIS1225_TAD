import unittest
import config
import math
from ADT import indexminpq as ipq


class IminPQTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def comparekeys (self, key, element):
        if ( key == element['key']):
            return True
        return False

    def test_newiminpq (self):

        iminpq = ipq.newIndexMinPQ(12, self.comparekeys)

        self.assertTrue (ipq.isEmpty(iminpq))

        ipq.insert (iminpq, 'A', 78)  
        ipq.insert (iminpq, 'B', 16)
        ipq.insert (iminpq, 'C', 9)
        ipq.insert (iminpq, 'D', 33)
        ipq.insert (iminpq, 'E', 21)
        ipq.insert (iminpq, 'F', 82)
        ipq.insert (iminpq, 'G', 4)
        ipq.insert (iminpq, 'H', 93)
        ipq.insert (iminpq, 'I', 51)
        ipq.insert (iminpq, 'J', 87)
        ipq.insert (iminpq, 'K', 12)
        ipq.insert (iminpq, 'L', 14) 
                    
        self.assertTrue (ipq.size(iminpq), 12)
        self.assertFalse (ipq.isEmpty(iminpq))
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 4)


    def test_increaseLeaf (self):

        iminpq = ipq.newIndexMinPQ(12, self.comparekeys)

        self.assertTrue (ipq.isEmpty(iminpq))

        ipq.insert (iminpq, 'A', 78)  
        ipq.insert (iminpq, 'B', 16)
        ipq.insert (iminpq, 'C', 9)
        ipq.insert (iminpq, 'D', 33)
        ipq.insert (iminpq, 'E', 21)
        ipq.insert (iminpq, 'F', 82)
        ipq.insert (iminpq, 'G', 4)
        ipq.insert (iminpq, 'H', 93)
        ipq.insert (iminpq, 'I', 51)
        ipq.insert (iminpq, 'J', 87)
        ipq.insert (iminpq, 'K', 12)
        ipq.insert (iminpq, 'L', 14) 
                    
        self.assertTrue (ipq.size(iminpq), 12)
        self.assertFalse (ipq.isEmpty(iminpq))
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 4)

        ipq.changeKeyIndex (iminpq, 'A', 2)
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 2)
        self.assertEqual (min['key'], 'A')


    def test_increaseNode (self):

        iminpq = ipq.newIndexMinPQ(12, self.comparekeys)

        self.assertTrue (ipq.isEmpty(iminpq))

        ipq.insert (iminpq, 'A', 78)  
        ipq.insert (iminpq, 'B', 16)
        ipq.insert (iminpq, 'C', 9)
        ipq.insert (iminpq, 'D', 33)
        ipq.insert (iminpq, 'E', 21)
        ipq.insert (iminpq, 'F', 82)
        ipq.insert (iminpq, 'G', 4)
        ipq.insert (iminpq, 'H', 93)
        ipq.insert (iminpq, 'I', 51)
        ipq.insert (iminpq, 'J', 87)
        ipq.insert (iminpq, 'K', 12)
        ipq.insert (iminpq, 'L', 14) 
                    
        self.assertTrue (ipq.size(iminpq), 12)
        self.assertFalse (ipq.isEmpty(iminpq))
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 4)

        ipq.changeKeyIndex (iminpq, 'I', 3)
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 3)
        self.assertEqual (min['key'], 'I')
    


    def test_decreaseNode (self):

        iminpq = ipq.newIndexMinPQ(12, self.comparekeys)

        self.assertTrue (ipq.isEmpty(iminpq))

        ipq.insert (iminpq, 'A', 78)  
        ipq.insert (iminpq, 'B', 16)
        ipq.insert (iminpq, 'C', 9)
        ipq.insert (iminpq, 'D', 33)
        ipq.insert (iminpq, 'E', 21)
        ipq.insert (iminpq, 'F', 82)
        ipq.insert (iminpq, 'G', 4)
        ipq.insert (iminpq, 'H', 93)
        ipq.insert (iminpq, 'I', 51)
        ipq.insert (iminpq, 'J', 87)
        ipq.insert (iminpq, 'K', 12)
        ipq.insert (iminpq, 'L', 14) 
                    
        self.assertTrue (ipq.size(iminpq), 12)
        self.assertFalse (ipq.isEmpty(iminpq))
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 4)

        ipq.changeKeyIndex (iminpq, 'K', 105)
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 4)
        self.assertEqual (min['key'], 'G')
        

    def test_decreaseRoot (self):

        iminpq = ipq.newIndexMinPQ(12, self.comparekeys)

        self.assertTrue (ipq.isEmpty(iminpq))

        ipq.insert (iminpq, 'A', 78)  
        ipq.insert (iminpq, 'B', 16)
        ipq.insert (iminpq, 'C', 9)
        ipq.insert (iminpq, 'D', 33)
        ipq.insert (iminpq, 'E', 21)
        ipq.insert (iminpq, 'F', 82)
        ipq.insert (iminpq, 'G', 4)
        ipq.insert (iminpq, 'H', 93)
        ipq.insert (iminpq, 'I', 51)
        ipq.insert (iminpq, 'J', 87)
        ipq.insert (iminpq, 'K', 12)
        ipq.insert (iminpq, 'L', 14) 
                    
        self.assertTrue (ipq.size(iminpq), 12)
        self.assertFalse (ipq.isEmpty(iminpq))
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 4)

        ipq.changeKeyIndex (iminpq, 'G', 180)
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 9)
        self.assertEqual (min['key'], 'C')


    def test_infinitum (self):

        iminpq = ipq.newIndexMinPQ(12, self.comparekeys)

        self.assertTrue (ipq.isEmpty(iminpq))

        ipq.insert (iminpq, 'A', math.inf)  
        ipq.insert (iminpq, 'B', math.inf)
        ipq.insert (iminpq, 'C', math.inf)
        ipq.insert (iminpq, 'D', math.inf)
        ipq.insert (iminpq, 'E', math.inf)
        ipq.insert (iminpq, 'F', math.inf)
        ipq.insert (iminpq, 'G', math.inf)
        ipq.insert (iminpq, 'H', math.inf)
        ipq.insert (iminpq, 'I', math.inf)
        ipq.insert (iminpq, 'J', math.inf)
        ipq.insert (iminpq, 'K', math.inf)
        ipq.insert (iminpq, 'L', math.inf) 
                    
        self.assertTrue (ipq.size(iminpq), 12)
        self.assertFalse (ipq.isEmpty(iminpq))

        ipq.changeKeyIndex (iminpq, 'I', 0.0)
        min = ipq.min(iminpq)
        self.assertEqual (min['value'], 0.0)
        self.assertEqual (min['key'], 'I')

if __name__ == "__main__":
    unittest.main()
