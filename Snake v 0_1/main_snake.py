from pygame import PixelArray
from Field import Field
from DrawnObj import DrawnObj
from block import Block
from Apple import Apple
from stats import Stats
from stat_ import Stat
from threading import Thread
from barrier import Barrier
from common import FPS

import random
import common
import threading
import sys
import pygame
import random

SPEED = 5

pygame.init()
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake game v2")
blocks = []
hInfoBlock = int(screenHeight / 20)

mainBlock = Block((screenWidth, screenHeight-hInfoBlock), anchorPoint=(0, hInfoBlock))
field = Field(mainBlock, SPEED)
barriers = []
# for _ in range(10):
#     barriers.append(
#         Barrier(field=field, coord=(random.randint(0, field.quantityCellsX), random.randint(0, field.quantityCellsY)),
#                 isMove=True)
#     )
barriers.append(Barrier(field=field, coord=(5, 5), isMove=True, moveStep=["U", "R", "U"]))
blocks.append(mainBlock)

infoBlock = Stats((screenWidth, hInfoBlock), anchorPoint=(0, 0))
nameMainText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=8,
                    text="Snake v0.2",
                    textColor=common.COLOR_WHITE,
                    sizeFont="mainFont",
                    )
levelText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=5,
                    text=r"level 1/01",
                    textColor=common.COLOR_LIGHT_GRAY,
                    sizeFont="miniFont",
                    )
qBlockSnakeText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=8,
                    text=r"Size snake: ",
                    textColor=common.COLOR_RED,
                    sizeFont="mediumFont",
                    number=3,
                    haveNumber=True
                    )
pointText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=7,
                    text=r"Point: ",
                    textColor=common.COLOR_YELLOW,
                    sizeFont="mediumFont",
                    number=0,
                    haveNumber=True
                    )
infoBlock.set_pointsStat(pointText)
field.set_stats_block(infoBlock)
field.add_stat_block_quantity_snake(qBlockSnakeText)

qThisPointsText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=7,
                    text=r"Now point: ",
                    textColor=common.COLOR_YELLOW,
                    sizeFont="mediumFont",
                    number=0,
                    haveNumber=True
                    )
timeStats = Stat(stats=infoBlock,
                    qIndent=10,
                    xSizeOnIndent=7,
                    text=r"",
                    textColor=common.COLOR_YELLOW,
                    sizeFont="mediumFont",
                    number=0,
                    haveNumber=True
                    )
infoBlock.set_addToPointsStat(qThisPointsText)
blocks.append(infoBlock)

running = True
cFPS = 0
def draw_loop():
    clock = pygame.time.Clock()
    global running
    global screen
    global blocks
    global FPS
    global cFPS
    
    while (running):
        cFPS += 1
        screen.fill((0, 0, 0, 0))
        for block in blocks:
            block.draw_all_DrawnObj()
            screen.blit(block, block.get_anchorPoint())
        
        pygame.display.update()
        clock.tick(FPS)
theardDrawLoop = Thread(target=draw_loop)
theardDrawLoop.start()

def fps():
    global timeStats
    global cFPS
    clock = pygame.time.Clock()
    global running
    while running:
        timeStats.set_my_number(cFPS)
        cFPS = 0
        clock.tick(1)
theardFPS = Thread(target=fps)
theardFPS.start()

clock = pygame.time.Clock()
dir = []
lastDir = "U"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dir.append("L")
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dir.append("R")
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dir.append("D")
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                dir.append("U")
    infoBlock.step_snake()
    if len(dir) == 0:
        field.snake.change_direction(lastDir)
    else:
        lastDir = dir[0]
        field.snake.change_direction(dir.pop(0))
  
    field.snake.step_snake()
    for barrier in barriers:
        barrier.move()
        
    field.is_apple_eaten()
    if field.is_it_a_loss():
        running = False
        break
    clock.tick(SPEED)

clock.tick(1)
theardFPS.join()
theardDrawLoop.join()
pygame.quit()
sys.exit()