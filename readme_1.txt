# RPG Character System

Проект на Python, реализующий систему персонажей для текстовой RPG-игры. Используются принципы ООП: абстракция, наследование, инкапсуляция и фабричный паттерн.

## 📦 Структура

- `Character` — абстрактный базовый класс персонажа
- `Warrior`, `Mage`, `Archer` — конкретные классы персонажей с уникальной логикой атаки и защиты
- `CharacterCreator` — абстрактная фабрика
- `WarriorCreator`, `MageCreator`, `ArcherCreator` — фабрики для создания персонажей

## 🚀 Пример использования

```python
character1 = WarriorCreator().create_character('Золтан')
character2 = MageCreator().create_character('Зельда')

print(character1.attack(character2))
print(character2.defend())

## Особенности
- Защита от самоуничтожения (attack(self) проверяет, чтобы персонаж не атаковал сам себя)
- Метод change_lives(delta) контролирует изменение жизней и смерть персонажа
- У каждого класса есть __str__, чтобы красиво выводить информацию
