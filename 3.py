# 3 Лабораторная.
# 4 Задание Интерактивный опросник с Radiobutton и Checkbutton
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Важный опрос ʕ ᵔᴥᵔ ʔ")
root.geometry("600x800")

def result():
    pass

label1 = tk.Label(
    root,
    text="Какая вы булочка? (^ ω ^)",
    font=("Arial", 18), # Установка шрифта и размера
    fg="red", # Цвет текста (foreground)
    bg="lightpink" # Цвет фона (background)
)
label1.pack(pady=20)

label2 = tk.Label(
    root,
    text="Введите ваше имя:",
    font=("Arial", 10), # Установка шрифта и размера
    fg="red", # Цвет текста (foreground)
)
label2.pack(pady=10)
entry = tk.Entry(root, width=30) # Ширина поля ввода
entry.pack(pady=5)

label3 = tk.Label(
    root,
    text="У тебя много друзей?",
    font=("Arial", 10), # Установка шрифта и размера
    fg="red", # Цвет текста (foreground)
)
label3.pack(anchor="w", padx=20, pady=10)


q1 = tk.StringVar() # Переменная для хранения выбранного значения
q1.set("a")

radio1 = tk.Radiobutton(
    root,
    text="Немного, но каждый на вес золота",
    variable=q1,
    value="a"
)
radio2 = tk.Radiobutton(
    root,
    text="Мне кажется, нет никого, кого бы я мог назвать другом",
    variable=q1,
    value="b"
)
radio3 = tk.Radiobutton(
    root,
    text="Да, так сразу и не сосчитаешь",
    variable=q1,
    value="c"
)
radio1.pack(anchor="w", padx=20, pady=5)
radio2.pack(anchor="w", padx=20, pady=5)
radio3.pack(anchor="w", padx=20, pady=5)

label4 = tk.Label(
    root,
    text="Если булочка, то обязательно...",
    font=("Arial", 10), # Установка шрифта и размера
    fg="red", # Цвет текста (foreground)
)
label4.pack(anchor="w", padx=20, pady=10)


q2 = tk.StringVar() # Переменная для хранения выбранного значения
q2.set("a")

radio1 = tk.Radiobutton(
    root,
    text="Со свежесваренным кофе",
    variable=q2,
    value="a"
)
radio2 = tk.Radiobutton(
    root,
    text="С апельсиновым соком – и обязательно свежевыжатым",
    variable=q2,
    value="b"
)
radio3 = tk.Radiobutton(
    root,
    text="С горячим чаем",
    variable=q2,
    value="c"
)
radio1.pack(anchor="w", padx=20, pady=5)
radio2.pack(anchor="w", padx=20, pady=5)
radio3.pack(anchor="w", padx=20, pady=5)

root.mainloop()
