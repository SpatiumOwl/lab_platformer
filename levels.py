import coin
import tile
import lava_droplet_spawner as lds

class Level:
    def __init__(self, tiles_text : str, player_spawn_pos, lava_droplet_spawner_positions, coin_positions):
        self.TILES_TEXT = tiles_text
        self.COIN_POSITIONS = coin_positions
        self.LAVA_DROPLET_SPAWNER_POSITIONS = lava_droplet_spawner_positions
        self.player_spawn_pos = player_spawn_pos
        self.lava_droplets = []       

    def enable(self):
        self.create_tiles()
        self.build_walls()
        self.build_bottom_death()
        self.add_lava_droplet_spawners(self.LAVA_DROPLET_SPAWNER_POSITIONS)
        self.add_coins()

    def create_tiles(self):
        self.tiles = []
        for i in range(len(self.TILES_TEXT)):
            for j in range(len(self.TILES_TEXT[0])):
                if (self.TILES_TEXT[i][j] == "X"):
                    tile_type = tile.TileType.SKY
                elif (self.TILES_TEXT[i][j] == "F"):
                    tile_type = tile.TileType.FLOOR
                elif (self.TILES_TEXT[i][j] == "L"):
                    tile_type = tile.TileType.LAVA
                self.tiles.append(tile.Tile(tile_type, [j, i]))
    
    def build_walls(self):
        for i in range(len(self.TILES_TEXT)):
            self.tiles.append(tile.Tile(tile.TileType.FLOOR, [-1, i]))
            self.tiles.append(tile.Tile(tile.TileType.FLOOR, [len(self.TILES_TEXT[0]), i]))
    
    def build_bottom_death(self):
        for i in range (len(self.TILES_TEXT[0])):
            # Set to floor for testing purposes. Revert to lava
            self.tiles.append(tile.Tile(tile.TileType.FLOOR, [i, len(self.TILES_TEXT)]))
    
    def add_lava_droplet_spawners(self, lava_droplet_spawner_positions):
        self.lava_droplet_spawners = []
        for position in lava_droplet_spawner_positions:
            self.lava_droplet_spawners.append(lds.LavaDropletSpawner(position, self))
    
    def add_coins(self):
        self.coins = []
        for position in self.COIN_POSITIONS:
            self.coins.append(coin.Coin(position, self))
    
    def reset_coins(self):
        self.coins = []
        self.add_coins()
    
    def disable(self):
        self.delete_all_tiles()
        self.delete_lava_droplet_spawners()
        self.delete_coins()
    
    def delete_all_tiles(self):
        for current_tile in self.tiles:
            if current_tile.TILE_TYPE == tile.TileType.FLOOR:
                current_tile.rigidbody.delete()
        self.tiles = []

    def delete_lava_droplet_spawners(self):
        self.lava_droplet_spawners = []
    
    def delete_coins(self):
        self.coins = []
    
class GameLevels:   
    LEVEL_2 = Level([
        "XXXFLLLLLLLLLLLLLLLLLLLLL",
        "XXXFLLLLLLLLLLLLLLLLLLLLL",
        "XXXFLFFFFFFFFFFFFFFLLLLLL",
        "XXXXXXXXXXXXXXXXXXFLFFFFF",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXFFFFFFXXXFFF",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXFFFFFFXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXFFFFFFFFFFFF",
        "FFFFXXXXXXXXXXXXXXXXXXXXX",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL"
    ], (2, 5), [(4, 3), (19,4)], [(4, 3), (14, 5), (13, 8), (24, 5)])
    LEVEL_1 = Level([
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXFFFFFFFXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "FFFFFFXXXXXXXXXXXXXFFFFFF",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXFFFFFFFFFXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "FFFFFFFXXXXXXXXXXXFFFFFFF",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL"
    ], (2, 8), [], [(2, 5), (22, 5), (22, 9), (12, 3)])
    LEVEL_3 = Level([
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "FFFFLFFFFLFFFFLFFFFLFFFFL",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXFFF",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXFFFFFFFFFFFF",
        "FFFFXXXXXFXXXXXXXXXXXXXXX",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL",
        "LLLLLLLLLLLLLLLLLLLLLLLLL"
    ], (2, 8), [(4, 4), (9, 4), (14, 4), (19, 4), (24, 4)], [(9, 8), (14, 8), (24, 8), (24, 5)])  
    LEVELS = [LEVEL_1, LEVEL_2, LEVEL_3]


