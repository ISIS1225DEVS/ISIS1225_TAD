import unittest
import config
from ADT import minpq as pq
from ADT import list as lt



class HeapTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

  
    def comparekeys (self, key, element):
        if ( key == element['key']):
            return True
        return False


    def test_newHeap (self):

        minpq = pq.newMinPQ(12, self.comparekeys)
        self.assertTrue (pq.isEmpty(minpq))

        pq.insert (minpq, 'A', 78)  
        pq.insert (minpq, 'B', 16)
        pq.insert (minpq, 'C', 9)
        pq.insert (minpq, 'D', 33)
        pq.insert (minpq, 'E', 21)
        pq.insert (minpq, 'F', 82)
        pq.insert (minpq, 'G', 4)
        pq.insert (minpq, 'H', 93)
        pq.insert (minpq, 'I', 51)
        pq.insert (minpq, 'J', 87)
        pq.insert (minpq, 'K', 12)
        pq.insert (minpq, 'L', 14) 

        self.assertTrue (pq.size(minpq), 12)
        self.assertFalse (pq.isEmpty(minpq))
        self.assertEqual (pq.min(minpq)['value'], 4)


        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 4)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 9)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 12)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 14)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 16)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 21)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 33)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 51)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 78)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 82)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 87)
        min = pq.delMin (minpq)
        self.assertEqual (min['value'], 93)

if __name__ == "__main__":
    unittest.main()
