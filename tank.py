import pygame

tank_image = pygame.image.load('assets/tank_resized.png')

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(tank_image, (self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy