import pygame

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SIZE = 5
BULLET_SPEED = 7

TANK_SPEED = 1.1

TOP_BAR_HEIGHT = 70

BG_COLOR = (140, 35, 10)
RECTS_COLOR = (190, 150, 55)

TANK_1_COLOR = (140, 200, 80)
TANK_2_COLOR = (70, 80, 200)
TANK_SIZE = 45

SHOT_SOUND = pygame.mixer.Sound("sound/sound_shot.mp3")
EXPLOSION_SOUND = pygame.mixer.Sound("sound/sound_explosion.mp3")
COLLISION_SOUND = pygame.mixer.Sound('sound/sound_collision.mp3')

SCREEN_RECTS = [(0, 0, 800, 20),
                (0, 0, 17, 531),
                (0, 511, 800, 20),
                (783, 0, 17, 531),
                (379, 0, 42, 65),
                (379, 467, 42, 65),
                (200, 244, 41, 44),
                (560, 244, 41, 44),
                (120, 88, 61, 23),
                (120, 421, 61, 23),
                (621, 88, 61, 23),
                (621, 421, 61, 23),
                (100, 178, 40, 21),
                (100, 333, 40, 21),
                (661, 178, 40, 21),
                (661, 333, 40, 21),
                (119, 178, 21, 176),
                (661, 178, 21, 176),
                (281, 133, 60, 22),
                (461, 133, 60, 22),
                (281, 377, 60, 22),
                (461, 377, 60, 22),
                (281, 133, 21, 44),
                (500, 133, 21, 44),
                (281, 355, 21, 44),
                (500, 355, 21, 44)]
