import unittest
import config
from ADT import minpq as pq
from ADT import list as lt



class HeapTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass


    def test_newHeap (self):

        minpq = pq.newMinPQ()
        self.assertTrue (pq.isEmpty(minpq))

        pq.insert (minpq, 78)  
        pq.insert (minpq, 16)
        pq.insert (minpq, 9)
        pq.insert (minpq, 33)
        pq.insert (minpq, 21)
        pq.insert (minpq, 82)
        pq.insert (minpq, 4)
        pq.insert (minpq, 93)
        pq.insert (minpq, 51)
        pq.insert (minpq, 87)
        pq.insert (minpq, 12)
        pq.insert (minpq, 14) 

        self.assertTrue (pq.size(minpq), 12)
        self.assertFalse (pq.isEmpty(minpq))
        self.assertEqual (pq.min(minpq), 4)


        min = pq.delMin (minpq)
        self.assertEqual (min, 4)
        min = pq.delMin (minpq)
        self.assertEqual (min, 9)
        min = pq.delMin (minpq)
        self.assertEqual (min, 12)
        min = pq.delMin (minpq)
        self.assertEqual (min, 14)
        min = pq.delMin (minpq)
        self.assertEqual (min, 16)
        min = pq.delMin (minpq)
        self.assertEqual (min, 21)
        min = pq.delMin (minpq)
        self.assertEqual (min, 33)
        min = pq.delMin (minpq)
        self.assertEqual (min, 51)
        min = pq.delMin (minpq)
        self.assertEqual (min, 78)
        min = pq.delMin (minpq)
        self.assertEqual (min, 82)
        min = pq.delMin (minpq)
        self.assertEqual (min, 87)
        min = pq.delMin (minpq)
        self.assertEqual (min, 93)

if __name__ == "__main__":
    unittest.main()
