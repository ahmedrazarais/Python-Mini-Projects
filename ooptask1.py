
# Certainly! Here's a task for you to practice object-oriented programming in Python:

# Task: Create a simple program to model a library system. You'll have three classes: one for a Library, one for a Book, and one for a Member.

# Book Class:

# Attributes: Title, author, publication year, and availability (whether the book is currently available or not).
# # Methods:
# __init__: Initialize the book with given attributes.
# check_availability: Check if the book is available for borrowing.
# borrow_book: Set the availability of the book to False when borrowed.
# return_book: Set the availability of the book to True when returned.

class Book:
    def __init__(self, title, author, publication_year, availability):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability = availability

    def check_availability(self):
        if self.availability:
            print("Book Is Available")
        else:
            print("Book is Not Available")

    def borrow_book(self):
        if not self.availability:
            self.availability = False
            print("Book Is Borrowed.")
        else:
            print("Book Has Been Received")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print("Book has Been Returned")
        else:
            print("Book Has Not Been Returned Yet")












# Member Class:

# Attributes: Name and a list of borrowed books.
# Methods:
# __init__: Initialize the member with a given name and an empty list of borrowed books.
# borrow_book: Add a book to the list of borrowed books.
# return_book: Remove a book from the list of borrowed books when returned.
            
class Member:
    Name=""
    borrowed_books=[]

    def __init__(self,Name,borrowed_books) :
        self.Name=Name
        self.borrowed_books=borrowed_books

    def borrow_book(self,book_name):
        self.borrowed_books.append(book_name)
        print("Book Is added.")
    
    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            print("Book has been returned.")
        else:
            print("Book not found in the borrowed list.")


# Library Class:

# Attributes: List of books and list of members.
# Methods:
# __init__: Initialize the library with empty lists of books and members.
# add_book: Add a book to the library.
# add_member: Add a member to the library.
# borrow_book: Allow a member to borrow a book (updating availability and member's list of borrowed books).
# return_book: Allow a member to return a book (updating availability and member's list of borrowed books).

class Library:
    def __init__(self, book_list=None, member_list=None):
        if book_list is None:
            book_list = []
        if member_list is None:
            member_list = []
        self.book_list = book_list
        self.member_list = member_list

    def add_book(self, book):
        self.book_list.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def add_member(self, member):
        self.member_list.append(member)
        print(f"Member '{member.Name}' has been added to the library.")

    def borrow_book(self, member_name, book_title):
        for member in self.member_list:
            if member.Name == member_name:
                for book in self.book_list:
                    if book.title == book_title:
                        if book.availability:
                            book.borrow_book()
                            member.borrow_book(book_title)
                        else:
                            print("Book is not available for borrowing.")
                        return
                print("Book not found in the library.")
                return
        print("Member not found in the library.")

    def return_book(self, member_name, book_title):
        for member in self.member_list:
            if member.Name == member_name:
                for book in self.book_list:
                    if book.title == book_title:
                        if not book.availability:
                            book.return_book()
                            member.return_book(book_title)
                            print(f"Book '{book_title}' has been returned.")
                            return
                        else:
                            print("Book is already available.")
                            return
                print("Book not found in the library.")
                return
        print("Member not found in the library.")