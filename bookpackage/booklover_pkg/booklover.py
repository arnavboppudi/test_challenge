#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:25:12 2023

@author: arnavboppudi
"""
import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        if not self.book_list[self.book_list['book_name'] == book_name].empty:
            print("You have already read this book.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            
    def has_read(self, book_name):
        return not self.book_list[self.book_list['book_name'] == book_name].empty
        
    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Dune", 5)
    test_object.add_book("Foundation", 4)
    test_object.add_book("1984", 2)

    print("You have read these books.")

    book_name = "Dune"
    if test_object.has_read(book_name):
        print("You have not read this book.")
    else:
        print("You have not read this book.")

    print("This is your favorite books:")
    print(test_object.fav_books())
