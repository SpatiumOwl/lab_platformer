import pygame

import managers as mgr
import viewport as vp
import player as pl

def main():
    player = pl.Player((2, 5))

    run = True

    while run:
        vp.ViewPort.start_next_frame()

        #React to different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                vp.ViewPort.key_down.append(event.key)

        mgr.WorldManager.draw_level_tiles()
        player.update()

        pygame.display.update()

if __name__ == "__main__":
    main()