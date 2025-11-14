# 5 Лабораторная.
# 1 Анализатор текстового файла
import tkinter as tk
from tkinter import messagebox

def result():
    name_of_file = entry.get()
    if name_of_file:
        messagebox.showinfo("Результат", name_of_file)
    else:
        messagebox.showwarning("Внимание", "Пожалуйста, введите имя файла.")

# --- Интерфейс ---
root: tk.Tk = tk.Tk()
root.title("Статистика по файлу")
root.geometry("300x200")

# Ввод имени файла
label2: tk.Label = tk.Label(root, text="Введите имя файла:", font=("Arial", 10), fg="blue")
label2.pack(pady=10)
entry: tk.Entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Кнопка
button: tk.Button = tk.Button(root, text="Отправить", command=result)
button.pack(pady=5)

root.mainloop()