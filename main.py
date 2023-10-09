import pygame
import time
pygame.init()

white = (255, 255, 255)
blue = (121, 197, 216)
red = (181, 65, 111)


disWight = 800
disHeight = 600
dis = pygame.display.set_mode((disWight, disHeight))

pygame.display.set_caption('Snake by Stradivarius')

game_over = False

varX = disWight/2
varY = disHeight/2

snakeBlock = 10

varXChange = 0
varYChange = 0

clock = pygame.time.Clock()
snakeSpeed = 20


fontStyle = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    dis.blit(mesg, [disWight/2, disHeight/2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                varXChange = -snakeBlock
                varYChange = 0
            elif event.key == pygame.K_RIGHT:
                varXChange = snakeBlock
                varYChange = 0
            elif event.key == pygame.K_UP:
                varYChange = -snakeBlock
                varXChange = 0
            elif event.key == pygame.K_DOWN:
                varYChange = snakeBlock
                varXChange = 0
    
    if varX >= disWight or varX < 0 or varY >= disHeight or varY < 0:
        game_over = True
    
    varX += varXChange
    varY += varYChange
    dis.fill(white)
    pygame.draw.rect(dis, blue, [varX, varY, snakeBlock, snakeBlock])
    
    pygame.display.update()
    clock.tick(snakeSpeed)

message("You lost", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()