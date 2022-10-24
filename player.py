import pygame

import viewport as vp
import rigidbody as rb
import managers as mgr
import levels as lvl
import tile
import userevents

class Player:
    KEY_LEFT = pygame.K_a
    KEY_RIGHT = pygame.K_d
    KEY_JUMP = pygame.K_SPACE

    RUN_SPEED = 0.04
    JUMP_FORCE = 0.18
    
    COLOR = (150, 150, 150)

    GROUND_COLLIDER_OFFSET = (2, vp.ViewPort.TILE_SIZE[1]*2)
    
    def __init__(self, start_position):
        self.collider = pygame.rect.Rect(
            start_position[0] * vp.ViewPort.TILE_SIZE[0], 
            start_position[1] * vp.ViewPort.TILE_SIZE[1], 
            vp.ViewPort.TILE_SIZE[0], 
            vp.ViewPort.TILE_SIZE[1] * 2)
        self.ground_collider = pygame.rect.Rect(
            start_position[0] * vp.ViewPort.TILE_SIZE[0] + Player.GROUND_COLLIDER_OFFSET[0], 
            start_position[1] * vp.ViewPort.TILE_SIZE[1] + Player.GROUND_COLLIDER_OFFSET[1], 
            vp.ViewPort.TILE_SIZE[0] - 4, 
            1)
        self.rigidbody = rb.RigidBody(self.collider, False)

    def update(self):
        self.rigidbody.update()
        self.sync_ground_collider()    
        self.control_player()    
        self.draw_player()
        self.collide_with_lava()
        self.collide_with_lava_droplet()
        self.collect_coin()

    def sync_ground_collider(self):
        self.ground_collider.x = self.collider.x + Player.GROUND_COLLIDER_OFFSET[0]
        self.ground_collider.y = self.collider.y + Player.GROUND_COLLIDER_OFFSET[1]

    def control_player(self):
        keys_pressed = pygame.key.get_pressed()

        target_velocity = self.rigidbody.velocity
        if (keys_pressed[Player.KEY_LEFT]):
            target_velocity = (-self.RUN_SPEED, target_velocity[1])
        
        if (keys_pressed[Player.KEY_RIGHT]):
            target_velocity = (self.RUN_SPEED, target_velocity[1])

        if (not keys_pressed[Player.KEY_RIGHT] and not keys_pressed[Player.KEY_LEFT]):
            target_velocity = (0, target_velocity[1])

        self.rigidbody.lerp(0.7, target_velocity)

        if (Player.KEY_JUMP in vp.ViewPort.key_down and self.touching_ground()):
            self.rigidbody.reset_velocity_y()
            self.rigidbody.add_velocity((0, -Player.JUMP_FORCE))            
    
    def touching_ground(self):
        for rigidbody in rb.RigidBody.rb_list:
            if (self.ground_collider.colliderect(rigidbody.collider)):
                return True
        return False

    def draw_player(self):
        pygame.draw.rect(vp.ViewPort.WINDOW, self.COLOR, self.collider)
    
    def collide_with_lava(self):
        for current_tile in mgr.WorldManager.current_level.tiles:
            if (current_tile.TILE_TYPE == tile.TileType.LAVA):
                if (self.collider.colliderect(current_tile.COLLIDER)):
                    pygame.event.post(pygame.event.Event(userevents.UserEvents.PLAYER_DEAD))

    def collide_with_lava_droplet(self):
        for droplet in mgr.WorldManager.current_level.lava_droplets:
            if (self.collider.colliderect(droplet.burn_collider)):
                pygame.event.post(pygame.event.Event(userevents.UserEvents.PLAYER_DEAD))

    def collect_coin(self):
        collected_coin = -1
        for coin in mgr.WorldManager.current_level.coins:
            if (self.collider.colliderect(coin.collider)):
                collected_coin = coin
        if (collected_coin != -1):
            pygame.event.post(pygame.event.Event(userevents.UserEvents.COLLECTED_COIN))
            mgr.WorldManager.current_level.coins.remove(collected_coin)


    def teleport(self, position):
        self.collider.x = position[0] * vp.ViewPort.TILE_SIZE[0]
        self.collider.y = position[1] * vp.ViewPort.TILE_SIZE[1]
        self.rigidbody.reset_velocity()
