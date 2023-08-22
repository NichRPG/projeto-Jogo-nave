#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame.image
from pygame import Surface, rect
from pygame.font import Font
from code.const import WIN_WIDTH, COLOR_BLUE, COLOR_RED, MENU_OPTION, COLOR_WHITE, COLOR_PURPLE


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('../Asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('../Asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0

        while True:
            #  desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Montain', COLOR_BLUE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLOR_RED, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_PURPLE, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # testar se alguma tecla foi pressionada
                    if event.key == pygame.K_DOWN:  # testa se a tecla pressionada foi seta para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # testa se a tecla pressionada foi seta para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
