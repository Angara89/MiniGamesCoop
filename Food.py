import random
import pygame
class food:
	import pygame
	def __init__(self, food_color, wight, height):
		self.food_color= food_color
		self.foodSizeX = 10
		self.foodSizeY = 10
		self.foodPos = [random.randrange(1, wight/10)*10, random.randrange(1, height/10)*10]
		
	def drawfood(self, surface):
		pygame.draw.rect(surface, self.food_color, pygame.Rect(self.foodPos[0], self.foodPos[1], self.foodSizeX, self.foodSizeY))
		
		