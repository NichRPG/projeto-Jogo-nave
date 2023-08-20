#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame as pygame
from pygame import Surface, rect
from pygame.font import Font

from code.Menu import Menu
from code.const import WIN_WEIGHT, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WEIGHT, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass
