# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True  # Book successfully checked out

    def return_book(self):
        if not self._is_checked_out:
            return False  # Book is already available
        self._is_checked_out = False
        return True  # Book successfully returned

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        self._books.append(book)  # Add book to the library

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                    return
                else:
                    print(f"{title} is already checked out.")
                return
        print(f"{title} not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {title}")
                    return
                else:
                    print(f"{title} is not checked out.")
                return
        print(f"{title} not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")
