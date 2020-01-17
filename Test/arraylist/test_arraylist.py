import unittest 
import config 
from DataStructures import singlelinkedlist as slt

class ListTest (unittest.TestCase):

    def setUp (self):
        self.book1 = {'book_id':'1', 'book_title':'Title 1', 'author':'author 1'}
        self.book2 = {'book_id':'2', 'book_title':'Title 2', 'author':'author 2'}
        self.book3 = {'book_id':'3', 'book_title':'Title 3', 'author':'author 3'}
        self.book4 = {'book_id':'4', 'book_title':'Title 4', 'author':'author 4'}
        self.book5 = {'book_id':'5', 'book_title':'Title 5', 'author':'author 5'}

    def tearDown (self):
        pass


    def test_empty (self):
        self.lst = slt.newList()
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)

    def test_addFirst (self):
        self.lst = slt.newList()
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addFirst (self.lst, self.book1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addFirst (self.lst, self.book2)
        self.assertEqual (slt.size(self.lst), 2)
        book = slt.firstElement(self.lst)
        self.assertDictEqual (book, self.book2)


    def test_addLast (self):
        self.lst = slt.newList()
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.book1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.book2)
        self.assertEqual (slt.size(self.lst), 2)
        book = slt.firstElement(self.lst)
        self.assertDictEqual (book, self.book1)
        book = slt.lastElement(self.lst)
        self.assertDictEqual (book, self.book2)


    def test_getElement (self):
        self.lst = slt.newList()
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.book1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.book2)
        self.assertEqual (slt.size(self.lst), 2)
        book = slt.getElement(self.lst, 1)
        self.assertDictEqual (book, self.book1)
        book = slt.getElement(self.lst, 2)
        self.assertDictEqual (book, self.book2)

    def test_removeFirst (self):
        self.lst = slt.newList()
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.book1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.book2)
        self.assertEqual (slt.size(self.lst), 2)
        slt.removeFirst(self.lst)
        book = slt.getElement(self.lst, 1)
        self.assertEqual (slt.isEmpty(self.lst), False)
        self.assertEqual (slt.size(self.lst), 1)
        self.assertDictEqual (book, self.book2)

    def test_removeLast (self):
        self.lst = slt.newList()
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.book1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.book2)
        self.assertEqual (slt.size(self.lst), 2)
        slt.removeLast(self.lst)
        book = slt.getElement(self.lst, 1)
        self.assertEqual (slt.isEmpty(self.lst), False)
        self.assertEqual (slt.size(self.lst), 1)
        self.assertDictEqual (book, self.book1)

    def test_insertElement (self):
        self.lst = slt.newList()
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.insertElement (self.lst, self.book1, 1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.insertElement (self.lst, self.book2, 1)
        self.assertEqual (slt.size(self.lst), 2)
        book = slt.getElement(self.lst, 1)
        self.assertDictEqual (book, self.book2)
        book = slt.getElement(self.lst, 2)
        self.assertDictEqual (book, self.book1)


if __name__ == "__main__":
    unittest.main()