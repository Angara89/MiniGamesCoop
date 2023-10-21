from pygame import PixelArray

import Field
import pygame
import DrawnObj
import block
import Apple
import sys



imgApple = r"material\apple_1.png"

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

# mainSurface = pygame.Surface((screenWidth, screenHeight))

blocks = []
mainBlock = block.Block(((screenWidth - screenWidth/5), (screenHeight)), anchorPoint=(0, 0))
# mainBlock.fill_color((0, 255, 255))

field = Field.Field(mainBlock)

blocks.append(mainBlock)



infoBlock = block.Block(((screenWidth/5), (screenHeight - screenHeight/4)), anchorPoint=(screenWidth - screenWidth/5, 0))
infoBlock.fill_color(COLOR_RED)

blocks.append(infoBlock)



buttonBlock = block.Block(((screenWidth/5), (screenHeight/4)), anchorPoint=(screenWidth - screenWidth/5, screenHeight - screenHeight/4))
buttonBlock.fill_color(COLOR_YELLOW)

blocks.append(buttonBlock)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                field.snake.change_direction("L")
            elif event.key == pygame.K_RIGHT:
                field.snake.change_direction("R")
            elif event.key == pygame.K_DOWN:
                field.snake.change_direction("U")
            elif event.key == pygame.K_UP:
                field.snake.change_direction("D")
                
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