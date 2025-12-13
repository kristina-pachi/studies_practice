# 7 Лабораторная.
# 3  Сохранение состояния игры.

import pickle
import random



class Game():
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.level = 0
        self.filename = 'game_data.pkl'
    
    def play(self):
        nums = [random.randint(1, 100) for _ in range(3)]
        choice = random.choice(nums)
        print('Угадай число:', *nums, sep='\n')
        player_choice = int(input("Введи число: "))
        if player_choice == choice:
            print('Поздравляю, ты угадал!')
            self.score += 1
            if self.score == 10:
                self.level += 1
                self.score = 0
        else:
            print('Промах, попробуй ёще раз')


    def save_game(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self, f)


    @staticmethod
    def load_game(filename='game_data.pkl'):
        with open(filename, 'rb') as f:
            return pickle.load(f)

    
    def __str__(self):
        return f'Игрок {self.player_name} заработал {self.score} очков и имеет уровень {self.level}'


player = Game('@user345')

player.play()
player.save_game()

loaded_game = Game.load_game()
print(loaded_game)
