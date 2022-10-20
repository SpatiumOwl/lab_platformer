import pygame

import levels as lvl
import managers as mgr
import viewport as vp
import player as pl
import userevents

def main():
    mgr.WorldManager.reset_level()

    run = True

    while run:
        vp.ViewPort.start_next_frame()

        #React to different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                vp.ViewPort.key_down.append(event.key)
            if event.type == userevents.UserEvents.PLAYER_DEAD:
                mgr.WorldManager.reset_level()

        mgr.WorldManager.draw_level_tiles()
        mgr.WorldManager.player.update()

        pygame.display.update()

if __name__ == "__main__":
    main()