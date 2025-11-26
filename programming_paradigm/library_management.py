class Book:
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False
    
    def check_out(self):
        """Check out the book if available"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book if it was checked out"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        # Private list to store book instances
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library"""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only Book objects can be added to the library")
    
    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                if book.check_out():
                    print(f"Successfully checked out: {book.title}")
                    return True
                else:
                    print(f"Book '{title}' is already checked out")
                    return False
        print(f"Book '{title}' not found or unavailable")
        return False
    
    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                if book.return_book():
                    print(f"Successfully returned: {book.title}")
                    return True
                else:
                    print(f"Book '{title}' was not checked out")
                    return False
        print(f"Book '{title}' not found in library")
        return False
    
    def list_available_books(self):
        """List all available books"""
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books in the library")
    
    def find_book(self, title):
        """Find a book by title (helper method)"""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None