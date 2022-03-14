from config import *


class Screen:
    surface: pygame.Surface

    def __init__(self):
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.arena = self.surface.subsurface(
            (0, TOP_BAR_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - TOP_BAR_HEIGHT))
        self.font = pygame.font.Font("font/Pixeltype.ttf", 100)

    def draw(self, mapa, score):
        self.surface.fill(BG_COLOR)

        score_p1 = self.font.render(
            str(score[0]), False, TANK_1_COLOR)
        score_p2 = self.font.render(
            str(score[1]), False, TANK_2_COLOR)

        self.surface.blit(score_p1, (220, 10))
        self.surface.blit(score_p2, (550, 10))

        for rect in mapa:
            pygame.draw.rect(self.arena, RECTS_COLOR, rect)
