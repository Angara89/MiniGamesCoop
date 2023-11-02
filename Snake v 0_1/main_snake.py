from pygame import PixelArray

import Field
import pygame
import DrawnObj
import block
import Apple
import sys
from stats import Stats
from stat_ import Stat




COLOR_RED =(255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_MAGENTA = (255, 0, 255)
COLOR_CYAN = (0, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_LIGHT_GRAY = (192, 192, 192)


pygame.init()
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake game v2")
blocks = []

hInfoBlock = int(screenHeight / 20)


mainBlock = block.Block((screenWidth, screenHeight-hInfoBlock), anchorPoint=(0, hInfoBlock))
field = Field.Field(mainBlock)
blocks.append(mainBlock)

infoBlock = Stats((screenWidth, hInfoBlock), anchorPoint=(0, 0))
nameMainText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=8,
                    text="Snake v0.2",
                    textColor=COLOR_WHITE,
                    sizeFont="mainFont",
                    )
levelText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=5,
                    text=r"level 1/01",
                    textColor=COLOR_LIGHT_GRAY,
                    sizeFont="miniFont",
                    )
qBlockSnakeText = Stat(stats=infoBlock,
                    qIndent=1,
                    xSizeOnIndent=20,
                    text=r"Size snake: ",
                    textColor=COLOR_RED,
                    sizeFont="mediumFont",
                    number=3,
                    haveNumber=True
                    )
field.add_stat_block_quantity_snake(qBlockSnakeText)


# infoBlock.fill_color((100, 0, 100))
blocks.append(infoBlock)



clock = pygame.time.Clock()
running = True
dir = "U"
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dir = "L"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dir = "R"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dir = "D"
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                dir = "U"
    field.snake.change_direction(dir)
    field.snake.step_snake()
    field.is_apple_eaten()
    if field.is_it_a_loss():
        running = False
        
    for block in blocks:
        block.draw_all_DrawnObj()
        screen.blit(block, block.get_anchorPoint())
        
    pygame.display.update()
    
    clock.tick(6)

pygame.quit()
sys.exit()