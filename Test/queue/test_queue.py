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
from DataStructures import listiterator as it
from ADT import queue as q


class insertionSortTest (unittest.TestCase):

    list_type = 'ARRAY_LIST'
    #list_type = 'SINGLE_LINKED_LIST'

    def setUp (self):
        """
        Creacion de diccionarios utilizados en las pruebas de la estructura de datos
        """
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

    def test_enqueueElements (self):
        """
        Se prueba la creacion de una nueva cola, se agregan todos los datos creados por sistema y se imprime su valor
        """
        self.queue = q.newQueue(self.list_type)
        q.enqueue  (self.queue, self.book5)
        q.enqueue  (self.queue, self.book6)
        q.enqueue  (self.queue, self.book3)
        q.enqueue  (self.queue, self.book10)
        q.enqueue  (self.queue, self.book1)
        q.enqueue  (self.queue, self.book2)
        q.enqueue  (self.queue, self.book8)
        q.enqueue  (self.queue, self.book4)
        q.enqueue  (self.queue, self.book7)
        q.enqueue  (self.queue, self.book9)

        iterator = it.newIterator(self.queue)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)


    def test_emptyQueue (self):
        """
        Esta prueba confirma la creación de una lista vacia que empieza en tamaño 0
        Al agregar los libros si tamaño debe ser igual a 10.
        """
        self.queue = q.newQueue(self.list_type)
        self.assertEqual (q.size(self.queue), 0)
        self.assertTrue (q.isEmpty(self.queue))
        q.enqueue  (self.queue, self.book5)
        q.enqueue  (self.queue, self.book6)
        q.enqueue  (self.queue, self.book3)
        q.enqueue  (self.queue, self.book10)
        q.enqueue  (self.queue, self.book1)
        q.enqueue  (self.queue, self.book2)
        q.enqueue  (self.queue, self.book8)
        q.enqueue  (self.queue, self.book4)
        q.enqueue  (self.queue, self.book7)
        q.enqueue  (self.queue, self.book9)
        self.assertEqual (q.size(self.queue), 10)


    def test_infoElements (self):
        """
        Este test busca confirmar que los datos se almacenen de forma correcta y que
        sean los valores correctos en el orden apropiado de la estructura.
        """
        self.queue = q.newQueue(self.list_type)
        self.assertEqual (q.size(self.queue), 0)
        self.assertTrue (q.isEmpty(self.queue))
        q.enqueue  (self.queue, self.book5)
        q.enqueue  (self.queue, self.book6)
        q.enqueue  (self.queue, self.book3)
        q.enqueue  (self.queue, self.book10)
        q.enqueue  (self.queue, self.book1)
        q.enqueue  (self.queue, self.book2)
        q.enqueue  (self.queue, self.book8)
        q.enqueue  (self.queue, self.book4)
        q.enqueue  (self.queue, self.book7)
        q.enqueue  (self.queue, self.book9)

        elem = q.dequeue (self.queue)
        self.assertEqual (q.size(self.queue), 9)
        self.assertDictEqual (elem, self.book5)

        elem = q.dequeue (self.queue)
        self.assertEqual (q.size(self.queue), 8)
        self.assertDictEqual (elem, self.book6)

        elem = q.peek (self.queue)
        self.assertEqual (q.size(self.queue), 8)
        self.assertDictEqual (elem, self.book3)

        q.enqueue  (self.queue, self.book5)
        self.assertEqual (q.size(self.queue), 9)
        
        elem = q.peek (self.queue)
        self.assertDictEqual (elem, self.book3)

    def test_dequeue_peek(self):
        """
        Este test prueba la creacion de una cola y que el orden de salida sea el correcto para la
        estructura en cuestion, y que el tamaño se reduzca para cada salida de objeto
        """
        self.queue = q.newQueue(self.list_type)
        self.assertEqual (q.size(self.queue), 0)
        self.assertTrue (q.isEmpty(self.queue))
        q.enqueue  (self.queue, self.book5)
        q.enqueue  (self.queue, self.book6)
        q.enqueue  (self.queue, self.book3)
        q.enqueue  (self.queue, self.book10)
        q.enqueue  (self.queue, self.book1)
        q.enqueue  (self.queue, self.book2)
        q.enqueue  (self.queue, self.book8)
        q.enqueue  (self.queue, self.book4)
        q.enqueue  (self.queue, self.book7)
        q.enqueue  (self.queue, self.book9)
        
        total = q.size(self.queue)
        while not (q.isEmpty(self.queue)):
            top = q.peek(self.queue)
            self.assertEqual(q.dequeue(self.queue), top)
            total-=1
            self.assertEqual(total, q.size(self.queue))

    def test_enqueue_dequeue(self):
        """
        Este test prueba que la cola pueda manejar inserciones y eliminaciones de forma correcta siguiendo
        un orden establecido, y que no quede referencia al objeto sacado despues de haberlo removido de la
        cola
        """
        self.queue = q.newQueue(self.list_type)
        self.assertEqual (q.size(self.queue), 0)
        self.assertTrue (q.isEmpty(self.queue))
        q.enqueue  (self.queue, self.book5)
        self.assertEqual(q.size(self.queue),1)
        self.assertEqual(q.peek(self.queue),q.dequeue(self.queue))
        self.assertEqual(q.size(self.queue),0)

        q.enqueue  (self.queue, self.book6)
        self.assertEqual(q.size(self.queue),1)
        self.assertEqual(q.peek(self.queue),q.dequeue(self.queue))
        self.assertEqual(q.size(self.queue),0)
        
        q.enqueue  (self.queue, self.book3)
        self.assertEqual(q.size(self.queue),1)
        self.assertEqual(q.peek(self.queue),q.dequeue(self.queue))
        self.assertEqual(q.size(self.queue),0)
        
        q.enqueue  (self.queue, self.book10)
        self.assertEqual(q.size(self.queue),1)
        self.assertEqual(q.peek(self.queue),q.dequeue(self.queue))
        self.assertEqual(q.size(self.queue),0)

        q.enqueue  (self.queue, self.book1)
        self.assertEqual(q.size(self.queue),1)
        self.assertEqual(q.peek(self.queue),q.dequeue(self.queue))
        self.assertEqual(q.size(self.queue),0)

        q.enqueue  (self.queue, self.book2)
        self.assertEqual(q.size(self.queue),1)
        self.assertEqual(q.peek(self.queue),q.dequeue(self.queue))
        self.assertEqual(q.size(self.queue),0)

        q.enqueue  (self.queue, self.book8)
        q.enqueue  (self.queue, self.book4)
        q.enqueue  (self.queue, self.book7)
        q.enqueue  (self.queue, self.book9)
        self.assertEqual(q.size(self.queue),4)
        self.assertEqual(self.book8,q.dequeue(self.queue))
        self.assertEqual(self.book4,q.dequeue(self.queue))
        self.assertEqual(self.book7,q.dequeue(self.queue))
        self.assertEqual(self.book9,q.dequeue(self.queue))

        self.assertEqual(q.size(self.queue),0)

    def test_error_dequeue(self):
        """
        Este test busca comprobar que es imposible eliminar un objeto de una cola vacia
        """
        self.queue = q.newQueue(self.list_type)
        self.assertEqual (q.size(self.queue), 0)
        self.assertTrue (q.isEmpty(self.queue))
        
        try:
            q.dequeue(self.queue)
            raise Exception('Deberia fallar')
        except:
            print('No fail')

if __name__ == "__main__":
    unittest.main()
