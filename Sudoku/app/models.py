import sys, pygame as pg

pg.init()
WIN_SIZE = 750, 750
SCREEN = pg.display.set_mode(WIN_SIZE)
font = pg.font.SysFont(None, 80)

#Title and Icon
pg.display.set_caption("Sudoku solver using backtracking")


number_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class Board:

    # def __init__(self):
    #     pass

    def game_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        self.draw_bg()
        self.draw_nbrs()
        pg.display.flip()

    
    def draw_bg(self):
        SCREEN.fill(pg.Color("white"))
        pg.draw.rect(SCREEN, pg.Color("black"), pg.Rect(15, 15, 720, 720), 5)
        i = 1
        while (i * 80) < 720:
            line_width = 5 if i % 3 > 0 else 10
            pg.draw.line(SCREEN, pg.Color("black"), pg.Vector2((i * 80) + 15, 15), pg.Vector2((i * 80) + 15, 735), line_width)
            pg.draw.line(SCREEN, pg.Color("black"), pg.Vector2(15, (i * 80) + 15), pg.Vector2(735, (i * 80) + 15), line_width)
            i += 1

    
    def draw_nbrs(self):
        row = 0
        offset = 36
        while row < 9:
            col = 0
            while col < 9:
                output = number_grid[row][col]
                # print(str(output))
                n_text = font.render(str(output), True, pg.Color("black"))
                SCREEN.blit(n_text, pg.Vector2((col * 80) + offset + 3, (row * 80) + offset - 3))
                col += 1
            row += 1


# board = Board()
# while True:
#     board.game_loop()

    