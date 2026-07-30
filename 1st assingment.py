

class books:
    def __init__(self, book_id, book_name, author):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.books_borrowed = False

    def display(self):
        status = "Borrowed" if self.books_borrowed else "Available"
        print(f"Book ID : {self.book_id}")
        print(f"Book Name : {self.book_name}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")
        print("-" * 30)


class patron:
    def __init__(self, patron_id, patron_name):
        self.patron_id = patron_id
        self.patron_name = patron_name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID : {self.patron_id}")
        print(f"Patron Name : {self.patron_name}")

        if self.borrowed_books:
            print("Borrowed Books :", ", ".join(self.borrowed_books))
        else:
            print("No borrowed books.")

        print("-" * 30)


class library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_books(self, book):
        self.books[book.book_id] = book
        print(f"The new book '{book.book_name}' is added.")

    def add_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"The new patron '{patron.patron_name}' is successfully registered.")

    def borrowed_books(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.books_borrowed:
            print(f"'{book.book_name}' is already borrowed.")
        else:
            book.books_borrowed = True
            patron.borrowed_books.append(book.book_name)
            print(f"{patron.patron_name} borrowed '{book.book_name}'.")

    def return_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.book_name in patron.borrowed_books:
            patron.borrowed_books.remove(book.book_name)
            book.books_borrowed = False
            print(f"{patron.patron_name} returned '{book.book_name}'.")
        else:
            print(f"{patron.patron_name} has not borrowed '{book.book_name}'.")

    def display_books(self):
        print("\nLibrary Books")
        print("-" * 30)
        for book in self.books.values():
            book.display()

    def display_patrons(self):
        print("\nRegistered Patrons")
        print("-" * 30)
        for patron in self.patrons.values():
            patron.display()


# ---------------- MAIN PROGRAM ---------------- #

lib = library()

# Add Books
lib.add_books(books(101, "SHRIMAN YOGI", "Ranjeet Desai"))
lib.add_books(books(102, "Budhbhushan", "CHH. SAMBHAJI SHIVAJI BHOSALE "))
lib.add_books(books(103, "CHHAVA", " Shivaji Sawant"))
lib.add_books(books(104, "Samrat Balasaheb Thackeray", "Sujata Anandan "))

# Register Patrons
lib.add_patron(patron(1, "raj"))
lib.add_patron(patron(2, "piyyaa"))

# Display Books
lib.display_books()

# Borrow Books
print("\nBorrowing Books")
lib.borrowed_books(1, 101)
lib.borrowed_books(2, 102)

# Display Books
lib.display_books()

# Return Book
print("\nReturning Book")
lib.return_book(1, 101)

# Display Books
lib.display_books()

# Display Patrons
lib.display_patrons()