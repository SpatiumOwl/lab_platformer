import pygame
import os

class SFX:
    pygame.mixer.init()

    BGM = pygame.mixer.Sound(os.path.join("Sound", "BGM_Mission_Stage_Crater_01_A [1].mp3"))
    BGM.set_volume(0.3)

    GOT_COIN = pygame.mixer.Sound(os.path.join("Sound", "VoiceFDefeat01.wav"))
    GOT_COIN.set_volume(0.5)

    NEXT_LEVEL = pygame.mixer.Sound(os.path.join("Sound", "VoiceFJet00.wav"))
    NEXT_LEVEL.set_volume(0.5)

    DEATH = pygame.mixer.Sound(os.path.join("Sound", "VoiceFSoul03.wav"))
    DEATH.set_volume(0.4)

    CLOSED_GAME = pygame.mixer.Sound(os.path.join("Sound", "MusicRIP.mp3"))
    CLOSED_GAME.set_volume(0.5)

    FINISHED_GAME = pygame.mixer.Sound(os.path.join("Sound", "MusicOnward.mp3"))
    FINISHED_GAME.set_volume(0.5)