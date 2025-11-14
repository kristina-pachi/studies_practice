# 5 Лабораторная.
# 1 Анализатор текстового файла
import os
import tkinter as tk
from tkinter import messagebox, filedialog


filepath = None

def choose_file():
    global filepath
    filepath = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt")]
    )
    if filepath:
        filename = os.path.basename(filepath)
        messagebox.showinfo("Выбранный файл", f"Файл выбран: {filename}")
    else:
        messagebox.showwarning("Внимание", "Пожалуйста, выбирите текстовый файл.")


def result():
    if not filepath: 
        messagebox.showwarning("Внимание", "Пожалуйста, выбирите текстовый файл.")
    with open(filepath, "r", encoding="utf-8") as f:
        count_lines = len(f.readlines())
        print(count_lines)
        messagebox.showinfo("Инфо", f"Количество строк: {count_lines}")

# --- Интерфейс ---
root: tk.Tk = tk.Tk()
root.title("Статистика по файлу")
root.geometry("300x250")

# Выбор файла
label: tk.Label = tk.Label(root, text="Выбирите текстовый файл:", font=("Arial", 14), fg="blue")
label.pack(pady=10)


# Кнопка
button: tk.Button = tk.Button(root, text="Обзор файлов", command=choose_file)
button.pack(pady=5)

# Вопрос
label: tk.Label = tk.Label(
    root,
    text="Хотите узнать, сколько\n строк, слов и символов в вашем файле?",
    font=("Arial", 10),
    fg="black")
label.pack(pady=20)

# Кнопка
button: tk.Button = tk.Button(root, text="Хочу!", command=result)
button.pack(pady=5)

root.mainloop()
