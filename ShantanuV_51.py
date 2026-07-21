class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Not available"
        print(f"Title      : {self.title}")
        print(f"Author     : {self.author}")
        print(f"Available  : {status}")
        print("-" * 30)


class Patron:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.books_borrowed = []

    def display(self):
        borrowed = ", ".join(b.title for b in self.books_borrowed) if self.books_borrowed else "None"
        print(f"Name             : {self.first_name} {self.last_name}")
        print(f"Books borrowed   : {borrowed}")
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book added: '{book.title}' by {book.author}")
        return book

    def register_patron(self, first_name, last_name):
        patron = Patron(first_name, last_name)
        self.patrons.append(patron)
        print(f"Patron registered: {patron.first_name} {patron.last_name}")
        return patron

    def _find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def _find_patron(self, first_name, last_name):
        for patron in self.patrons:
            if patron.first_name.lower() == first_name.lower() and patron.last_name.lower() == last_name.lower():
                return patron
        return None

    def borrow_book(self, title, first_name, last_name):
        book = self._find_book(title)
        patron = self._find_patron(first_name, last_name)

        if book is None:
            print(f"Error: Book '{title}' not found.")
            return
        if patron is None:
            print(f"Error: Patron {first_name} {last_name} not found.")
            return
        if not book.available:
            print(f"Error: '{book.title}' is already borrowed.")
            return

        else:
            book.available = False
            patron.books_borrowed.append(book)
            print(f"{patron.first_name} {patron.last_name} borrowed '{book.title}'.")

    def return_book(self, title, first_name, last_name):
        book = self._find_book(title)
        patron = self._find_patron(first_name, last_name)

        if book is None:
            print(f"Error: Book '{title}' not found.")
            return
        if patron is None:
            print(f"Error: Patron {first_name} {last_name} not found.")
            return
        if book not in patron.books_borrowed:
            print(f"Error: {patron.first_name} {patron.last_name} did not borrow '{book.title}'.")
            return

        else:
            book.available = True
            patron.books_borrowed.remove(book)
            print(f"{patron.first_name} {patron.last_name} returned '{book.title}'.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("=== Library Books ===")
        for book in self.books:
            book.display()

    def show_patrons(self):
        if not self.patrons:
            print("No registered patrons.")
            return
        print("=== Registered Patrons ===")
        for patron in self.patrons:
            patron.display()


if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.add_book("Dune", "Frank Herbert")
    library.add_book("1984", "George Orwell")

    # Register patrons
    library.register_patron("Alice", "Johnson")
    library.register_patron("Bob", "Smith")

    print()
    library.show_books()
    print()
    library.show_patrons()

    print()
    # Borrow / return demo
    library.borrow_book("Dune", "Alice", "Johnson")
    library.borrow_book("Dune", "Bob", "Smith")  # should fail
    library.return_book("Dune", "Alice", "Johnson")
    library.borrow_book("Dune", "Bob", "Smith")

    print()
    library.show_books()
    print()
    library.show_patrons()