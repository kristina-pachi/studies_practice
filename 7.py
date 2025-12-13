# 7 Лабораторная.
# 3  Сохранение состояния игры.

import pickle
import random
import os

class Game:
    def __init__(self, player_name, filename='game_data.pkl'):
        self.player_name = player_name
        self.score = 0
        self.level = 0
        self.filename = filename
    
    def play(self):
        nums = [random.randint(1, 100) for _ in range(3)]
        choice = random.choice(nums)
        print('Угадай число:', *nums, sep='\n')
        player_choice = int(input("Введи число: "))
        if player_choice == choice:
            print('Поздравляю, ты угадал!')
            self.score += 1
            if self.score == 3:
                self.level += 1
                self.score = 0
        else:
            print('Промах, попробуй ещё раз')
    
    def save_game(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load_game(filename='game_data.pkl'):
        if not os.path.exists(filename):
            print("Нет сохранённой игры.")
            return None
        with open(filename, 'rb') as f:
            return pickle.load(f)
    
    def __str__(self):
        return f'Игрок {self.player_name} заработал {self.score} очков и имеет уровень {self.level}'


# разделение на новою игру и загрузку сохранений
if os.path.exists("game_data.pkl"):
    player = Game.load_game()
    print("Загружена сохранённая игра:")
    print(player)
else:
    player = Game('@user345')
    print("Начата новая игра.")

player.play()
player.save_game()

loaded_game = Game.load_game()
if loaded_game:
    print("Состояние после сохранения и загрузки:")
    print(loaded_game)
