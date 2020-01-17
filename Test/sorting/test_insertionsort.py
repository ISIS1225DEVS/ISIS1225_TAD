import unittest 
import config 
from Sorting import insertionsort as isort
from DataStructures import listiterator as it
from TAD import list as slt


class insertionSortTest (unittest.TestCase):

    def setUp (self):
        self.book1 = {'book_id':'1', 'book_title':'Title 1', 'author':'author 1'}
        self.book2 = {'book_id':'2', 'book_title':'Title 2', 'author':'author 2'}
        self.book3 = {'book_id':'3', 'book_title':'Title 3', 'author':'author 3'}
        self.book4 = {'book_id':'4', 'book_title':'Title 4', 'author':'author 4'}
        self.book5 = {'book_id':'5', 'book_title':'Title 5', 'author':'author 5'}

    def tearDown (self):
        pass

    def less( self, element1, element2):
        if int(element1['book_id']) <  int(element2['book_id']):
            return True
        return False

    def test_addElements (self):
        """
           Con muchos elementos en la lista
        """
        self.lst = slt.newList()
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book4)
        self.assertEqual (slt.size(self.lst), 5)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        isort.insertionSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)


if __name__ == "__main__":
    unittest.main()
