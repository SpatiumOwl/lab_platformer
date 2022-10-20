import pygame

import viewport as vp
import rigidbody as rb

class Player:
    KEY_LEFT = pygame.K_a
    KEY_RIGHT = pygame.K_d
    KEY_JUMP = pygame.K_SPACE

    RUN_SPEED = 0.04
    JUMP_FORCE = 0.2
    
    COLOR = (150, 150, 150)
    
    def __init__(self, start_position):
        self.collider = pygame.rect.Rect(
            start_position[0] * vp.ViewPort.TILE_SIZE[0], 
            start_position[1] * vp.ViewPort.TILE_SIZE[1], 
            vp.ViewPort.TILE_SIZE[0], 
            vp.ViewPort.TILE_SIZE[1] * 2)
        self.rigidbody = rb.RigidBody(self.collider, False)

    def update(self):
        self.rigidbody.update()    
        self.control_player()    
        self.draw_player()

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

        if (Player.KEY_JUMP in vp.ViewPort.key_down):
            self.rigidbody.reset_velocity_y()
            self.rigidbody.add_velocity((0, -Player.JUMP_FORCE))
            

    
    def draw_player(self):
        pygame.draw.rect(vp.ViewPort.WINDOW, self.COLOR, self.collider)
