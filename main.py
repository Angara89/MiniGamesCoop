import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
blue = (121, 197, 216)
red = (181, 65, 111)
black = (0, 0, 0)
green = (0, 255, 0)

disWight = 800
disHeight = 600
dis = pygame.display.set_mode((disWight, disHeight))
pygame.display.set_caption('Snake by Stradivarius')

from SurfaceSnake import Surface
surface = Surface(800, 600)
from SnakeBody import Body
snake = Body(green, 10, 10)


clock = pygame.time.Clock()

snakespeed = 20
snakeblock = 10

varX = disWight / 2
varY = disHeight / 2

varXChange = 0
varYChange = 0

fontStyle = pygame.font.SysFont("bahnschrift", 25)
scoreFont = pygame.font.SysFont("comicsans", 35)

def ourSnake(snakeblock, snakelist):
    for x in snakelist:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeblock, snakeblock])
        
from SurfaceSnake import Surface
        
surface = Surface(10, 10)


def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    dis.blit(mesg, [disWight/6, disHeight/3])
    
def gameLoop():
    gameOver = False
    gameclose = False
    
    varx = disWight / 2
    vary = disHeight / 2
    
    varxchange = 0
    varychange = 0
    
    snakelist = []
    lengthofsnake = 1
    
    foodx = round(random.randrange(0, disWight - snakeblock) / 10) * 10
    foody = round(random.randrange(0, disWight - snakeblock) / 10) * 10


    while not gameOver:
    
        while gameclose == True:
            dis.fill(white)
            message("You Lost! Peress Q-quit or C to play again", red)
            pygame.display.update()
    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameclose = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    varxchange = -snakeblock
                    varychange= 0
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
        snakehead = []
        snakehead.append(varx)
        snakehead.append(vary)
        snakelist.append(snakehead)
        if len(snakelist)> lengthofsnake:
            del snakelist[0]
            
        for x in snakelist[:-1]:
            if x == snakehead:
                gameclose = True
                
        ourSnake(snakeblock, snakelist)
        
        pygame.display.update()
        
        clock.tick(snakespeed)
        
        if varx == foodx and vary == foody:
            foodx = round(random.randrange(0, disWight - snakeblock)/ 10) * 10
            foody = round(random.randrange(0, disHeight - snakeblock)/ 10) * 10
            lengthofsnake += 1
        clock.tick(snakespeed)


    pygame.quit()
    quit()

gameLoop()