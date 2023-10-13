import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
blue = (121, 197, 216)
red = (181, 65, 111)
black = (0, 0, 0)


disWight = 800
disHeight = 600
dis = pygame.display.set_mode((disWight, disHeight))
pygame.display.set_caption('Snake by Stradivarius')



clock = pygame.time.Clock()

snakespeed = 20
snakeblock = 10

varX = disWight / 2
varY = disHeight / 2

varXChange = 0
varYChange = 0

fontStyle = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    dis.blit(mesg, [disWight/3, disHeight/3])
    
def gameLoop():
    gameover = False
    gameclose = False
    
    varx = disWight / 2
    vary = disHeight / 2
    
    varxchange = 0
    varychange = 0
    
    foodx = round(random.randrange(0, disWight - snakeblock) / 10) * 10
    foody = round(random.randrange(0, disWight - snakeblock) / 10) * 10


    while not gameover:
    
        while gameclose == True:
            dis.fill(white)
            message("You Lost! Peress Q-quit or C to play again", red)
            pygame.display.update()
    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        gameclose = False
                    if event.key == pygame.K_c:
                        gameLoop()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    varxchange = -snakeblock
                    varychange = 0
                elif event.key == pygame.K_RIGHT:
                    varxchange = snakeblock
                    varychange = 0
                elif event.key == pygame.K_UP:
                    varychange = -snakeblock
                    varxchange = 0
                elif event.key == pygame.K_DOWN:
                    varychange = snakeblock
                    varxchange = 0
    
        if varx >= disWight or varx < 0 or vary >= disHeight or vary < 0:
            gameclose = True
    
        varx += varxchange
        vary += varychange
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snakeblock, snakeblock])
        pygame.draw.rect(dis, blue, [varx, vary, snakeblock, snakeblock])
        pygame.display.update()
        
        clock.tick(snakespeed)
        
        if varx == foodx and vary == foody:
            print("Ymmy!")
        clock.tick(snakespeed)


    pygame.quit()
    quit()

gameLoop()