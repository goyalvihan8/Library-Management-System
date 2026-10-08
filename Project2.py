from abc import ABC, abstractmethod
import csv
import os


# ==========================================================
# 1. ABSTRACT BASE CLASS
# ==========================================================

class Book(ABC):

    def __init__(self, Name, Author, Serial_Number):

        # Encapsulation
        self.__Name = Name
        self.__Author = Author
        self.__Serial_Number = Serial_Number

    def display_available_books(self):

        print("Name:", self.__Name)
        print("Author:", self.__Author)
        print("Serial Number:", self.__Serial_Number)

    # ---------------- GETTERS ----------------

    def get_Name(self):
        return self.__Name

    def get_Author(self):
        return self.__Author

    def get_Serial_Number(self):
        return self.__Serial_Number

    # ---------------- SETTER ----------------

    def set_Name(self, Name):
        self.__Name = Name

    # ---------------- ABSTRACTION ----------------

    @abstractmethod
    def library_name(self):
        pass


# ==========================================================
# 2. DERIVED CLASS - INHERITANCE
# ==========================================================

class Library_Name(Book):

    def library_name(self):
        return "Government Maharaja Public Library"


# ==========================================================
# 3. LIBRARY MANAGEMENT SYSTEM
# ==========================================================

class Library_Management_System:

    def __init__(self):

        self.books = []
        self.issued_book = []


    # ------------------------------------------------------
    # ADD BOOK
    # ------------------------------------------------------

    def add_books(self):

        Name = input("Enter The Name Of The Book: ")
        Author = input("Enter The Author Name Of The Book: ")
        Serial_Number = input("Enter The Serial Number Of The Book: ")

        # Check duplicate serial number
        for book in self.books + self.issued_book:

            if book.get_Serial_Number() == Serial_Number:

                print("Serial Number Already Exists...")
                return

        # Create object of derived class
        book = Library_Name(
            Name,
            Author,
            Serial_Number
        )

        self.books.append(book)

        print("Book Added Successfully...")


    # ------------------------------------------------------
    # SEARCH BOOK
    # ------------------------------------------------------

    def search_book(self):

        Serial_Number = input(
            "Enter The Serial Number Of The Book: "
        )

        for book in self.books + self.issued_book:

            if book.get_Serial_Number() == Serial_Number:

                print("Book Found...")
                book.display_available_books()

                if book in self.books:
                    print("Status: Available")
                else:
                    print("Status: Issued")

                return

        print("Book Not Found...")


    # ------------------------------------------------------
    # ISSUE BOOK
    # ------------------------------------------------------

    def issue_book(self):

        Serial_Number = input(
            "Enter The Serial Number Of The Book: "
        )

        for book in self.books:

            if book.get_Serial_Number() == Serial_Number:

                self.books.remove(book)
                self.issued_book.append(book)

                print("Book Issued Successfully...")
                return

        print("Book Not Found Or Already Issued...")


    # ------------------------------------------------------
    # RETURN BOOK
    # ------------------------------------------------------

    def return_book(self):

        Serial_Number = input(
            "Enter The Serial Number Of The Book: "
        )

        for book in self.issued_book:

            if book.get_Serial_Number() == Serial_Number:

                self.issued_book.remove(book)
                self.books.append(book)

                print("Book Returned Successfully...")
                return

        print("Book Not Found In Issued Books...")


    # ------------------------------------------------------
    # DISPLAY AVAILABLE BOOKS
    # ------------------------------------------------------

    def display_available_book(self):

        if len(self.books) == 0:

            print("No Available Book Found...")
            return

        print("\n----- Available Books -----")

        for book in self.books:

            book.display_available_books()
            print("---------------------------")


    # ------------------------------------------------------
    # SAVE RECORD
    # ------------------------------------------------------

    def save_record(self):

        try:

            with open("Book.csv", "w") as bk:

                # Save available books
                for book in self.books:

                    bk.write(
                        book.get_Name() + "," +
                        book.get_Author() + "," +
                        book.get_Serial_Number() + "," +
                        "Available\n"
                    )

                # Save issued books
                for book in self.issued_book:

                    bk.write(
                        book.get_Name() + "," +
                        book.get_Author() + "," +
                        book.get_Serial_Number() + "," +
                        "Issued\n"
                    )

            print("Record Saved Successfully...")

        except OSError:

            print("Error While Saving File...")


    # ------------------------------------------------------
    # LOAD RECORD
    # ------------------------------------------------------

    def load_record(self):

        try:

            with open("Book.csv", "r") as bk:

                for line in bk:

                    line = line.strip()

                    if not line:
                        continue

                    data = line.split(",", 3)

                    if len(data) < 4:
                        continue

                    Name = data[0]
                    Author = data[1]
                    Serial_Number = data[2]
                    Status = data[3]

                    book = Library_Name(
                        Name,
                        Author,
                        Serial_Number
                    )

                    if Status == "Issued":

                        self.issued_book.append(book)

                    else:

                        self.books.append(book)

            print("Previous Data Loaded Successfully...")

        except FileNotFoundError:

            print("No Previous Record Found.")

        except OSError:

            print("Error While Reading File...")


# ==========================================================
# MAIN PROGRAM
# ==========================================================

system = Library_Management_System()

# Load previous library records
system.load_record()


while True:

    print("\n====== Library Management System ======")

    print("1. Add Books")
    print("2. Search Books")
    print("3. Issue Books")
    print("4. Return Books")
    print("5. Display Available Books")
    print("6. Save Records")
    print("7. Exit")

    choice = input("Enter The Choice: ")

    if choice == "1":

        system.add_books()

    elif choice == "2":

        system.search_book()

    elif choice == "3":

        system.issue_book()

    elif choice == "4":

        system.return_book()

    elif choice == "5":

        system.display_available_book()

    elif choice == "6":

        system.save_record()

    elif choice == "7":

        system.save_record()

        print("Program Exited...")
        break

    else:

        print("Invalid Choice...")
