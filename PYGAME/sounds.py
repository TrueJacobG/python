import pygame

pygame.init()


class Music():
    knifeSound = pygame.mixer.Sound("character/knife.wav")
    hitSound = pygame.mixer.Sound("character/hit.wav")
    hit2Sound = pygame.mixer.Sound("character/hit2.wav")
    jumpSound = pygame.mixer.Sound("character/jump.wav")

    pygame.mixer.Sound.set_volume(knifeSound, 0.3)
    pygame.mixer.Sound.set_volume(hitSound, 0.3)
    pygame.mixer.Sound.set_volume(hit2Sound, 0.3)
    pygame.mixer.Sound.set_volume(jumpSound, 0.1)

    music = pygame.mixer.music.load(
        "character/MUSICadmiralbob77-HighAboveTheDarkness.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
