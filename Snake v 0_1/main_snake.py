import pygame

pygame.init()
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake game v2")

# mainSurface = pygame.Surface((screenWidth, screenHeight))

blocks = []


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obj in blocks:
        screen.blit(obj, obj.get_main_corner())
    pygame.display.update()

pygame.quit()
