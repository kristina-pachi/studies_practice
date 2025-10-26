# 4 Лабораторная.
# 3 Задание Система визуализации данных (GUI + Декоратор)
import tkinter as tk
import abc

class DataPointVisualizer(abc.ABC):
    """Абстрактный базовый класс для визуализаторов точек данных."""

    @abc.abstractmethod
    def show_point(self, canvas: tk.Canvas) -> int:
        """Отображает точку на Canvas и возвращает ID созданного элемента."""
        pass


class SimpleDataPointVisualizer(DataPointVisualizer):
    """Базовая реализация визуализатора точки."""

    def __init__(self, x: int, y: int) -> None:
        """
        Инициализация точки с координатами x и y.

        :param x: Абсцисса точки
        :param y: Ордината точки
        """
        self._color: str = "blue"
        self._width: int = 2
        self._lable = None
        self._x: int = x
        self._y: int = y

    def show_point(self, canvas: tk.Canvas) -> int:
        """Рисует точку как маленький прямоугольник на Canvas."""
        return canvas.create_rectangle(
            self._x + 50, 350 - self._y,
            self._x + 51, 349 - self._y,
            outline=self._color, width=self._width
        )


class PointDecorator(DataPointVisualizer, abc.ABC):
    """Абстрактный декоратор для точек данных."""

    def __init__(self, decorated_point: DataPointVisualizer) -> None:
        """
        Инициализация декоратора.

        :param decorated_point: Объект, который нужно декорировать
        """
        self._decorated_point: DataPointVisualizer = decorated_point

    @abc.abstractmethod
    def show_point(self, canvas: tk.Canvas) -> int:
        """Отображает точку с дополнительной функциональностью."""
        pass


class LabelDecorator(PointDecorator):
    """Декоратор, добавляющий метку рядом с точкой."""

    def show_point(self, canvas: tk.Canvas) -> int:
        """Рисует точку и отображает координаты рядом с ней."""
        point_id: int = self._decorated_point.show_point(canvas)
        canvas.create_text(
            self._decorated_point._x + 55,
            350 - self._decorated_point._y,
            text=f"({self._decorated_point._x}, {self._decorated_point._y})",
            anchor="w", font=("Arial", 9), fill="black"
        )
        return point_id


class TooltipDecorator(PointDecorator):
    """Декоратор, добавляющий всплывающую подсказку при наведении."""

    def show_point(self, canvas: tk.Canvas) -> int:
        """Рисует точку и добавляет всплывающую подсказку при наведении."""
        point_id: int = self._decorated_point.show_point(canvas)
        tooltip: tk.Label = tk.Label(
            canvas,
            text=f"Точка: ({self._decorated_point._x}, {self._decorated_point._y})",
            bg="lightyellow", relief="solid", bd=1, font=("Arial", 8)
        )
        tooltip.place_forget()

        def on_enter(event: tk.Event) -> None:
            tooltip.place(x=event.x + 10, y=event.y - 10)

        def on_leave(event: tk.Event) -> None:
            tooltip.place_forget()

        canvas.tag_bind(point_id, "<Enter>", on_enter)
        canvas.tag_bind(point_id, "<Leave>", on_leave)
        return point_id


class HighlightDecorator(PointDecorator):
    """Декоратор, изменяющий цвет точки при наведении."""

    def show_point(self, canvas: tk.Canvas) -> int:
        """Рисует точку и добавляет эффект выделения при наведении."""
        point_id: int = self._decorated_point.show_point(canvas)

        def on_enter(event: tk.Event) -> None:
            canvas.itemconfig(point_id, fill="red", outline="red")

        def on_leave(event: tk.Event) -> None:
            canvas.itemconfig(point_id, fill="blue", outline="blue")

        canvas.tag_bind(point_id, "<Enter>", on_enter)
        canvas.tag_bind(point_id, "<Leave>", on_leave)
        return point_id


class PointVisualizerApp:
    """GUI-приложение для отображения точек с декораторами."""

    def __init__(self, master: tk.Tk) -> None:
        """
        Инициализация интерфейса приложения.

        :param master: Корневой элемент Tkinter
        """
        self.master: tk.Tk = master
        master.title("Визуализация точек с декораторами")
        master.geometry("600x550")

        self.canvas: tk.Canvas = tk.Canvas(master, width=580, height=380, bg="#F0F0F0", bd=2, relief="sunken")
        self.canvas.pack(pady=10)

        self._draw_axes()
        self._build_controls()

    def _draw_axes(self) -> None:
        """Рисует координатную сетку на Canvas."""
        self.canvas.create_line(50, 350, 530, 350, fill="red", width=1)
        self.canvas.create_line(50, 350, 50, 30, fill="red", width=1)
        for i in range(50, 501, 50):
            self.canvas.create_text(i, 360, text=f"{i - 50}", fill="blue", font=("Arial", 10))
            self.canvas.create_rectangle(i, 351, i + 1, 351, outline="blue", width=2)
        for i in range(300, 0, -50):
            self.canvas.create_text(35, i, text=f"{350 - i}", fill="blue", font=("Arial", 10))
            self.canvas.create_rectangle(50, i, 49, i - 1, outline="blue", width=2)

    def _build_controls(self) -> None:
        """Создает элементы управления для ввода координат и выбора декораторов."""
        entry_frame: tk.Frame = tk.Frame(self.master)
        entry_frame.pack(pady=10)

        self.entry_x: tk.Entry = tk.Entry(entry_frame, width=20)
        self.entry_x.grid(row=0, column=0, padx=5)
        self.entry_x.insert(0, "X")

        self.entry_y: tk.Entry = tk.Entry(entry_frame, width=20)
        self.entry_y.grid(row=0, column=1, padx=5)
        self.entry_y.insert(0, "Y")

        decorator_frame: tk.Frame = tk.Frame(self.master)
        decorator_frame.pack(pady=5)

        self.label_var: tk.BooleanVar = tk.BooleanVar()
        self.tooltip_var: tk.BooleanVar = tk.BooleanVar()
        self.highlight_var: tk.BooleanVar = tk.BooleanVar()

        tk.Checkbutton(decorator_frame, text="Метка", variable=self.label_var).grid(row=0, column=0, padx=5)
        tk.Checkbutton(decorator_frame, text="Подсказка", variable=self.tooltip_var).grid(row=0, column=1, padx=5)
        tk.Checkbutton(decorator_frame, text="Выделение", variable=self.highlight_var).grid(row=0, column=2, padx=5)

        tk.Button(self.master, text="Добавить точку", command=self._on_add_point).pack(pady=10)

    def _on_add_point(self) -> None:
        """Обрабатывает добавление новой точки с выбранными декораторами."""
        try:
            x: int = int(self.entry_x.get())
            y: int = int(self.entry_y.get())
        except ValueError:
            print("Ошибка: введите целые числа")
            return

        point: DataPointVisualizer = SimpleDataPointVisualizer(x, y)
        if self.label_var.get():
            point = LabelDecorator(point)
        if self.tooltip_var.get():
            point = TooltipDecorator(point)
        if self.highlight_var.get():
            point = HighlightDecorator(point)

        point.show_point(self.canvas)


root: tk.Tk = tk.Tk()
app: PointVisualizerApp = PointVisualizerApp(root)
root.mainloop()