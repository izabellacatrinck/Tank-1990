import pygame

block_image = pygame.image.load('assets/block_resized.png')

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(block_image, (self.x, self.y))