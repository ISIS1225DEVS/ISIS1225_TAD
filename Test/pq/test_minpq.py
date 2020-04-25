import unittest
import config
from DataStructures import heap as h




class HeapTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass


    def test_newHeap (self):

        heap = h.newHeap ()
        self.assertTrue (h.isEmpty(heap))

        h.insert (heap, 78)  
        h.insert (heap, 16)
        h.insert (heap, 9)
        h.insert (heap, 33)
        h.insert (heap, 21)
        h.insert (heap, 82)
        h.insert (heap, 4)
        h.insert (heap, 93)
        h.insert (heap, 51)
        h.insert (heap, 87)
        h.insert (heap, 12)
        h.insert (heap, 14) 

        self.assertTrue (h.size(heap), 12)
        self.assertFalse (h.isEmpty(heap))
        self.assertEqual (h.min(heap), 4)


        min = h.delMin (heap)
        self.assertEqual (min, 4)
        min = h.delMin (heap)
        self.assertEqual (min, 9)
        min = h.delMin (heap)
        self.assertEqual (min, 12)
        min = h.delMin (heap)
        self.assertEqual (min, 14)
        min = h.delMin (heap)
        self.assertEqual (min, 16)
        min = h.delMin (heap)
        self.assertEqual (min, 21)
        min = h.delMin (heap)
        self.assertEqual (min, 33)
        min = h.delMin (heap)
        self.assertEqual (min, 51)
        min = h.delMin (heap)
        self.assertEqual (min, 78)
        min = h.delMin (heap)
        self.assertEqual (min, 82)
        min = h.delMin (heap)
        self.assertEqual (min, 87)
        min = h.delMin (heap)
        self.assertEqual (min, 93)




if __name__ == "__main__":
    unittest.main()
