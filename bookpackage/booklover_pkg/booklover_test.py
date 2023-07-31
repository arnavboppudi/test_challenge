#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:19:50 2023

@author: arnavboppudi
"""
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # Add a book and test if it is in book_list
        book_lover = BookLover("Alice", "bbc@gmail.com", "fiction")
        book_lover.add_book("The Great Gatsby", 3)
        self.assertIn("The Great Gatsby", book_lover.book_list)
    
    def test_2_add_book(self):
        # Add the same book twice. Test if it's in book_list only once.
        book_lover = BookLover("Bob", "bob@gmail.com", "nonfiction")
        book_lover.add_book("To Kill a Mockingbird", 3)
        book_lover.add_book("To Kill a Mockingbird", 3)
        self.assertEqual(len(book_lover.book_list),1)
    
    def test_3_has_read(self):
        # Pass a book in the list and test the answer is True.
        book_lover = BookLover("Charlie", "charlie@gmail.com", "fiction")
        book_lover.add_book("Pride and Prejudice", 5)
        self.assertTrue(book_lover.has_read("Pride and Prejudice"))
    
    def test_4_has_read(self):
        # Pass a book NOT in the list and use assert False to test if the answer is False.
        book_lover = BookLover("David", ["Brave New World"], "david@gmail.com", "fiction")
        self.assertFalse(book_lover.has_read("The Catcher in the Rye"))
    
    def test_5_num_books_read(self):
        # Add some books to the list, and test num_books matches expected.
        book_lover = BookLover("Eve","david@gmail.com", "fiction", 5)
        book_lover.add_book("Harry Potter and the Sorcerer's Stone", 5)
        book_lover.add_book("Harry Potter and the Chamber of Secrets", 3)
        book_lover.add_book("Harry Potter and the Prisoner of Azkaban", 5)
        expected_num_books = 3
        self.assertEqual(book_lover.num_books_read(), expected_num_books)
    
    def test_6_fav_books(self):
        # Add some books with ratings to the list and check that the returned books have rating > 3.
        book_lover = BookLover("Frank", "david@gmail.com", "fiction")
        book_lover.add_book("To Kill a Mockingbird", 5)
        book_lover.add_book("The Great Gatsby", 4)
        book_lover.add_book("1984", 2)
        book_lover.add_book("Pride and Prejudice", 5)
        book_lover.add_book("The Catcher in the Rye", 3)
        fav_books = book_lover.fav_books()
        self.assertEqual(len(book_lover.book_list), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
