import unittest
import config
from DataStructures import heap as h




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

        heap = h.newHeap (12, self.comparekeys)
        self.assertTrue (h.isEmpty(heap))

        h.insert (heap, 'A', 78)  
        h.insert (heap, 'B', 16)
        h.insert (heap, 'C', 9)
        h.insert (heap, 'D', 33)
        h.insert (heap, 'E', 21)
        h.insert (heap, 'F', 82)
        h.insert (heap, 'G', 4)
        h.insert (heap, 'H', 93)
        h.insert (heap, 'I', 51)
        h.insert (heap, 'J', 87)
        h.insert (heap, 'K', 12)
        h.insert (heap, 'L', 14) 

        self.assertTrue (h.size(heap), 12)
        self.assertFalse (h.isEmpty(heap))
        self.assertEqual (h.min(heap)['value'], 4)


        min = h.delMin (heap)
        self.assertEqual (min['value'], 4)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 9)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 12)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 14)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 16)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 21)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 33)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 51)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 78)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 82)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 87)
        min = h.delMin (heap)
        self.assertEqual (min['value'], 93)




if __name__ == "__main__":
    unittest.main()
