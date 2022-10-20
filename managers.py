import pygame

import levels as lvl
import viewport as vp
import player as pl

class WorldManager:
    current_level = lvl.GameLevels.LEVEL_1
    player = pl.Player(current_level.player_spawn_pos)

    def draw_level_tiles():
        for tile in WorldManager.current_level.TILES:
            pygame.draw.rect(vp.ViewPort.WINDOW, tile.COLOR, tile.COLLIDER)
    
    def reset_level():
        WorldManager.player.teleport(WorldManager.current_level.player_spawn_pos)