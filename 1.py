import abc

class Character(abc.ABC):
    """
    Абстрактный базовый класс для RPG-персонажа.

    Атрибуты:
        name (str): Имя персонажа
        lives (int): Количество жизней
        power (int): Сила атаки

    Методы:
        attack(): Абстрактный метод атаки
        defend(): Абстрактный метод защиты
        change_lives(delta): Изменяет количество жизней
    """

    def __init__(self, name, lives, power):
        """
        Инициализирует базовые параметры персонажа.

        Args:
            name (str): Имя персонажа
            lives (int): Количество жизней
            power (int): Сила атаки
        """
        self.__name = name
        self.__lives = lives
        self.__power = power

    @abc.abstractmethod
    def attack(self):
        """Абстрактный метод атаки."""
        pass

    @abc.abstractmethod
    def defend(self):
        """Абстрактный метод защиты."""
        pass

    @property
    def name(self):
        """Возвращает имя персонажа."""
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Устанавливает новое имя персонажа.

        Args:
            new_name (str): Новое имя
        """
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
            print(f"Имя персонажа изменено на: {self.__name}")
        else:
            print("Имя персонажа должно быть непустой строкой.")

    @property
    def lives(self):
        """Возвращает текущее количество жизней."""
        return self.__lives

    @lives.setter
    def lives(self, value):
        """
        Устанавливает новое значение жизней.

        Args:
            value (int): Новое значение
        """
        self.__lives = value

    def change_lives(self, delta):
        """
        Изменяет количество жизней персонажа.

        Args:
            delta (int): Изменение жизней (может быть отрицательным)

        Returns:
            bool: True, если персонаж мёртв, иначе False
        """
        if self.__lives <= 0:
            print(f'{self.__name} уже в другом мире... :(')
            return self.__lives == 0
        self.__lives += delta

    @property
    def power(self):
        """Возвращает силу персонажа."""
        return self.__power

    @power.setter
    def power(self, value):
        """
        Увеличивает силу персонажа.

        Args:
            value (int): Прибавка к силе
        """
        self.__power += value


class Warrior(Character):
    """Класс персонажа-Воин."""

    def attack(self, character):
        """
        Атакует другого персонажа.

        Args:
            character (Character): Цель атаки

        Returns:
            str: Описание действия
        """
        if character == self:
            return 'Ты не можешь атаковать сам себя'
        character.change_lives(-self.power)
        return f'Краснолюд {self.name} тупым тапором наносит урон {character.name} на {self.power}'

    def defend(self, character):
        """
        Защищается, нанося ответный урон.

        Args:
            character (Character): Цель защиты

        Returns:
            str: Описание действия
        """
        character.change_lives(-self.power // 4)
        return 'Лучшая защита - нападение'

    def __str__(self):
        """Возвращает строковое описание персонажа."""
        return f'Славный воин {self.name} обладает силой равной {self.power} и здоровьем {self.lives}'


class Mage(Character):
    """Класс персонажа-Маг."""

    def attack(self, character):
        """
        Атакует другого персонажа магией.

        Args:
            character (Character): Цель атаки

        Returns:
            str: Описание действия
        """
        if character == self:
            return 'Ты не можешь атаковать сам себя'
        character.change_lives(-self.power)
        return f'Маг {self.name} заколдованной руной наносит урон {character.name} на {self.power}'

    def defend(self, character=None):
        """
        Защищается, восстанавливая здоровье.

        Args:
            character (Character, optional): Не используется

        Returns:
            str: Описание действия
        """
        self.change_lives(25)
        return 'Осторожность никогда не бывает лишней'

    def __str__(self):
        """Возвращает строковое описание персонажа."""
        return f'Опытный маг {self.name} обладает силой равной {self.power} и здоровьем {self.lives}'


class Archer(Character):
    """Класс персонажа-Лучник."""

    def attack(self, character):
        """
        Атакует другого персонажа стрелой.

        Args:
            character (Character): Цель атаки

        Returns:
            str: Описание действия
        """
        if character == self:
            return 'Ты не можешь атаковать сам себя'
        character.change_lives(-self.power)
        return f'Эльф {self.name} меткой стрелой наносит урон {character.name} на {self.power}'

    def defend(self, character):
        """
        Защищается, нанося слабый урон и восстанавливая здоровье.

        Args:
            character (Character): Цель защиты

        Returns:
            str: Описание действия
        """
        character.change_lives(-self.power // 5)
        self.change_lives(5)
        return 'Всего понемногу'

    def __str__(self):
        """Возвращает строковое описание персонажа."""
        return f'Гордый эльф {self.name} обладает силой равной {self.power} и здоровьем {self.lives}'


class CharacterCreator(abc.ABC):
    """
    Абстрактная фабрика для создания персонажей.
    """

    @abc.abstractmethod
    def create_character(self) -> Character:
        """Создаёт персонажа."""
        pass


class WarriorCreator(CharacterCreator):
    """Фабрика для создания Воина."""

    def create_character(self, name, lives=100, power=20):
        """
        Создаёт персонажа-Воина.

        Args:
            name (str): Имя
            lives (int): Жизни
            power (int): Сила

        Returns:
            Warrior: Новый воин
        """
        return Warrior(name, lives, power)


class MageCreator(CharacterCreator):
    """Фабрика для создания Мага."""

    def create_character(self, name, lives=150, power=10):
        """
        Создаёт персонажа-Мага.

        Args:
            name (str): Имя
            lives (int): Жизни
            power (int): Сила

        Returns:
            Mage: Новый маг
        """
        return Mage(name, lives, power)


class ArcherCreator(CharacterCreator):
    """Фабрика для создания Лучника."""

    def create_character(self, name, lives=120, power=15):
        """
        Создаёт персонажа-Лучника.

        Args:
            name (str): Имя
            lives (int): Жизни
            power (int): Сила

        Returns:
            Archer: Новый лучник
        """
        return Archer(name, lives, power)


# Пример использования
character1 = WarriorCreator().create_character('Золтан')
character2 = MageCreator().create_character('Зельда')
character3 = ArcherCreator().create_character('Иорвет')

print(character1, character2, character3, sep='\n')
print(character1.attack(character2))
print(character2.lives)
print(character2.attack(character1))
print(character1.defend(character2))
print(character2.lives)
print(character1.lives)
print(character1.attack(character1))

# Дополнительные атаки
for _ in range(8):
    character1.attack(character2)