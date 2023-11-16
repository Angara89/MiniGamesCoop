import pygame
from DrawnObj import DrawnObj
from Field import Field
import block
import random


class Apple(DrawnObj):
	
	def __init__(self, field: Field, size: tuple, aPoint: tuple = (0, 0), path: str = "___"):
		super().__init__(field.myBlock, (field.PIXEL_CELL, field.PIXEL_CELL), aPoint, path)
		self.myField = field
		self.coord = self.new_random_coord()
		self.anchorPoint = self.myField.get_new_anchorPoint_on_coord(self.coord)
		self.soundEat = pygame.mixer.Sound(r"material\sound\hhhhraaaaaammm_1.wav")
	
	
	def apple_is_eaten(self):
		self.soundEat.play()
		self.coord = self.new_random_coord()
		self.anchorPoint = self.myField.get_new_anchorPoint_on_coord(self.coord)
		
	def new_random_coord(self):
		flag = 0
		newCoord = (0, 0)
		while flag == 0:
			yq = self.myField.quantityCellsY
			xq = self.myField.quantityCellsX
			yVar = random.randint(0, yq-1)
			xVar = random.randint(0, xq-1)
			newCoord = (xVar, yVar)
			
			flag = 1
			for part in self.myField.snake.parts:
				if(newCoord == part):
					flag = 0
			if self.myField.snake.tail == newCoord or self.myField.snake.head == newCoord:
				flag = 0
			
		return newCoord