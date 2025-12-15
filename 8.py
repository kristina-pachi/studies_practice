# 8 Лабораторная.
# 1  Система управления библиотекой.

import sqlite3


with sqlite3.connect('library.db') as conn:
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

    try:
        print('Введите название, автора, год, ? книги через enter: ')
        title, author, year, isbn = [input() for _ in range(4)]
        cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", (title, author, int(year), isbn))
        conn.commit()
        print("Книга успешно добавлена в библиотеку.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback() 
    
    cursor.execute("SELECT * FROM books")
    all_books = cursor.fetchall() # Получить все строки
    print("\nВсе книги библиотеки:")

    for book in all_books:
        print(book)
    
    print('Поиск по названию или по автору')
    sourch = '%' + input('Введите строку из названия или автора: ') + '%'
    cursor.execute(f"SELECT * FROM books WHERE author LIKE ? OR title LIKE ?", (sourch, sourch))
    selected_books = cursor.fetchall()
    print("\nКниги по запросу:")

    for book in selected_books:
        print(book)
    
    print('Обновить год издания книги')
    id, new_year =[int(input('Введите id, новый год для книги: ')) for _ in range(2)]

    cursor.execute("UPDATE books SET year = ? WHERE id = ?", (new_year, id))
    cursor.execute(f"SELECT * FROM books WHERE id = ?", (id,))
    print('Год издания книги обновлен') 
    print(cursor.fetchone())
    
    print('Удаление книги')

    id = int(input('Введите id книги для удаления'))
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
