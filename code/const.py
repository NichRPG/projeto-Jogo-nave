import pygame

# C
COLOR_BLUE = (0, 0, 150)
COLOR_PURPLE = (100, 0, 100)
COLOR_RED = (150, 0, 0)
COLOR_WHITE = (255, 255, 255)
# E
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player2': 3,
                'Enimy1': 2,
                'Enimy2': 1
                }
EVENT_ENIMY = pygame.USEREVENT + 1
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
