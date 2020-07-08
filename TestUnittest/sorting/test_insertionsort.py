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
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as slt


class insertionSortTest (unittest.TestCase):

    #list_type = 'ARRAY_LIST'
    list_type = 'SINGLE_LINKED_LIST'

    def setUp (self):
        self.book1 = {'book_id':'1', 'book_title':'Title 1', 'author':'author 1'}
        self.book2 = {'book_id':'2', 'book_title':'Title 2', 'author':'author 2'}
        self.book3 = {'book_id':'3', 'book_title':'Title 3', 'author':'author 3'}
        self.book4 = {'book_id':'4', 'book_title':'Title 4', 'author':'author 4'}
        self.book5 = {'book_id':'5', 'book_title':'Title 5', 'author':'author 5'}
        self.book6 = {'book_id':'6', 'book_title':'Title 6', 'author':'author 6'}
        self.book7 = {'book_id':'7', 'book_title':'Title 7', 'author':'author 7'}
        self.book8 = {'book_id':'8', 'book_title':'Title 8', 'author':'author 8'}
        self.book9 = {'book_id':'9', 'book_title':'Title 9', 'author':'author 9'}
        self.book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
        self.book11 = {'book_id':'7', 'book_title':'Title 11', 'author':'author 11'}
        self.book12 = {'book_id':'8', 'book_title':'Title 12', 'author':'author 12'}
        self.book13 = {'book_id':'9', 'book_title':'Title 13', 'author':'author 13'}
        self.book14 = {'book_id':'10', 'book_title':'Title 14', 'author':'author 14'}

    def tearDown (self):
        pass

    def less( self, element1, element2):
        if int(element1['book_id']) <  int(element2['book_id']):
            return True
        return False

    def test_randomElements (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book10)
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book9)
     
        print ("Random list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)


    def test_invertedElements (self):
        """
        Lista ordenada inversamente
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book9)
        slt.addFirst (self.lst, self.book10)

        print ("Inverted list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)


    def test_orderedElements (self):
        """
        Lista ordenada
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book10)
        slt.addFirst (self.lst, self.book9)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book1)

        print ("ordered list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_oneElement (self):
        """
        Un elemento
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book1)

        print ("one element:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)



    def test_repeatedElements (self):
        """
           Con muchos elementos en la lista
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book14)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book13)
        slt.addFirst (self.lst, self.book10)
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book12)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book11)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book9)

        print ("Repeated elements:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)




if __name__ == "__main__":
    unittest.main()
