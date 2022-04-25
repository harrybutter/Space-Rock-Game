import pygame as pg
from utils import load_sprite

class SpaceRocks:
    def __init__(self):
        self._init_pygame()
        self.screen = pg.display.set_mode((800,600))
        self.background = load_sprite("space", False)

    def main_loop(self):
        while True: #if a function is not rly in the game but for the bg settings of the game, "_" is usually placed at the front of the function
                    #if a function is very important and well known(?), "__" is inserted
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pg.init() #every function that uses pygame shld have pygame.init() in front
        pg.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        pass

    def _draw(self):
        #whenever somehting happens, this function will be called to display any changes on the screen
        self.screen.blit(self.background, (0,0)) #put the bg image over the window, not into the window, 
                                                #starting from left bottom corner
        pg.display.flip() #.flip resets to the original contents




