from app.models import Board, InputBox


def main():
    board = Board()
    while True:
        board.game_loop()


if __name__ == '__main__':
    main()
