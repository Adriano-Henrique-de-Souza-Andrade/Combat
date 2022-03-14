import pygame
import game

pygame.init()
pygame.mixer.init()

game.Game().loop()

pygame.quit()
