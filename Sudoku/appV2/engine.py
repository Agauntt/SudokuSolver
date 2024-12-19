import os, sys
import requests
from pprint import pprint


class Engine:

    def __init__(self):
        pass


    def get_starting_board(self):
        req = requests.get("https://sudoku-api.vercel.app/api/dosuku")
        res_raw = req.json()
        res = res_raw['newboard']['grids'][0]
        return  res['value'], res['solution']
    


    def is_game_over(self):
        pass


    def check_for_mistake(self, guess, x, y, solution):
        pprint(solution)
        pprint(guess)
        if solution[y][x] == int(guess):
            return True
        return False


    def check_vertical(self):
        pass


    def check_horizontal(self):
        pass


    def check_square(self):
        pass