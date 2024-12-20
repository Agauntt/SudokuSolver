import os, sys
import requests
from pprint import pprint


def get_starting_board():
    req = requests.get("https://sudoku-api.vercel.app/api/dosuku")
    res_raw = req.json()
    # print(res_raw)
    res = res_raw['newboard']['grids'][0]
    return  res['value'], res['solution']



def is_game_over(board, solution):
    return True if board == solution else False
    


def check_for_mistake(guess, x, y, solution):
    if solution[y][x] == int(guess):
        return True
    return False


def check_vertical(self):
    pass


def check_horizontal(self):
    pass


def check_square(self):
    pass