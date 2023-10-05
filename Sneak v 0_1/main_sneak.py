from typing import Sequence

import pygame


def new_color(r, g, b):
	return tuple[r, g, b]


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game")
#rect1 = pygame.draw.rect(new_color(0, 255, 153), )

running = True

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()

pygame.quit()