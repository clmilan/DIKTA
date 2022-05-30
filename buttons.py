from buttons import *
from pygame import mixer
import time
import os
import pygame


class Buttons():
    def __init__(self, x, y, img, name):
        self.x = x
        self.y = y
        self.img = img
        self.rect = self.img.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.img)
        self.name = name
        self.clicked = False

    def draw_window(self, window):
        window.blit(self.img, (self.x, self.y))

    def checkClick(self, pos):

        print(pos)
        if self.rect.collidepoint(pos):
            print(f"clicked {self.name}")
            self.clicked = True

# class Menu(Game):
#     def __init__(self):
#         super().__init__()
#         self.click = None
#         self.menu_state = 'main_menu'
#         self.player = Player()

#     def decide_option(self):
#         if self.menu_state == 'main_menu':
#             self.main_menu()
#         if self.menu_state == 'new_game':
#             self.new_game()
#         if self.menu_state == 'exit_game':
#             self.exit_game()

#     def main_menu(self):

#         # BLITTING THE MAIN MENU BG
#         MAIN_MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join(
#             'assets/e0m0_files', 'e0m0-bg-main.png')), (self.width, self.height))
#         self.win.blit(MAIN_MENU_BG, (0, 0))

#         NEW_GAME = pygame.transform.scale(pygame.image.load(os.path.join(
#             'assets/e0m0_files', 'btn-new.png')), (73, 80))

#         NEW_GAME_BUTTON = Buttons(480, 660, NEW_GAME, 'new_game')

#         self.buttons = [NEW_GAME_BUTTON]

#         # WILL BLIT THE BUTTONS

#         for items in self.buttons:
#             items.draw_window(self.win)

#         pygame.display.update()

#     def new_game(self):
#         pass

#     def exit_game(self):
#         pass
