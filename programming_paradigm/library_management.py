# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book is already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book is already available

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book}")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book}")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        availa
