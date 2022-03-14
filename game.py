from tank import Tank
from screen import Screen
from config import *


pygame.init()
pygame.mixer.init()


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.play = True
        self.screen = Screen()
        self.score = (0, 0)
        self.map = SCREEN_RECTS
        self.tank1 = Tank((45, 245), TANK_1_COLOR, pygame.K_a,
                          pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_SPACE)
        self.tank2 = Tank((710, 245), TANK_2_COLOR, pygame.K_LEFT,
                          pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_PAGEDOWN)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False

    def listen_keyboard(self):
        self.tank1.move(
            self.map, self.tank2.get_rect())
        self.tank2.move(
            self.map, self.tank1.get_rect())

        if self.tank1.shot_enemy() and not self.tank2.spin:
            self.tank2.spin = True
            self.score = (self.score[0] + 1, self.score[1])

        if self.tank2.shot_enemy() and not self.tank2.spin:
            self.tank1.spin = True
            self.score = (self.score[0], self.score[1] + 1)

    def loop(self):
        while self.play:
            if self.tank2.angle == 0 and pygame.time.get_ticks() <= 2000:
                self.tank2.angle = 180
            self.events()
            self.listen_keyboard()

            self.screen.draw(self.map, self.score)
            self.tank1.draw(self.screen.arena)
            self.tank2.draw(self.screen.arena)

            pygame.display.flip()
            self.clock.tick(60)
