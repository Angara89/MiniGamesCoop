from pygame import PixelArray

import Field
import pygame
import DrawnObj
import block
import Apple
import sys
from stats import Stats
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_GREEN = pygame.Color(0, 255, 0)
COLOR_BLUE = pygame.Color(0, 0, 255)
COLOR_YELLOW = pygame.Color(255, 255, 0)
COLOR_MAGENTA = pygame.Color(255, 0, 255)
COLOR_CYAN = pygame.Color(0, 255, 255)
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_GRAY = pygame.Color(128, 128, 128)
COLOR_LIGHT_GRAY = pygame.Color(192, 192, 192)


pygame.init()
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake game v2")
blocks = []

mainBlock = block.Block(((screenWidth - screenWidth/5), (screenHeight)), anchorPoint=(0, 0))
field = Field.Field(mainBlock)
blocks.append(mainBlock)

infoBlock = block.Block(((screenWidth/5), (screenHeight - screenHeight/4)), anchorPoint=(screenWidth - screenWidth/5, 0))
stats = Stats(infoBlock, (infoBlock.size[0], infoBlock.size[1] / 100 * 5), (0, 0), "Snake1")

infoBlock.fill_color(COLOR_GRAY)


blocks.append(infoBlock)

buttonBlock = block.Block(((screenWidth/5), (screenHeight/4)), anchorPoint=(screenWidth - screenWidth/5, screenHeight - screenHeight/4))
buttonBlock.fill_color(COLOR_YELLOW)
blocks.append(buttonBlock) 

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
    
    clock.tick(10)

pygame.quit()
sys.exit()