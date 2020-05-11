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
import config as cf
from Sorting import selectionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv


class selectionSortTest (unittest.TestCase):
    list_type = 'ARRAY_LIST'
    #list_type = 'SINGLE_LINKED_LIST'
    
    lst_books = lt.newList(list_type)
    booksfile = cf.data_dir + 'GoodReads/books-medium.csv'

    def setUp (self):
        print ('Loading books')
        self.loadCSVFile (self.booksfile, self.lst_books)
        print (self.lst_books['size'])


    def tearDown (self):
        pass

    def loadCSVFile (self, file, lst):
        input_file = csv.DictReader(open(file))
        for row in input_file:  
            lt.addLast(lst,row)


    def printList (self, lst):
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            print (element ['goodreads_book_id'])


    def less( self, element1, element2):
        if int(element1['goodreads_book_id']) <  int(element2['goodreads_book_id']):
            return True
        return False


    def test_sort (self):
        """
         Lista con elementos en orden aleatorio
        """
        print ("sorting ....")
        sort.selectionSort (self.lst_books, self.less)
        self.printList (self.lst_books)


if __name__ == "__main__":
    unittest.main()
