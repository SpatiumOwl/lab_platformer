import time
import pygame

import managers as mgr
import viewport as vp 
import userevents
import sfx

def main():
    mgr.WorldManager.put_on_next_level()
    sfx.SFX.BGM.play(-1)

    run = True

    while run:
        vp.ViewPort.start_next_frame()

        #React to different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mgr.WorldManager.current_level.disable()
                sfx.SFX.BGM.stop()
                sfx.SFX.CLOSED_GAME.play()
                pygame.time.wait(int(sfx.SFX.CLOSED_GAME.get_length()*1000))
                run = False
            if event.type == pygame.KEYDOWN:
                vp.ViewPort.key_down.append(event.key)
            if event.type == userevents.UserEvents.PLAYER_DEAD:
                sfx.SFX.DEATH.play()
                mgr.WorldManager.reset_level()
            if event.type == userevents.UserEvents.FINISHED_LEVEL:
                sfx.SFX.NEXT_LEVEL.play()
                mgr.WorldManager.put_on_next_level()
            if event.type == userevents.UserEvents.COLLECTED_COIN:
                sfx.SFX.GOT_COIN.play()
            if event.type == userevents.UserEvents.END_GAME:
                mgr.WorldManager.current_level.disable()
                sfx.SFX.BGM.stop()
                sfx.SFX.FINISHED_GAME.play()
                pygame.time.wait(int(sfx.SFX.FINISHED_GAME.get_length()*1000))
                run = False
        if (run):
            mgr.WorldManager.update()

            pygame.display.update()

if __name__ == "__main__":
    main()