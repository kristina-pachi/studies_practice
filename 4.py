import tkinter as tk

def show_point(x, y):
    return canvas.create_rectangle(x+50, 350-y, x+51, 349-y, outline="blue", width=2)

root = tk.Tk()
root.title("Пример Canvas: Рисование фигур")
root.geometry("600x550")
canvas = tk.Canvas(root, width=580, height=380, bg="#F0F0F0", bd=2, relief="sunken")
canvas.pack(pady=10, padx=10)
# Рисуем Систему координат
canvas.create_line(50, 350, 530, 350, fill="red", width=1)
canvas.create_line(50, 350, 50, 30, fill="red", width=1)
for i in range(50, 501, 50):
    canvas.create_text(i, 360, text=f"{i-50}", fill="blue", font=("Arial", 10))
    canvas.create_rectangle(i, 351, i+1, 351, outline="blue", width=2)
for i in range(300, 0, -50):
    canvas.create_text(35, i, text=f"{350-i}", fill="blue", font=("Arial", 10))
    canvas.create_rectangle(50, i, 49, i-1, outline="blue", width=2)
message_entry_x = tk.Entry(root, width=40)
message_entry_x.pack(pady=10)
message_entry_x.insert(0, "Введите абсциссу точки")
message_entry_y = tk.Entry(root, width=40)
message_entry_y.pack(pady=10)
message_entry_y.insert(0, "Введите ординату точки")
button = tk.Button(root, text="Отобразить точку", command=lambda: show_point(int(message_entry_x.get()), int(message_entry_y.get())))
button.pack(pady=5)

root.mainloop()
