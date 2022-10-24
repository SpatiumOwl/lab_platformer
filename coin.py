import pygame

import viewport as vp

class Coin:
    COLOR = (255, 200, 20)
    
    def __init__(self, start_position, level):
        self.collider = pygame.rect.Rect(
            (start_position[0] + 0.125) * vp.ViewPort.TILE_SIZE[0], 
            (start_position[1] + 0.125) * vp.ViewPort.TILE_SIZE[1], 
            vp.ViewPort.TILE_SIZE[0] * 0.75, 
            vp.ViewPort.TILE_SIZE[1] * 0.75)
        self.level = level
    
    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.rect(vp.ViewPort.WINDOW, self.COLOR, self.collider)