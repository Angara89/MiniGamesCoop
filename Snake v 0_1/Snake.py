from DrawnObj import DrawnObj
import pygame
from Field import Field
class Snake(DrawnObj):
	
	
	def __init__(self, field: Field, path: str = "___"):
		super().__init__(field.myBlock, field.mainRect.size, field.mainRect.topleft, path)
		self.myField = field
		
		self.direction = "U"
		self.head = (int(self.myField.quantityCellsX/2), int(self.myField.quantityCellsY/2))
		self.tail = (self.head[0], self.head[1] - 1)
		self.parts = []
		PIXEL_CELL = self.myField.PIXEL_CELL
		self.imgHead = pygame.image.load(r"material\snake_head.png")
		self.imgHead = pygame.transform.scale(self.imgHead, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgPart = pygame.image.load(r"material\snake_part.png")
		self.imgPart = pygame.transform.scale(self.imgPart, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgTail = pygame.image.load(r"material\sneak_last_part.png")
		self.imgTail = pygame.transform.scale(self.imgTail, (PIXEL_CELL, PIXEL_CELL))
		
	def eat_apple(self):
		xChange = 0
		yChange = 0
		if self.direction == "U":
			yChange += 1
		elif self.direction == "D":
			yChange -= 1
		elif self.direction == "R":
			xChange += 1
		elif self.direction == "L":
			xChange -= 1
		
		self.parts.append((self.parts[-1][0], self.parts[-1][1]))
		
		for i in reversed(range(1, len(self.parts) - 1)):
			self.parts[i] = self.parts[i - 1]
		self.parts[0] = self.head

		self.head = (self.head[0] + xChange, self.head[1] + yChange)
		
	def move_snake(self):
		
		xChange = 0
		yChange = 0
		if self.direction == "U":
			yChange += 1
		elif self.direction == "D":
			yChange -= 1
		elif self.direction == "R":
			xChange += 1
		elif self.direction == "L":
			xChange -= 1

		self.tail = self.parts[-1]

		for i in reversed(range(1, len(self.parts))):
			self.parts[i] = self.parts[i - 1]
		self.parts[0] = self.head

		self.head = (self.head[0] + xChange, self.head[1] + yChange)
		
	def draw_snake(self):
		self.thisSurface.blit(self.imgHead, self.head)
		
		for part in self.parts:  # TODO корее всего тут он будет просто перерисовывать один part а новое место ПЕРЕДЕЛАТЬ
			self.thisSurface.blit(self.imgPart, part)
			
		self.thisSurface.blit(self.imgTail, self.imgTail)
		
	def change_direction(self, dir: str):
		self.direction = dir