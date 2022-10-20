import tile

class Level:
    TILES_TEXT = []
    TILES = []

    def __init__(self, tiles_text : str, player_spawn_pos):
        self.TILES_TEXT = tiles_text
        self.player_spawn_pos = player_spawn_pos
        self.create_tiles()
        self.build_walls()
        self.build_bottom_death()

    def create_tiles(self):
        for i in range(len(self.TILES_TEXT)):
            for j in range(len(self.TILES_TEXT[0])):
                if (self.TILES_TEXT[i][j] == "X"):
                    tile_type = tile.TileType.SKY
                elif (self.TILES_TEXT[i][j] == "F"):
                    tile_type = tile.TileType.FLOOR
                elif (self.TILES_TEXT[i][j] == "L"):
                    tile_type = tile.TileType.LAVA
                self.TILES.append(tile.Tile(tile_type, [j, i]))
    
    def build_walls(self):
        for i in range(len(self.TILES_TEXT)):
            self.TILES.append(tile.Tile(tile.TileType.FLOOR, [-1, i]))
            self.TILES.append(tile.Tile(tile.TileType.FLOOR, [len(self.TILES_TEXT[0]), i]))
    
    def build_bottom_death(self):
        for i in range (len(self.TILES_TEXT[0])):
            # Set to floor for testing purposes. Revert to lava
            self.TILES.append(tile.Tile(tile.TileType.FLOOR, [i, len(self.TILES_TEXT)]))

    
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
    ], (2, 5))  



