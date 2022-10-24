import pygame
import time
from threading import Thread

import levels as lvl
import viewport as vp
import player as pl
import userevents

class WorldManager:
    current_level_num = -1
    current_level = lvl.GameLevels.LEVELS[0]
    player = pl.Player(current_level.player_spawn_pos)
    LAVA_DROPLET_INTERVAL = 3
    can_spawn_lava_droplets = True

    def update():
        WorldManager.draw_level_tiles()
        WorldManager.player.update()
        WorldManager.spawn_lava_droplets()
        WorldManager.update_lava_droplets()
        WorldManager.update_coins()
        WorldManager.try_finish_level()
    
    def draw_level_tiles():
        for tile in WorldManager.current_level.tiles:
            pygame.draw.rect(vp.ViewPort.WINDOW, tile.COLOR, tile.COLLIDER)
    
    def spawn_lava_droplets():
        if (WorldManager.can_spawn_lava_droplets):
            for spawner in WorldManager.current_level.lava_droplet_spawners:
                spawner.spawn_droplet()
            WorldManager.can_spawn_lava_droplets = False
            thread = Thread(target = WorldManager.wait_for_next_droplets)
            thread.start()

    def wait_for_next_droplets():
        time.sleep(WorldManager.LAVA_DROPLET_INTERVAL)
        WorldManager.can_spawn_lava_droplets = True
    
    def update_lava_droplets():
        for droplet in WorldManager.current_level.lava_droplets:
            droplet.update()
    
    def reset_level():
        WorldManager.player.teleport(WorldManager.current_level.player_spawn_pos)
        WorldManager.reset_lava_droplets()
        WorldManager.current_level.reset_coins()
    
    def reset_lava_droplets():
        #WorldManager.can_spawn_lava_droplets = True
        while (len(WorldManager.current_level.lava_droplets) != 0):
            droplet = WorldManager.current_level.lava_droplets.pop()
            droplet.delete()
    
    def update_coins():
        for coin in WorldManager.current_level.coins:
            coin.update()
    
    def try_finish_level():
        if (len(WorldManager.current_level.coins) == 0):
            pygame.event.post(pygame.event.Event(userevents.UserEvents.FINISHED_LEVEL))
    
    def put_on_next_level():
        if (WorldManager.current_level_num != -1):
            WorldManager.current_level.disable()
        WorldManager.current_level_num += 1
        if (WorldManager.current_level_num >= len(lvl.GameLevels.LEVELS)):
            pygame.event.post(pygame.event.Event(userevents.UserEvents.END_GAME))
        else:
            WorldManager.current_level = lvl.GameLevels.LEVELS[WorldManager.current_level_num]
            WorldManager.current_level.enable()
            WorldManager.reset_level()
