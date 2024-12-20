import sys, os
import pygame as pg
import pygame_gui as pgui

from pygame.math import Vector2 as vec2
from pprint import pprint
from .engine import get_starting_board, is_game_over, check_for_mistake




pg.init()
WIN_SIZE = 750, 750
CELL_SIZE = WIN_SIZE[0] // 9
INPUT_SIZE = 200, 200
SCREEN = pg.display.set_mode(WIN_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MANAGER = pgui.UIManager((INPUT_SIZE))
font = pg.font.SysFont(None, 80)

#Title and Icon
pg.display.set_caption("Sudoku solver using backtracking")


class InputBox:
    
    font = pg.font.Font(None, 32)

    def __init__(self, x, y, color='black'):
        self.input = '0'
        # self.rect = pg.Rect(150, 150, 140, 32)
        # self.active = False


    def display(self):
        print("Before while loop")
        while 1==1:
            for event in pg.event.get():
                if event.type == pg.KEYUP and event.key == pg.K_BACKSPACE:
                    self.input = '0'
                elif event.type == pg.KEYUP:
                    self.input = event.unicode
                    # print(self.input)
            if self.input != '0':
                break
        SCREEN.fill(BLACK)
        input_surface = font.render(str(self.input), True, WHITE)
        SCREEN.blit(input_surface, (20, 30))
        print("EXITING DISPLAY LOOP")
        return self.input


class Board:

    def __init__(self):
        self.number_grid, self.solution = get_starting_board()
        pprint(self.solution)

    def game_loop(self):
        # self.cheat_test()
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                coords_raw = vec2(pg.mouse.get_pos()) // CELL_SIZE
                x, y = (int(coords_raw[0])), int(coords_raw[1])
                self.handle_click(x, y)
            if event.type == pg.QUIT: sys.exit()
        if is_game_over(self.number_grid, self.solution):
            print("GAME COMPLETE")
            sys.exit() 
        self.draw_bg()
        self.draw_nbrs()
        pg.display.flip()


    def draw_bg(self):
        SCREEN.fill(pg.Color("white"))
        pg.draw.rect(SCREEN, pg.Color("black"), pg.Rect(15, 15, 720, 720), 5)
        i = 1
        while (i * 80) < 720:
            line_width = 5 if i % 3 > 0 else 10
            pg.draw.line(SCREEN, pg.Color("black"), 
                      pg.Vector2((i * 80) + 15, 15),
                      pg.Vector2((i * 80) + 15, 735), line_width)
            pg.draw.line(SCREEN, pg.Color("black"), 
                         pg.Vector2(15, (i * 80) + 15), 
                         pg.Vector2(735, (i * 80) + 15), line_width)
            i += 1

    
    def draw_nbrs(self):
        row = 0
        offset = 36
        while row < 9:
            col = 0
            while col < 9:
                output = self.number_grid[row][col]
                if output != 0:  
                    n_text = font.render(str(output), True, pg.Color("black"))
                    SCREEN.blit(n_text, pg.Vector2((col * 80) + offset + 3, (row * 80) + offset - 3))
                col += 1
            row += 1


    def handle_click(self, x, y):
        input = InputBox(x, y).display()
        if check_for_mistake(input, x, y, self.solution):
            self.number_grid[y][x] = input
        else:
            self.number_grid[y][x] = '0'


    # def make_note(self, x, y):
    #     note = self.number_grid[y][x]
    #     n_text = font.render(str(note), True, pg.Color("green"))
    #     SCREEN.blit(n_text)

    def cheat_test(self):
        for x, y in enumerate(self.solution):
            for i in y:
                j = y.index(i)
                self.number_grid[x][j] = self.solution[x][j]



   