"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """



import unittest 
import config 
from DataStructures import liststructure as slt

class AddFirstListTest (unittest.TestCase):

    def setUp (self):
        self.book1 = {'book_id':'1', 'book_title':'Title 1', 'author':'author 1'}
        self.book2 = {'book_id':'2', 'book_title':'Title 2', 'author':'author 2'}
        self.book3 = {'book_id':'3', 'book_title':'Title 3', 'author':'author 3'}
        self.book4 = {'book_id':'4', 'book_title':'Title 4', 'author':'author 4'}
        self.book5 = {'book_id':'5', 'book_title':'Title 5', 'author':'author 5'}

    def tearDown (self):
        pass


    def test_addFirstEmpty (self):
        """
           Con la lista vacia
        """
        self.lst = slt.newList('SINGLE_LINKED_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addFirst (self.lst, self.book1)
        self.assertEqual (slt.size(self.lst), 1)
        book = slt.firstElement(self.lst)
        self.assertDictEqual (book, self.book1)

    def test_addFirstOneElement (self):
        """
           Con un elemento en la lista
        """
        self.lst = slt.newList('SINGLE_LINKED_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addFirst (self.lst, self.book1)
        self.assertEqual (slt.size(self.lst), 1)
        book = slt.firstElement(self.lst)
        self.assertDictEqual (book, self.book1)    
        slt.addFirst (self.lst, self.book2)
        self.assertEqual (slt.size(self.lst), 2)
        book = slt.firstElement(self.lst)
        self.assertDictEqual (book, self.book2) 

    def test_addFirstMultiElements (self):
        """
           Con muchos elementos en la lista
        """
        self.lst = slt.newList('SINGLE_LINKED_LIST')
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book5)
        self.assertEqual (slt.size(self.lst), 5)
        book = slt.firstElement(self.lst)
        self.assertDictEqual (book, self.book5)     

    def comparebooks (self, book1, book2):
        if book1['book_id'] == book2['book_id']:
            return True    
        return False

    def test_isPresent (self):
        """
           Con muchos elementos en la lista
        """
        self.lst = slt.newList('SINGLE_LINKED_LIST')
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book5)
        book = {'book_id':'1', 'book_title':'Title 1', 'author':'author 1'}
        self.assertEqual (slt.size(self.lst), 5)
        present = slt.isPresent (self.lst, book, self.comparebooks )
        if  present > 0:
            print ('el libro esta presente') 
        else:
            print ('El libro no esta presente')    

if __name__ == "__main__":
    unittest.main()
