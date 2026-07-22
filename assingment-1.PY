class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Patron ID: {self.patron_id}, Name: {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add exactly 5 books
    def add_books(self):
        print("\n ADD BOOKS ")

        for i in range(5):
            print(f"\nEnter details for Book {i + 1}")

            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            self.books[book_id] = book

            print(f"Book '{title}' added successfully.")

        print("\nAll 5 books have been added successfully!")

    # Register exactly 5 patrons
    def register_patrons(self):
        print("\nREGISTER PATRONS")

        for i in range(5):
            print(f"\nEnter details for Patron {i + 1}")

            patron_id = input("Enter Patron ID: ")
            name = input("Enter Patron Name: ")

            patron = Patron(patron_id, name)
            self.patrons[patron_id] = patron

            print(f"Patron '{name}' registered successfully.")

        print("\nAll 5 patrons have been registered successfully!")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)

            print(f"{patron.name} borrowed '{book.title}'.")


    # Return a book
    def return_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[patron_id]

        for book in patron.borrowed_books:

            if book.book_id == book_id:

                book.is_borrowed = False
                patron.borrowed_books.remove(book)

                print(f"{patron.name} returned '{book.title}'.")
                return

        print("This patron did not borrow the book.")


    # Display all books
    def display_books(self):

        print("\n LIBRARY BOOKS ")

        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            print(book)


    # Display all patrons
    def display_patrons(self):

        print("\n REGISTERED PATRONS ")

        if not self.patrons:
            print("No patrons registered.")
            return

        for patron in self.patrons.values():
            print(patron)


# ================= MAIN PROGRAM =================

library = Library()

while True:


    print("       LIBRARY MANAGEMENT SYSTEM")


    print("1. Add Books")
    print("2. Register Patrons")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Display All Patrons")
    print("7. Exit")



    choice = input("Enter your choice: ")


    # Add 5 books
    if choice == "1":

        library.add_books()


    # Register 5 patrons
    elif choice == "2":

        library.register_patrons()


    # Borrow book
    elif choice == "3":

        print("\n BORROW BOOK ")

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.borrow_book(patron_id, book_id)


    # Return book
    elif choice == "4":

        print("\n RETURN BOOK ")

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.return_book(patron_id, book_id)


    # Display books
    elif choice == "5":

        library.display_books()


    # Display patrons
    elif choice == "6":

        library.display_patrons()


    # Exit
    elif choice == "7":

        print("\nExiting Library Management System.")
        break


    # Invalid choice
    else:

        print("\nInvalid choice! Please try again.")
