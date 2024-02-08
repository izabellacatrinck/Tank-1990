import pygame

bullet_image = pygame.image.load('assets/bullet_resized.png')

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(bullet_image, (self.x, self.y))

    def move(self):
        if self.active:
            self.y -= 4
            if self.y < 0:
                self.active = False