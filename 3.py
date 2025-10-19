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