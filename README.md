# Python_indiviual-_project_Library-Managment-System
📚 Library Management System — Python Project

This is a Library Management System written in Python. It allows users to sign up, log in, and then manage or use books depending on their role — either Admin or User.

✅ Features

User Authentication (Login/Signup)

Admin Panel:

Add books

View books

Delete books

User Panel:

View books

Issue books

Return books

Persistent Storage using Text Files

(Optional) Book statistics with matplotlib

💡 How It Works

1. User Roles

Admin: Can add, view, and delete books.

User: Can view, issue, and return books.

2. Program Flow

Start the program with a menu: Login, Sign Up, or Exit.

Sign Up: Stores username, password, and role in users.txt.

Login: Checks credentials and grants access.

Based on user role, shows the appropriate menu.

3. Admin Menu

Add Book

View Books

Delete Book

Logout

4. User Menu

View Books

Issue Book

Return Book

Logout

📦 Book Management (Library Class)

Books are stored in books.txt.

Book attributes:

Book ID

Title

Author

Genre

Availability (True/False)

Methods:

add_book() — Add a book to the library.

view_books() — Display all books.

issue_book() — Mark a book as issued.

return_book() — Mark a book as returned.

delete_book() — Delete a book (if available).

reassign_book_ids() — Reorder book IDs after deletion.

save_books_to_file() / load_books_from_file() — Handle file operations.

👤 User Management (Authentication Class)

User data stored in users.txt.

Attributes: Username, Password, Role

Methods:

signup() — Register a new user.

login() — Log in an existing user.

📊 Optional: Plot Book Statistics

plot_books_data() shows a bar chart comparing stored vs issued books.

Uses matplotlib.

⚠️ Note: This function is not included in the menu by default.

📁 Files Used

books.txt – Stores book records.

users.txt – Stores user login details.

These are plain text files that preserve your data between runs.

🛠 Technologies Used

Python (Basic Programming + File Handling)

os module

matplotlib.pyplot (Optional)

⚠️ Limitations

Passwords stored in plain text — not secure.

No input validation (e.g., non-numeric Book IDs).

Book IDs are reassigned after deletion — not ideal for real-world systems.

No error handling for incorrect data types.

User ID is based on username length — not unique.

🟢 Summary

This is a simple, text-based Library Management System designed for beginners learning Python. It includes core features like login, book issuing/returning, and file-based data storage.

🔄 Future Improvements

Secure password storage

Add error handling

Store data using a database (e.g., MySQL)

Add GUI (Tkinter, PyQt)

Add search/filter features

Happy coding! 🎉

