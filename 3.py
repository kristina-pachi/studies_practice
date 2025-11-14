# 3 Лабораторная.
# 4 Задание Интерактивный опросник с Radiobutton и Checkbutton
import tkinter as tk
from tkinter import messagebox

def result() -> None:
    """
    Обрабатывает результаты опроса, определяет тип булочки на основе ответов
    и отображает соответствующее сообщение.
    """
    name: str = entry.get()  # Получаем текст из поля ввода
    answers: list[str] = [q1.get(), q2.get(), q3.get(), q4.get()]  # Все ответы

    # Считаем количество каждого типа
    scores: dict[str, int] = {'a': 0, 'b': 0, 'c': 0}
    for ans in answers:
        if ans in scores:
            scores[ans] += 1

    # Находим тип с максимальным количеством баллов
    max_type: str = max(scores, key=scores.get)

    # Формируем результат в зависимости от типа
    if max_type == 'a':
        res: str = (
            "Ты – булочка с маком, и пока одни в тебе души не чают, другие предпочитают обходить за километр. "
            "Да, с некоторыми тебе не по пути, зато те, кто смог «распробовать начинку», ни за что не останутся разочарованными."
        )
    elif max_type == 'b':
        res = (
            "Ты – булочка с изюмом. Скажем прямо – характер у тебя, судя по всему, не из простых, "
            "но тем ценнее становятся люди, которые смогли его раскусить и принять во всем многообразии. "
            "Впрочем, кто знает, где еще у тебя припрятана горстка изюма?"
        )
    else:
        res = (
            "Ты – «Московская» плюшка, а это значит, что тебя просто невозможно не любить. "
            "Идеальное комбо мягкого хлеба и сахарной сладости автоматически делают любой день лучше – как и ты своим появлением."
        )

    if name:
        messagebox.showinfo("Результат", f"{name}, {res}!")
    else:
        messagebox.showwarning("Внимание", "Пожалуйста, введите ваше имя.")

# --- Интерфейс ---
root: tk.Tk = tk.Tk()
root.title("Важный опрос ʕ ᵔᴥᵔ ʔ")
root.geometry("600x800")

# Заголовок
label1: tk.Label = tk.Label(
    root,
    text="Какая ты булочка? (^ ω ^)",
    font=("Arial", 18),
    fg="red",
    bg="lightpink"
)
label1.pack(pady=20)

# Имя
label2: tk.Label = tk.Label(root, text="Введите ваше имя:", font=("Arial", 10), fg="red")
label2.pack(pady=10)
entry: tk.Entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Вопрос 1
label3: tk.Label = tk.Label(root, text="У тебя много друзей?", font=("Arial", 10), fg="red")
label3.pack(anchor="w", padx=20, pady=10)

q1: tk.StringVar = tk.StringVar()
q1.set("a")

radio1: tk.Radiobutton = tk.Radiobutton(root, text="Немного, но каждый на вес золота", variable=q1, value="a")
radio2: tk.Radiobutton = tk.Radiobutton(root, text="Мне кажется, нет никого, кого бы я мог назвать другом", variable=q1, value="b")
radio3: tk.Radiobutton = tk.Radiobutton(root, text="Да, так сразу и не сосчитаешь", variable=q1, value="c")
radio1.pack(anchor="w", padx=20, pady=5)
radio2.pack(anchor="w", padx=20, pady=5)
radio3.pack(anchor="w", padx=20, pady=5)

# Вопрос 2
label4: tk.Label = tk.Label(root, text="Если булочка, то обязательно...", font=("Arial", 10), fg="red")
label4.pack(anchor="w", padx=20, pady=10)

q2: tk.StringVar = tk.StringVar()
q2.set("a")

radio1 = tk.Radiobutton(root, text="Со свежесваренным кофе", variable=q2, value="a")
radio2 = tk.Radiobutton(root, text="С апельсиновым соком – и обязательно свежевыжатым", variable=q2, value="b")
radio3 = tk.Radiobutton(root, text="С горячим чаем", variable=q2, value="c")
radio1.pack(anchor="w", padx=20, pady=5)
radio2.pack(anchor="w", padx=20, pady=5)
radio3.pack(anchor="w", padx=20, pady=5)

# Вопрос 3
label5: tk.Label = tk.Label(root, text="Какой жанр фильмов тебе нравится больше?", font=("Arial", 10), fg="red")
label5.pack(anchor="w", padx=20, pady=10)

q3: tk.StringVar = tk.StringVar()
q3.set("a")

radio1 = tk.Radiobutton(root, text="Детектив", variable=q3, value="a")
radio2 = tk.Radiobutton(root, text="Мелодрама", variable=q3, value="b")
radio3 = tk.Radiobutton(root, text="Комедия", variable=q3, value="c")
radio1.pack(anchor="w", padx=20, pady=5)
radio2.pack(anchor="w", padx=20, pady=5)
radio3.pack(anchor="w", padx=20, pady=5)

# Вопрос 4
label6: tk.Label = tk.Label(root, text="Какой стиль одежды тебе нравится?", font=("Arial", 10), fg="red")
label6.pack(anchor="w", padx=20, pady=10)

q4: tk.StringVar = tk.StringVar()
q4.set("a")

radio1 = tk.Radiobutton(root, text="Строгая классика", variable=q4, value="a")
radio2 = tk.Radiobutton(root, text="Я за комфорт и практически не вылезаю из оверсайза", variable=q4, value="b")
radio3 = tk.Radiobutton(root, text="Люблю следовать трендам", variable=q4, value="c")
radio1.pack(anchor="w", padx=20, pady=5)
radio2.pack(anchor="w", padx=20, pady=5)
radio3.pack(anchor="w", padx=20, pady=5)

# Кнопка отправки
button: tk.Button = tk.Button(root, text="Отправить", command=result)
button.pack(pady=5)

root.mainloop()