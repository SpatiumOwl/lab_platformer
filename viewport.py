import pygame

class ViewPort:
    WINDOW_SIZE = (700, 450)
    UNIT_SIZE = (25, 15)
    TILE_SIZE = (WINDOW_SIZE[0]/UNIT_SIZE[0], WINDOW_SIZE[1]/UNIT_SIZE[1])
    TARGET_FPS = 60
    WINDOW = pygame.display.set_mode(WINDOW_SIZE)
    CLOCK = pygame.time.Clock()
    delta_time = 0
    key_down = []

    def start_next_frame():
        ViewPort.delta_time = ViewPort.CLOCK.tick() / 1000
        ViewPort.key_down = []
