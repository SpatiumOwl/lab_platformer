import pygame

import levels as lvl
import viewport as vp

class WorldManager:
    current_level = lvl.GameLevels.LEVEL_1

    def draw_level_tiles():
        for tile in WorldManager.current_level.TILES:
            pygame.draw.rect(vp.ViewPort.WINDOW, tile.COLOR, tile.COLLIDER)