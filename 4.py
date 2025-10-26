import tkinter as tk
import abc

class DataPointVisualizer(abc.ABC):
    @abc.abstractmethod
    def show_point(self, canvas):
        pass


class SimpleDataPointVisualizer(DataPointVisualizer):
    def __init__(self, x, y):
        self._color = "blue"
        self._width = 2
        self._lable = None
        self._x = x
        self._y = y

    def show_point(self, canvas):
        return canvas.create_rectangle(
            self._x+50, 350-self._y,
            self._x+51, 349-self._y,
            outline=self._color, width=self._width
        )


class PointDecorator(DataPointVisualizer, abc.ABC):
    def __init__(self, decorated_point: DataPointVisualizer):
        self._decorated_point = decorated_point

    @abc.abstractmethod
    def show_point(self, canvas):
        pass


class LabelDecorator(PointDecorator):
    
    def show_point(self, canvas):
        point_id = self._decorated_point.show_point(canvas)
        canvas.create_text(self._decorated_point._x + 55, 350 - self._decorated_point._y,
                           text=f"({self._decorated_point._x}, {self._decorated_point._y})",
                           anchor="w", font=("Arial", 9), fill="black")
        return point_id


class TooltipDecorator(PointDecorator):
    def show_point(self, canvas):
        point_id = self._decorated_point.show_point(canvas)
        tooltip = tk.Label(canvas, text=f"Точка: ({self._decorated_point._x}, {self._decorated_point._y})",
                           bg="lightyellow", relief="solid", bd=1, font=("Arial", 8))
        tooltip.place_forget()

        def on_enter(event):
            tooltip.place(x=event.x + 10, y=event.y - 10)

        def on_leave(event):
            tooltip.place_forget()

        canvas.tag_bind(point_id, "<Enter>", on_enter)
        canvas.tag_bind(point_id, "<Leave>", on_leave)
        return point_id


class HighlightDecorator(PointDecorator):
    def show_point(self, canvas):
        point_id = self._decorated_point.show_point(canvas)

        def on_enter(event):
            canvas.itemconfig(point_id, fill="red", outline="red")

        def on_leave(event):
            canvas.itemconfig(point_id, fill="blue", outline="blue")

        canvas.tag_bind(point_id, "<Enter>", on_enter)
        canvas.tag_bind(point_id, "<Leave>", on_leave)
        return point_id  

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
button = tk.Button(
    root, text="Отобразить точку",
    command=lambda: show_point(
        int(message_entry_x.get()),
        int(message_entry_y.get())
        )
    )
button.pack(pady=5)

root.mainloop()
