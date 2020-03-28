import unittest 
import config as cf
import csv
from DataStructures import mapentry as me
from ADT import map as ht
from DataStructures import listiterator as it
from ADT import list as lt


class mapTest (unittest.TestCase):


    def loadCSVFile (file, lst):
        input_file = csv.DictReader(open(file))
        for row in input_file:  
            lt.addLast(lst,row)
        input_file.close()


    def compare_book_id (self, key, element):
        return (key == element['value']['book_id'])


    def setUp (self):
        pass



    def tearDown (self):
        pass



    def printTable (self, map):
        if map['type'] == 'CHAINING':
            self.printChainingTable (map)
        else:
            self.printProbingTable (map)


    def printChainingTable (self, map):
        print ('TABLE:')
        print ('Capacity: ' + str(map['capacity']))
        print ('Scale: ' + str(map['scale']))
        print ('Shift: ' + str(map['shift']))
        print ('Prime: ' + str(map['prime']))
        print ('size: ' + str(map['size']))
        iterator = it.newIterator(map['table'])
        pos = 1
        while  it.hasNext(iterator):
            bucket = it.next(iterator)
            bucketiterator = it.newIterator(bucket)
            print ("[ " + str(pos) + " ]-->", end="")
            while  it.hasNext(bucketiterator):
                entry = it.next(bucketiterator)
                print (entry, end="")
                print ("-->",end="")
            print ("None")
            pos += 1



    def printProbingTable (self, map):
        print ('TABLE:')
        print ('Capacity: ' + str(map['capacity']))
        print ('Scale: ' + str(map['scale']))
        print ('Shift: ' + str(map['shift']))
        print ('Prime: ' + str(map['prime']))
        print ('size: ' + str(map['size']))
        iterator = it.newIterator(map['table'])
        pos = 1
        while  it.hasNext(iterator):
            print ("[ " + str(pos) + " ]-->", end="")
            entry = it.next(iterator)
            print (entry, end="")
            print ("-->",end="")
            print ("None")
            pos += 1
        


    def test_LoadTable (self):
        table_capacity = 171
        book_map = ht.newMap (capacity=table_capacity, maptype='CHAINING', comparefunction = self.compare_book_id)
        booksfile = cf.data_dir + 'GoodReads/books-small.csv'

        self.assertEqual (ht.size (book_map), 0)
        self.assertTrue (ht.isEmpty (book_map))

        input_file = csv.DictReader(open(booksfile))
        for book in input_file:  
            ht.put(book_map,book['book_id'],book)

        self.assertEqual (ht.size(book_map), 149)
        self.assertTrue (ht.contains(book_map,'100'))

        entry = ht.get (book_map, '100')
        self.assertIsNotNone (entry)
        self.assertEqual (entry['value']['book_id'],'100')

        ht.remove(book_map,'100')
        self.assertEqual (ht.size (book_map), 148)
        self.assertFalse (ht.contains(book_map,'100'))

        lst_keys = ht.keySet (book_map )
        self.assertFalse (lt.isEmpty (lst_keys))
        self.assertEqual (lt.size (lst_keys), 148)

        lst_values = ht.valueSet (book_map )
        self.assertFalse (lt.isEmpty (lst_values))
        self.assertEqual (lt.size (lst_values), 148)




if __name__ == "__main__":
    unittest.main()
