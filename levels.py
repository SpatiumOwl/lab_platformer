from enum import Enum
import pygame

import viewport as vp
import rigidbody as rb

class TileType(Enum):
    SKY = 0
    FLOOR = 1
    LAVA = 2

class Tile:
    DEFAULT_COLORS = [
        (50, 100, 255),     #Sky
        (255, 255, 255),    #Floor
        (150, 20, 20)       #Lava
    ]
    
    def __init__(self, tile_type : TileType, position_units : int):
        self.TILE_TYPE = tile_type
        self.COLLIDER = pygame.Rect(
            position_units[0] * vp.ViewPort.TILE_SIZE[0],
            position_units[1] * vp.ViewPort.TILE_SIZE[1],
            vp.ViewPort.TILE_SIZE[0],
            vp.ViewPort.TILE_SIZE[1],
        )
        self.set_color()
        self.enable_physics()
    
    def set_color(self):
        if (self.TILE_TYPE == TileType.SKY):
            self.COLOR = self.DEFAULT_COLORS[0]
        elif (self.TILE_TYPE == TileType.FLOOR):
            self.COLOR = self.DEFAULT_COLORS[1]
        elif (self.TILE_TYPE == TileType.LAVA):
            self.COLOR = self.DEFAULT_COLORS[2]

    def enable_physics(self):
        if (self.TILE_TYPE == TileType.FLOOR):
            self.rigidbody = rb.RigidBody(self.COLLIDER, True)

class Level:
    TILES_TEXT = []
    TILES = []

    def __init__(self, tiles_text : str):
        self.TILES_TEXT = tiles_text
        self.create_tiles()

    def create_tiles(self):
        for i in range(len(self.TILES_TEXT)):
            for j in range(len(self.TILES_TEXT[0])):
                if (self.TILES_TEXT[i][j] == "X"):
                    tile_type = TileType.SKY
                elif (self.TILES_TEXT[i][j] == "F"):
                    tile_type = TileType.FLOOR
                elif (self.TILES_TEXT[i][j] == "L"):
                    tile_type = TileType.LAVA
                self.TILES.append(Tile(tile_type, [j, i]))
    
class GameLevels:   
    LEVEL_1 = Level([
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXFFFFFFXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXFFFFFFXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXFFFFFFFFFFFF",
        "FFFFXXXXXXXXXXXXXXXXXXXXX",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL"
    ])  



