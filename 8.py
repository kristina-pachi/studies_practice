# 8 Лабораторная.
# 1  Система управления библиотекой.

import sqlite3

class Library:
    def __init__(self, db_name="library.db"):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        """Создаём таблицу и заполняем её 5 книгами, если она пуста."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER,
                    isbn TEXT UNIQUE
                )
            ''')
            cursor.execute("SELECT COUNT(*) FROM books")
            count = cursor.fetchone()[0]
            if count == 0:
                books = [
                    ("Война и мир", "Лев Толстой", 1869, "ISBN001"),
                    ("Преступление и наказание", "Фёдор Достоевский", 1866, "ISBN002"),
                    ("Мастер и Маргарита", "Михаил Булгаков", 1967, "ISBN003"),
                    ("Евгений Онегин", "Александр Пушкин", 1833, "ISBN004"),
                    ("Анна Каренина", "Лев Толстой", 1877, "ISBN005"),
                ]
                cursor.executemany(
                    "INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", books
                )
                conn.commit()
                print("База данных заполнена 5 книгами.")

    def add_book(self):
        print("\nДобовляем книгу в библиотеку")
        title = input("Введите название книги: ")
        author = input("Введите автора: ")
        year = int(input("Введите год издания: "))
        isbn = input("Введите ISBN: ")
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                    (title, author, year, isbn),
                )
                conn.commit()
                print("Книга успешно добавлена.")
            except sqlite3.IntegrityError:
                print("Ошибка: книга с таким ISBN уже существует.")

    def show_books(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            print("\nВсе книги:")
            for book in books:
                print(book)

    def search_books(self):
        query = "%" + input("Введите строку для поиска (автор или название): ") + "%"
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM books WHERE author LIKE ? OR title LIKE ?", (query, query)
            )
            results = cursor.fetchall()
            print("\nРезультаты поиска:")
            for book in results:
                print(book)

    def update_year(self):
        print("\nОбновляем год издания книги по id")
        book_id = int(input("Введите id книги: "))
        new_year = int(input("Введите новый год издания: "))
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET year = ? WHERE id = ?", (new_year, book_id))
            conn.commit()
            print("Год издания обновлён.")

    def delete_book(self):
        print("\nУдаляем книгу по id")
        book_id = int(input("Введите id книги для удаления: "))
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()
            print("Книга удалена.")


library = Library()

library.show_books()       # показать все книги
library.search_books()     # поиск по автору/названию
library.add_book()         # добавить книгу
library.update_year()      # обновить год издания
library.delete_book()      # удалить книгу
library.show_books()       # показать книги после изменений