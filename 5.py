# 5 Лабораторная.
# 1 Анализатор текстового файла
import os
import tkinter as tk
from tkinter import messagebox, filedialog


def choose_file():
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
    pass

# --- Интерфейс ---
root: tk.Tk = tk.Tk()
root.title("Статистика по файлу")
root.geometry("300x200")

# Выбор файла
label: tk.Label = tk.Label(root, text="Выбирите текстовый файл:", font=("Arial", 10), fg="blue")
label.pack(pady=10)


# Кнопка
button: tk.Button = tk.Button(root, text="Обзор файлов", command=choose_file)
button.pack(pady=5)

root.mainloop()
