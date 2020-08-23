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


import pytest
import config as cf
from Sorting import selectionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'


@pytest.fixture
def lst_books ():
    lst = lt.newList(list_type)
    booksfile = cf.data_dir + 'GoodReads/books-small.csv'
    loadCSVFile(booksfile, lst)
    return lst


def loadCSVFile(file, lst):
    input_file = csv.DictReader(open(file, encoding = "utf-8"))
    for row in input_file:
        lt.addLast(lst, row)

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['goodreads_book_id'])

def less(element1, element2):
    if int(element1['goodreads_book_id']) < int(element2['goodreads_book_id']):
        return True
    return False


def test_loading_CSV_y_ordenamiento(lst_books):
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    element = lt.lastElement (lst_books)
    assert element['goodreads_book_id'] == '4374400'
    element = lt.firstElement (lst_books)
    assert element['goodreads_book_id'] == '2767052'

    sort.selectionSort(lst_books,less)

    tam = lt.size (lst_books)
    assert tam == 149
    element = lt.lastElement (lst_books)
    assert element['goodreads_book_id'] == '22557272'
    element = lt.firstElement (lst_books)
    assert element['goodreads_book_id'] == '1'

