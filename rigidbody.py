import math
import pygame

import physics
import viewport as vp

class RigidBody:
    rb_list = []
    
    def __init__(self, collider, stationary):
        self.collider = collider
        self.velocity = (0, 0)
        self.stationary = stationary
        RigidBody.rb_list.append(self)
    
    def delete(self):
        RigidBody.rb_list.remove(self)
    
    def add_velocity(self, vector2):
        self.velocity = (self.velocity[0] + vector2[0], self.velocity[1] + vector2[1])

    def reset_velocity(self):
        self.reset_velocity_x()
        self.reset_velocity_y()
    
    def reset_velocity_x(self):
        self.velocity = (0, self.velocity[1])

    def reset_velocity_y(self):
        self.velocity = (self.velocity[0], 0)
    
    def lerp(self, multiplier, vector2):
        self.velocity = (
            self.velocity[0] + (vector2[0] - self.velocity[0]) * multiplier,
            self.velocity[1] + (vector2[1] - self.velocity[1]) * multiplier
        )

    def apply_air_friction(self):
        self.velocity = (
            self.velocity[0] * (1 - physics.PhysicsData.AIR_FRICTION * vp.ViewPort.delta_time), 
            self.velocity[1] * (1 - physics.PhysicsData.AIR_FRICTION * vp.ViewPort.delta_time)
            )
    
    def update(self):
        if (not self.stationary):
            self.add_velocity((0, physics.PhysicsData.FREEFALL_ACCELERATION * vp.ViewPort.delta_time))           
            self.apply_air_friction()

            next_position_collider_full = pygame.Rect(self.collider)
            next_position_collider_full.x += self.velocity[0] * vp.ViewPort.TILE_SIZE[0]
            next_position_collider_full.y += self.velocity[1] * vp.ViewPort.TILE_SIZE[1]

            next_position_collider_horizontal = pygame.Rect(self.collider)
            next_position_collider_horizontal.x += self.velocity[0] * vp.ViewPort.TILE_SIZE[0]
            
            next_position_collider_vertical = pygame.Rect(self.collider)
            next_position_collider_vertical.y += self.velocity[1] * vp.ViewPort.TILE_SIZE[1]
            
            can_move_fully = True
            can_move_horizontally = True
            can_move_vertically = True

            for rb in RigidBody.rb_list:
                if (rb is not self):
                    if rb.collider.colliderect(next_position_collider_full):
                        can_move_fully = False
                    if rb.collider.colliderect(next_position_collider_horizontal):
                        can_move_horizontally = False
                    if rb.collider.colliderect(next_position_collider_vertical):
                        can_move_vertically = False
                    
                    if (not can_move_fully and not can_move_horizontally and not can_move_vertically):
                        break
            if (can_move_fully):
                self.collider.x += RigidBody.absolute_trunc(self.velocity[0] * vp.ViewPort.TILE_SIZE[0])
                self.collider.y += RigidBody.absolute_trunc(self.velocity[1] * vp.ViewPort.TILE_SIZE[1])
            else:
                if (can_move_horizontally):
                    self.collider.x += RigidBody.absolute_trunc(self.velocity[0] * vp.ViewPort.TILE_SIZE[0])
                else:
                    self.reset_velocity_x()

                if (can_move_vertically):
                    self.collider.y += RigidBody.absolute_trunc(self.velocity[1] * vp.ViewPort.TILE_SIZE[1])
                else:
                    self.reset_velocity_y()

    def absolute_trunc(num):
        if (num >= 0):
            return math.trunc(num)
        else:
            return -math.trunc(-num)

            
