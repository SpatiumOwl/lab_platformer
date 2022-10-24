import pygame

import rigidbody as rb
import tile as tl
import viewport as vp

class LavaDroplet:
    COLOR = (150, 20, 20)
    
    def __init__(self, start_position, level):
        self.collider = pygame.rect.Rect(
            (start_position[0] + 0.125) * vp.ViewPort.TILE_SIZE[0], 
            (start_position[1] + 0.125) * vp.ViewPort.TILE_SIZE[1], 
            vp.ViewPort.TILE_SIZE[0] * 0.75, 
            vp.ViewPort.TILE_SIZE[1] * 0.75)
        self.ground_collider = pygame.rect.Rect(
            self.collider.x, self.collider.y + self.collider.height, self.collider.width, 1)
        self.burn_collider = pygame.rect.Rect(
            self.collider.x - 0.125 * vp.ViewPort.TILE_SIZE[0], 
            self.collider.y - 0.125 * vp.ViewPort.TILE_SIZE[1], 
            vp.ViewPort.TILE_SIZE[0], 
            vp.ViewPort.TILE_SIZE[1])
        self.rigidbody = rb.RigidBody(self.collider, False)
        self.level = level
    
    def delete(self):
        self.rigidbody.delete()
    
    def update(self):
        self.rigidbody.update()
        self.sync_ground_collider()
        self.sync_burn_collider()
        self.draw()
        self.try_hit_floor()

    def draw(self):
        pygame.draw.rect(vp.ViewPort.WINDOW, self.COLOR, self.collider)
    
    def try_hit_floor(self):
        if (self.touches_floor()):
            self.level.lava_droplets.remove(self)
            self.delete()
    
    def touches_floor(self):
        for tile in self.level.tiles:
            if (tile.TILE_TYPE != tl.TileType.SKY and self.ground_collider.colliderect(tile.COLLIDER)):
                return True
        return False
    
    def sync_ground_collider(self):
        self.ground_collider.x = self.collider.x 
        self.ground_collider.y = self.collider.y + self.collider.height
    
    def sync_burn_collider(self):
        self.burn_collider.x = self.collider.x - 0.125 * vp.ViewPort.TILE_SIZE[0]
        self.burn_collider.y = self.collider.y - 0.125 * vp.ViewPort.TILE_SIZE[1]