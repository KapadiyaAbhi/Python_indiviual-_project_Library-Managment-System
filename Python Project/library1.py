import os

class Book:
    def __init__(self, book_id, title, author, genre, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = is_available

class Library:
    BOOK_FILE = "books.txt"

    def __init__(self):
        self.books = []
        self.load_books_from_file()

    def save_books_to_file(self):
        """Saves the books list to a text file."""
        with open(self.BOOK_FILE, "w") as file:
            for book in self.books:
                file.write(f"{book.book_id},{book.title},{book.author},{book.genre},{book.is_available}\n")

    def load_books_from_file(self):
        """Loads books from the text file into the program."""
        if not os.path.exists(self.BOOK_FILE):
            return
        with open(self.BOOK_FILE, "r") as file:
            for line in file:
                book_id, title, author, genre, is_available = line.strip().split(",")
                self.books.append(Book(int(book_id), title, author, genre, is_available == "True"))

    def add_book(self, title, author, genre):
        """Adds a book and saves it to the file."""
        book_id = len(self.books) + 1
        self.books.append(Book(book_id, title, author, genre))
        self.save_books_to_file()
        print("Book added successfully!")

    def view_books(self):
        """Displays the list of books."""
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            status = "Available" if book.is_available else "Issued"
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Status: {status}")

    def issue_book(self, book_id):
        """Issues a book and updates the file."""
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                self.save_books_to_file()
                print("Book issued successfully!")
                return
        print("Book not available or invalid ID.")

    def return_book(self, book_id):
        """Returns a book and updates the file."""
        for book in self.books:
            if book.book_id == book_id and not book.is_available:
                book.is_available = True
                self.save_books_to_file()
                print("Book returned successfully!")
                return
        print("Invalid book ID or book not issued.")

    def delete_book(self, book_id):
        """Deletes a book only if it is available."""
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    print("Book is issued and cannot be deleted.")
                    return
                self.books.remove(book)
                self.reassign_book_ids()
                self.save_books_to_file()
                print("Book deleted successfully!")
                return
        print("Invalid book ID.")

    def reassign_book_ids(self):
        """Reassigns book IDs after deletion to keep them sequential."""
        for index, book in enumerate(self.books, start=1):
            book.book_id = index

    def plot_books_data(self):
        """Plots a graph showing the number of books issued and stored."""
        issued_books = sum(not book.is_available for book in self.books)
        stored_books = sum(book.is_available for book in self.books)

        labels = ['Stored Books', 'Issued Books']
        values = [stored_books, issued_books]

        plt.figure(figsize=(6, 4))
        plt.bar(labels, values, color=['green', 'red'])
        plt.xlabel('Book Status')
        plt.ylabel('Number of Books')
        plt.title('Library Book Distribution')
        plt.show()



class User:
    def __init__(self, user_id, username, role):
        self.user_id = user_id
        self.username = username
        self.role = role

class Authentication:
    USER_FILE = "users.txt"

    
    def signup():
        username = input("Enter a new username: ")
        password = input("Enter a password: ")
        role = input("Enter role (Admin/User): ").lower()
        with open(Authentication.USER_FILE, "a") as file:
            file.write(f"{username},{password},{role}\n")
        print("Signup successful! You can now log in.")


    def login():
        if not os.path.exists(Authentication.USER_FILE):
            print("No users found. Please sign up first.")
            return None
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open(Authentication.USER_FILE, "r") as file:
            for line in file:
                stored_username, stored_password, stored_role = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    print("Login successful!")
                    return User(len(username), username, stored_role)
        print("Invalid username or password.")
        return None

def main():
    while True:
        print("\n1. Login\n2. Sign Up\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            user = Authentication.login()
            if user:
                library_menu(user)
        elif choice == "2":
            Authentication.signup()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def library_menu(user):
    library = Library()
    
    print(f"\nHello, {user.username}! You are logged in as a {user.role.capitalize()}.")

    while True:
        if user.role == "admin":
            print("\n1. Add Book\n2. View Books\n3. Delete Book\n4. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter Book Title: ")
                author = input("Enter Book Author: ")
                genre = input("Enter Book Genre: ")
                library.add_book(title, author, genre)
            elif choice == "2":
                library.view_books()
            elif choice == "3":
                book_id = int(input("Enter Book ID to delete: "))
                library.delete_book(book_id)
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice, try again.")

        else:  # Normal user
            print("\n1. View Books\n2. Issue Book\n3. Return Book\n4. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                library.view_books()
            elif choice == "2":
                book_id = int(input("Enter Book ID to issue: "))
                library.issue_book(book_id)
            elif choice == "3":
                book_id = int(input("Enter Book ID to return: "))
                library.return_book(book_id)
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice, try again.")

main()