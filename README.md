# 📚 Library Manager

A simple command-line library management system written in Python. This project allows users to manage a collection of books by adding, removing, viewing, and searching for books. Book data is stored persistently in a text file.

---

## 📁 Project Structure


---

## ✅ Features

- Add a book (title and author)
- Remove a book by title
- View all books in the library
- Search for a specific book by title
- Persistent storage in `library.txt`

---

## 📘 Classes Overview

**libraryClass.py** contains:

### `Book`

Represents a book with the following attributes:

- `author`: Name of the book’s author
- `title`: Title of the book

Method:
- `display_info()`: Returns a string with book information

### `library`

Represents the library and provides functionality to:

- `add_book(book)`: Adds a book to `library.txt`
- `remove_book()`: Removes a book (by title) from `library.txt`
- `sBook()`: Searches for a book by title
- `showBooks()`: Displays all books in the library

---

## 🖥️ How to Use

1. Make sure you have Python 3 installed.
2. Clone or download the project into a directory called `libraryManager`.
3. Run the main file:

```bash
python libraryUI.py
