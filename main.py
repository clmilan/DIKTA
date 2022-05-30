import pygame
import os
from buttons import *
from pygame import mixer

pygame.display.set_caption('BAWAL SA MGA BBM SUPPORTERS KATULAD NI DOC ******')


class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.width = 1360
        self.height = 765
        self.win = pygame.display.set_mode((self.width, self.height))
        self.buttons = []
        self.FPS = 60

        self.clicks = 0
        self.random_clicks = 0
        self.doneCliking = False

    def make_dialogue(self, count,  x, y, sayer='Joe'):
        DIALOUGE = [
            "I need to make sure that I didn’t forget anything before I go.", 'Hover over the items in your screen to perform an action on them. The cursor changes based on its location.']

        dialouge_font = pygame.font.SysFont('comicsans', 15)
        sayer_font = pygame.font.SysFont('comicsans', 17)

        dialogue_label = dialouge_font.render(
            DIALOUGE[count], 1, (255, 255, 255))

        sayer_label = sayer_font.render(
            sayer, 1, (255, 255, 255))

        self.win.blit(dialogue_label, (x, y))
        self.win.blit(sayer_label, (440, 25))

    def draw_window(self):

        curr_time = pygame.time.get_ticks()
        intro_done = True

        # INTRO IMAGES
        self.win.blit(pygame.transform.scale(pygame.image.load(os.path.join(
            'assets/e1m0_files', 'e1m0-intro-1.png')), (self.width, self.height)), (0, 0))

        if curr_time > 8000:

            self.win.blit(pygame.transform.scale(pygame.image.load(os.path.join(
                'assets/e1m0_files', 'e1m0-intro-2.png')), (self.width, self.height)), (0, 0))
            if curr_time > 15500:
                intro_done = True

        # DIALOGUE IMAGES
        if intro_done:
            self.win.blit(pygame.transform.scale(pygame.image.load(os.path.join(
                'assets/e1m1-main_files', 'e1m1-bg-main.png')), (self.width, self.height)), (0, 0))

            self.win.blit(pygame.transform.scale(pygame.image.load(os.path.join(
                'assets/e1m1-main_files', 'ui-dialogue-main.png')), (764, 80)), (280, 53))

            self.win.blit(pygame.transform.scale(pygame.image.load(os.path.join(
                'assets/e1m1-main_files', 'ui-dialogue-portrait-joe.png')), (115, 115)), (270, 30))

            self.win.blit(pygame.transform.scale(pygame.image.load(os.path.join(
                'assets/e1m1-main_files', 'ui-dialogue-namebox.png')), (124, 42)), (400, 20))

            self.make_dialogue(self.random_clicks,
                               400, 80)

            if self.clicks == 1:
                self.random_clicks = self.clicks
                self.make_dialogue(self.random_clicks,
                                   400, 80)
            if self.clicks == 2:

                JOURNAL = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-journal.png')), (126, 155))
                LETTERS = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-letters.png')), (273, 221))
                MAIL = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-mail.png')), (310, 394))
                PENCIL = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-pencils.png')), (102, 167))
                PRESS_CARD = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-press-card.png')), (87, 52))
                REPORTS = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-reports.png')), (332, 227))
                STAPLER = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-stapler.png')), (103, 64))
                TYPEWRITER = pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-item-typewriter.png')), (532, 545))

                JOURNAL_BUTTON = Buttons(1150, 600, JOURNAL, 'journal')
                LETTERS_BUTTON = Buttons(920, 360, LETTERS, 'letters')
                MAIL_BUTTON = Buttons(1049, 100, MAIL, 'mail')
                PENCIL_BUTTON = Buttons(1049, 100, PENCIL, 'pencil')
                PRESS_CARD_BUTTON = Buttons(30, 300, PRESS_CARD, 'press_card')
                REPORTS_BUTTON = Buttons(160, 130, REPORTS, 'reports')
                TYPEWRITER_BUTTON = Buttons(400, 20, TYPEWRITER, 'type_writer')
                STAPLER_BUTTON = Buttons(265, 20, STAPLER, 'stapler')

                self.buttons = [JOURNAL_BUTTON, MAIL_BUTTON,
                                LETTERS_BUTTON, PRESS_CARD_BUTTON, REPORTS_BUTTON, TYPEWRITER_BUTTON, STAPLER_BUTTON]
                self.win.blit(pygame.transform.scale(pygame.image.load(os.path.join(
                    'assets/e1m1-desk_files', 'e1m1-bg-desk.png')), (self.width, self.height)), (0, 0))
                for items in self.buttons:
                    items.draw_window(self.win)

        pygame.display.update()

    def run(self):
        player = Player()
        clock = pygame.time.Clock()
        clock.tick(self.FPS)
        # mixer.music.load(os.path.join('music', 'e1_main_intro.mp3'))
        # mixer.music.play()

        running = True
        clicked = False

        while running:

            self.draw_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if not self.doneCliking:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.clicks += 1

                        if self.clicks == 2:
                            self.doneCliking = True

                if event.type == pygame.MOUSEBUTTONDOWN:

                    pos = pygame.mouse.get_pos()
                    for items in self.buttons:
                        if items.clicked == False:

                            items.checkClick(pos)
                            items.clicked = True


class Player():
    def __init__(self):

        self.isClicked = False
        self.img = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/player', 'point.png')), (128, 128))
        self.mask = pygame.mask.from_surface(self.img)

    def draw_window(self, window):
        window.blit(self.img, ())

    def clicks(self):

        self.isClicked = True


game = Game()

game.run()
