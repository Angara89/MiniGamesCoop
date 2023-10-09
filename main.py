import pygame

pygame.init()

white = (255, 255, 255)
blue = (121, 197, 216)
red = (181, 65, 111)

dis = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake by Stradivarius')

game_over = False

varX = 300
varY = 300

varXChange = 0
varYChange = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                varXChange = -10
                varYChange = 0
            elif event.key == pygame.K_RIGHT:
                varXChange = 10
                varYChange = 0
            elif event.key == pygame.K_UP:
                varYChange = -10
                varXChange = 0
            elif event.key == pygame.K_DOWN:
                varYChange = 10
                varXChange = 0

    varX += varXChange
    varY += varYChange
    dis.fill(white)
    pygame.draw.rect(dis, blue, [varX, varY, 100, 100])


    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()