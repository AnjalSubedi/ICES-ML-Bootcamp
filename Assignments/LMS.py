"""This program is a library management sstem which chcks the availability of books and displays it to the user"""
class Book:
    """
    This class represents a book in the library.
    Attributes:
    - title: Title of the book
    - author: Author of the book
    - book_id: Unique ID for the book
    - availability: Availability status of the book (True if available, False if borrowed)
    """

    def __init__(self, title: str, author: str, book_id: int):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.availability = True

    def borrow_book(self):
        """
        Marks the book as borrowed.
        """
        if self.availability:
            self.availability = False
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def return_book(self):
        """
        Marks the book as returned.
        """
        if not self.availability:
            self.availability = True
        else:
            print(f"The book '{self.title}' was not borrowed.")

    def __str__(self):
        status = "Available" if self.availability else "Borrowed"
        return f'"{self.title}" by {self.author} (ID: {self.book_id}) - {status}'

class Library:
    """
    This class manages a list of books in the library.
    Attributes:
    - library_name: Name of the library
    - books: A list of Book objects
    """

    def __init__(self, library_name: str):
        self.library_name = library_name
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book to the library.
        Parameters:
        - book: A Book object
        """
        self.books.append(book)

    def borrow_book_by_id(self, book_id: int):
        """
        Marks a book as borrowed based on its ID.
        Parameters:
        - book_id: The ID of the book to be borrowed
        """
        for book in self.books:
            if book.book_id == book_id:
                book.borrow_book()
                return
        print(f"No book found with ID: {book_id}")

    def return_book_by_id(self, book_id: int):
        """
        Marks a book as returned based on its ID.
        Parameters:
        - book_id: The ID of the book to be returned
        """
        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                return
        print(f"No book found with ID: {book_id}")

    def get_inventory(self):
        """
        Prints the inventory of all books in the library.
        """
        for book in self.books:
            print(book)

# Example Usage
book1 = Book("The Great Gatsby", "Anjal Subedi", 1)
book2 = Book("1984", "George Orwell", 2)
book3 = Book("It ends with us", "Collen Hoover", 3)

# Create an instance of Library
library = Library("Pokhara Library")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# Borrow and return books
library.return_book_by_id(1)
library.return_book_by_id(2)
library.return_book_by_id(3)

# Print the inventory of books
library.get_inventory()
