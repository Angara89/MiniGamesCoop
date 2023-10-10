import Field
import pygame
import DrawnObj
import block
pygame.init()
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake game v2")

# mainSurface = pygame.Surface((screenWidth, screenHeight))

blocks = []
mainBlock = block.Block((screenWidth - screenWidth/5), (screenHeight), anchorPoint=(0, 0))
mainBlock.fill_color((255, 0, 0))
field = Field.Field(mainBlock),0



blocks.append(mainBlock)

infoBlock = block.Block((screenWidth/5), (screenHeight - screenHeight/4), anchorPoint=(screenWidth - screenWidth/5, 0))
infoBlock.fill_color((255, 255, 0))

blocks.append(infoBlock)

buttonBlock = block.Block((screenWidth/5), (screenHeight/4), anchorPoint=(screenWidth - screenWidth/5, screenHeight - screenHeight/4))
buttonBlock.fill_color((255, 0, 255))

blocks.append(buttonBlock)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for block in blocks:
        block.draw_all_DrawnObj()
        screen.blit(block, block.get_main_corner())
    pygame.display.update()

pygame.quit()
