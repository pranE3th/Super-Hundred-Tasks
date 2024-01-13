class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def is_available(self):
        return self.available

    def set_available(self, available):
        self.available = available


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        if member in self.members and book in self.books and book.is_available():
            book.set_available(False)
            print("{} borrowed {}".format(member.name,book.title))
        else:
            print("book not available or you are not a member.")

    def return_book(self, member, book):
        if member in self.members and book in self.books and not book.is_available():
            book.set_available(True)
            print("{} returned {}".format(member.name,book.title))
        else:
            print("Unable to return the book")

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available():
                print("{} by {}".format(book.title,book.author))

library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

member1 = Member("John Doe", 1)
member2 = Member("Jane Smith", 2)

library.add_book(book1)
library.add_book(book2)

library.add_member(member1)
library.add_member(member2)
"""
while 1:
    print('1 to borrow book--- 2 to display available books---3 to return book')
    if"""

library.borrow_book(member1, book1)
library.borrow_book(member2, book2)

library.display_available_books()

library.return_book(member1, book1)

library.display_available_books()
