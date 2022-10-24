import pygame

class UserEvents:
    PLAYER_DEAD = pygame.USEREVENT + 1
    COLLECTED_COIN = pygame.USEREVENT + 2
    FINISHED_LEVEL = pygame.USEREVENT + 3
    END_GAME = pygame.USEREVENT + 4