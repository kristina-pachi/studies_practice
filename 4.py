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

class PointVisualizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Визуализация точек с декораторами")
        master.geometry("600x550")

        self.canvas = tk.Canvas(master, width=580, height=380, bg="#F0F0F0", bd=2, relief="sunken")
        self.canvas.pack(pady=10)

        self._draw_axes()

        self._build_controls()

    def _draw_axes(self):
        self.canvas.create_line(50, 350, 530, 350, fill="red", width=1)
        self.canvas.create_line(50, 350, 50, 30, fill="red", width=1)
        for i in range(50, 501, 50):
            self.canvas.create_text(i, 360, text=f"{i-50}", fill="blue", font=("Arial", 10))
            self.canvas.create_rectangle(i, 351, i+1, 351, outline="blue", width=2)
        for i in range(300, 0, -50):
            self.canvas.create_text(35, i, text=f"{350-i}", fill="blue", font=("Arial", 10))
            self.canvas.create_rectangle(50, i, 49, i-1, outline="blue", width=2)

    def _build_controls(self):
        entry_frame = tk.Frame(self.master)
        entry_frame.pack(pady=10)

        self.entry_x = tk.Entry(entry_frame, width=20)
        self.entry_x.grid(row=0, column=0, padx=5)
        self.entry_x.insert(0, "X")

        self.entry_y = tk.Entry(entry_frame, width=20)
        self.entry_y.grid(row=0, column=1, padx=5)
        self.entry_y.insert(0, "Y")

        decorator_frame = tk.Frame(self.master)
        decorator_frame.pack(pady=5)
        self.label_var = tk.BooleanVar()
        self.tooltip_var = tk.BooleanVar()
        self.highlight_var = tk.BooleanVar()

        tk.Checkbutton(decorator_frame, text="Метка", variable=self.label_var).grid(row=0, column=0, padx=5)
        tk.Checkbutton(decorator_frame, text="Подсказка", variable=self.tooltip_var).grid(row=0, column=1, padx=5)
        tk.Checkbutton(decorator_frame, text="Выделение", variable=self.highlight_var).grid(row=0, column=2, padx=5)

        tk.Button(self.master, text="Добавить точку", command=self._on_add_point).pack(pady=10)

    def _on_add_point(self):
        try:
            x = int(self.entry_x.get())
            y = int(self.entry_y.get())
        except ValueError:
            print("Ошибка: введите целые числа")
            return

        point = SimpleDataPointVisualizer(x, y)
        if self.label_var.get():
            point = LabelDecorator(point)
        if self.tooltip_var.get():
            point = TooltipDecorator(point)
        if self.highlight_var.get():
            point = HighlightDecorator(point)

        point.show_point(self.canvas)


root = tk.Tk()
app = PointVisualizerApp(root)
root.mainloop()
