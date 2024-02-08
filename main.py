import pygame
from pygame.locals import *
from tank import Tank
from bullet import Bullet
from block import Block

# Inicializando o Pygame
pygame.init()

# Definindo constantes para a largura e altura da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

# Criando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Criando os objetos
tank = Tank(50, 200)
bullet = Bullet(-1, -1)
blocks = [Block(60, 60), Block(150, 60), Block(240, 60)]

# Loop principal do jogo
running = True
while running:
    # Preenchendo o fundo com preto
    screen.fill((0, 0, 0))

    # Desenhando os objetos
    tank.draw(screen)
    bullet.draw(screen)
    for block in blocks:
        block.draw(screen)

    # Atualizando a tela
    pygame.display.flip()

    # Lidando com eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                tank.move(-2, 0)
            elif event.key == K_RIGHT:
                tank.move(2, 0)
            elif event.key == K_SPACE:
                if not bullet.active:
                    bullet.active = True
                    bullet.x = tank.x
                    bullet.y = tank.y

    # Movendo a bala
    bullet.move()

pygame.quit()