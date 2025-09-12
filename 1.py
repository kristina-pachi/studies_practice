import abc


class Character(abc.ABC):

    def __init__(self, name, lives, power):
        self.__name = name
        self.__lives = lives
        self.__power = power

    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def defend(self):
        pass
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
            print(f"Имя персонажа изменено на: {self.__name}")
        else:
            print("Имя персонажа должно быть непустой строкой.")

    @property
    def lives(self):
        return self.__lives
    
    @lives.setter
    def lives(self, value):
        self.__lives = value
    
    def change_lives(self, delta):
        if self.__lives <= 0:
            print(f'{self.__name} уже в другом мир... :(')
            return self.__lives == 0
        self.__lives += delta

    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, value):
        self.__power += value


class Warrior(Character):

    def attack(self, character):
        if character == self:
            return f'Ты не можешь аттаковать сам себя' 
        character.change_lives(-self.power)
        return f'Краснолюд {self.name} тупым тапором наносит урон {character.name} на {self.power}'
    
    def defend(self, character):
        character.change_lives(-self.power//4)
        return f'Лучшая защита - нападение'
    
    def __str__(self):
        return f'Славный воин {self.name} обладает силой равной {self.power} и здоровьем {self.lives}'

class Mage(Character):

    def attack(self, character):
        if character == self:
            return f'Ты не можешь аттаковать сам себя' 
        character.change_lives(-self.power)
        return f'маг {self.name} заколдованной руной наносит урон {character.name} на {self.power}'
    
    def defend(self, character=None):
        self.change_lives(25)
        return f'Осторожность никогда не бывает лишней'

    def __str__(self):
        return f'Опытный маг {self.name} обладает силой равной {self.power} и здоровьем {self.lives}'


class Archer(Character):

    def attack(self, character):
        if character == self:
            return f'Ты не можешь аттаковать сам себя' 
        character.change_lives(-self.power)
        return f'Эльф {self.name} меткой стрелой наносит урон {character.name} на {self.power}'
    
    def defend(self, character):
        character.change_lives(-self.power//5)
        self.change_lives(5)
        return f'Всего понемногу'

    def __str__(self):
        return f'Гордый эльф {self.name} обладает силой равной {self.power} и здоровьем {self.lives}'


class CharacterCreator(abc.ABC):

    @abc.abstractmethod
    def create_character(self) -> Character:
        pass


class WarriorCreator(CharacterCreator):
    def create_character(self, name, lives=100, power=20):
        return Warrior(name, lives, power)


class MageCreator(CharacterCreator):
    def create_character(self, name, lives=150, power=10):
        return Mage(name, lives, power)


class ArcherCreator(CharacterCreator):
    def create_character(self, name, lives=120, power=15):
        return Archer(name, lives, power)
    

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
character1.attack(character2)
character1.attack(character2)
character1.attack(character2)
character1.attack(character2)
character1.attack(character2)
character1.attack(character2)
character1.attack(character2)
character1.attack(character2)
