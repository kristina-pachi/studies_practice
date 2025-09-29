# 1 Лабораторная. 2 Задание : Система создания персонажей для игры
import abc
from typing import Optional


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

    def __init__(self, name: str, lives: int, power: int) -> None:
        """Инициализирует базовые параметры персонажа."""

        self.__name = name
        self.__lives = lives
        self.__power = power

    @abc.abstractmethod
    def attack(self, character: 'Character') -> str:
        """Абстрактный метод атаки."""

        pass

    @abc.abstractmethod
    def defend(self, character: Optional['Character'] = None) -> str:
        """Абстрактный метод защиты."""

        pass

    @property
    def name(self) -> str:
        """Возвращает имя персонажа."""

        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Устанавливает новое имя персонажа."""

        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
            print(f"Имя персонажа изменено на: {self.__name}")
        else:
            print("Имя персонажа должно быть непустой строкой.")

    @property
    def lives(self) -> int:
        """Возвращает текущее количество жизней."""

        return self.__lives

    @lives.setter
    def lives(self, value: int) -> None:
        """Устанавливает новое значение жизней."""

        self.__lives = value

    def change_lives(self, delta: int) -> bool:
        """Изменяет количество жизней персонажа."""

        if self.__lives <= 0:
            print(f"{self.__name} уже в другом мире... :(")
            return True
        self.__lives += delta
        return False

    @property
    def power(self) -> int:
        """Возвращает силу персонажа."""

        return self.__power

    @power.setter
    def power(self, value: int) -> None:
        """Увеличивает силу персонажа."""

        self.__power += value


class Warrior(Character):
    """Класс персонажа-Воин."""

    def attack(self, character: Character) -> str:
        """Атакует другого персонажа."""

        if character is self:
            return "Ты не можешь атаковать сам себя"
        character.change_lives(-self.power)
        return f"Краснолюд {self.name} тупым тапором наносит урон {character.name} на {self.power}"

    def defend(self, character: Character) -> str:
        """Защищается, нанося ответный урон."""

        character.change_lives(-self.power // 4)
        return "Лучшая защита - нападение"

    def __str__(self) -> str:
        """Возвращает строковое описание персонажа."""

        return f"Славный воин {self.name} обладает силой равной {self.power} и здоровьем {self.lives}"


class Mage(Character):
    """Класс персонажа-Маг."""

    def attack(self, character: Character) -> str:
        """Атакует другого персонажа магией."""

        if character is self:
            return "Ты не можешь атаковать сам себя"
        character.change_lives(-self.power)
        return f"Маг {self.name} заколдованной руной наносит урон {character.name} на {self.power}"

    def defend(self, character: Optional[Character] = None) -> str:
        """Защищается, восстанавливая здоровье."""

        self.change_lives(25)
        return "Осторожность никогда не бывает лишней"

    def __str__(self) -> str:
        """Возвращает строковое описание персонажа."""

        return f"Опытный маг {self.name} обладает силой равной {self.power} и здоровьем {self.lives}"


class Archer(Character):
    """Класс персонажа-Лучник."""

    def attack(self, character: Character) -> str:
        """Атакует другого персонажа стрелой."""

        if character is self:
            return "Ты не можешь атаковать сам себя"
        character.change_lives(-self.power)
        return f"Эльф {self.name} меткой стрелой наносит урон {character.name} на {self.power}"

    def defend(self, character: Character) -> str:
        """Защищается, нанося слабый урон и восстанавливая здоровье."""

        character.change_lives(-self.power // 5)
        self.change_lives(5)
        return "Всего понемногу"

    def __str__(self) -> str:
        """Возвращает строковое описание персонажа."""

        return f"Гордый эльф {self.name} обладает силой равной {self.power} и здоровьем {self.lives}"


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

    def create_character(self, name: str, lives: int = 100, power: int = 20) -> Warrior:
        """Создаёт персонажа-Воина."""

        return Warrior(name, lives, power)


class MageCreator(CharacterCreator):
    """Фабрика для создания Мага."""

    def create_character(self, name: str, lives: int = 150, power: int = 10) -> Mage:
        """Создаёт персонажа-Мага."""

        return Mage(name, lives, power)


class ArcherCreator(CharacterCreator):
    """Фабрика для создания Лучника."""

    def create_character(self, name: str, lives: int = 120, power: int = 15) -> Archer:
        """Создаёт персонажа-Лучника."""

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