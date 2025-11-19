# 5 Лабораторная.
# 1 Анализатор текстового файла
import os
import tkinter as tk
from tkinter import messagebox, filedialog


filepath = None

def choose_file(i):
    global filepath
    if i =='a':
        filename = entry.get()
        for root, dirs, files in os.walk("C:/"):
            if filename in files:
                filepath = os.path.join(root, filename)

    elif i =='b':
        filepath = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt")]
        )
    if filepath:
        filename = os.path.basename(filepath)
        print("Выбранный файл", f"Файл выбран: {filename}")
    else:
        if i =='a':
            messagebox.showwarning("Внимание", "Файл не найден")
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, выбирите текстовый файл.")


def result():
    if not filepath: 
        return messagebox.showwarning("Внимание", "Пожалуйста, выбирите текстовый файл через обзор или поиск.")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        if text:
            count_lines = text.count('\n') + 1
            count_items = len(text)
            count_words = len(text.split())
            return messagebox.showinfo(
                "Инфо",
                f"Количество строк: {count_lines}\n"
                f"Количество символов: {count_items}\n"
                f"Количество слов: {count_words}"
            )
        return messagebox.showinfo(
            "Инфо",
            f"Ваш файл '{os.path.basename(filepath)}' пуст :("
        )
        

# --- Интерфейс ---
root: tk.Tk = tk.Tk()
root.title("Статистика по файлу")
root.geometry("350x350")

label1: tk.Label = tk.Label(root, text="Введите имя \nтекстового файла вручную:", font=("Arial", 14), fg="red")
label1.pack(pady=10)
entry: tk.Entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button1: tk.Button = tk.Button(root, text="Поиск по имени", command=lambda: choose_file('a'))
button1.pack(pady=5)

# Выбор файла
label2: tk.Label = tk.Label(root, text="Выбирите текстовый файл:", font=("Arial", 14), fg="blue")
label2.pack(pady=10)


# Кнопка
button2: tk.Button = tk.Button(root, text="Обзор файлов", command=lambda: choose_file('b'))
button2.pack(pady=5)

# Вопрос
label3: tk.Label = tk.Label(
    root,
    text="Хотите узнать, сколько\n строк, слов и символов в вашем файле?",
    font=("Arial", 12),
    fg="green")
label3.pack(pady=10)

# Кнопка
button3: tk.Button = tk.Button(root, text="Хочу!", command=result)
button3.pack(pady=5)

root.mainloop()
