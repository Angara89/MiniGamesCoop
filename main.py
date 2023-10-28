import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (61, 143, 186)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
	mesg = font_style.render(msg, True, color)
	dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop():
	game_over = False
	game_close = False
	
	x1 = dis_width / 2
	y1 = dis_height / 2
	
	x1_change = 0
	y1_change = 0
	
	snake_List = []
	Length_of_skake = 1
	
	food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
	food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
	
	while not game_close:
		
		while game_over:
			dis.fill(white)
			message("You lost! Q - quit A - play again", red)
			
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_close = True
						game_over = False
					elif event.key == pygame.K_a:
						gameLoop()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_UP:
					y1_change = -snake_block
					x1_change = 0
				elif event.key == pygame.K_DOWN:
					y1_change = snake_block
					x1_change = 0
	
		if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
			game_over = True
	
		x1 += x1_change
		y1 += y1_change
		dis.fill(blue)
		pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
		
		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)
		if len(snake_List) > Length_of_skake:
			del snake_List[0]
			
		for x in snake_List[:-1]:
			if x == snake_Head:
				game_over = True
				
		our_snake(snake_block, snake_List)

		pygame.display.update()
		
		if x1 == food_x and y1 == food_y:
			Length_of_skake += 1
			food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
			food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
		clock.tick(snake_speed)
		
	pygame.quit()
	quit()
gameLoop()
