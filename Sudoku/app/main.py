import pandas as pd
import numpy as np

from app.models import Board


def main():
    board = Board()
    while True:
        board.game_loop()


if __name__ == '__main__':
    main()
