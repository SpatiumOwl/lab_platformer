import lava_droplet as ld

class LavaDropletSpawner:
    def __init__(self, position, level):
        self.position = position
        self.level = level
        
    def spawn_droplet(self):
        self.level.lava_droplets.append(ld.LavaDroplet(self.position, self.level))

