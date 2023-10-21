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
		self.parts = [self.tail]
		self.tail = (self.head[0], self.head[1] - 2)
		PIXEL_CELL = self.myField.PIXEL_CELL
		self.imgHead = pygame.image.load(r"material\snake_head_2.png")
		self.imgHead = pygame.transform.scale(self.imgHead, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgPart = pygame.image.load(r"material\snake_part_2.png")
		self.imgPart = pygame.transform.scale(self.imgPart, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgTail = pygame.image.load(r"material\sneak_last_part_2.png")
		self.imgTail = pygame.transform.scale(self.imgTail, (PIXEL_CELL, PIXEL_CELL))
		
		self.flagEatenApple = False
		
		self.draw_snake()
		
	# def eat_apple(self):
	# 	xChange = 0
	# 	yChange = 0
	# 	if self.direction == "U":
	# 		yChange += 1
	# 	elif self.direction == "D":
	# 		yChange -= 1
	# 	elif self.direction == "R":
	# 		xChange += 1
	# 	elif self.direction == "L":
	# 		xChange -= 1
	#
	# 	self.parts.append((self.parts[-1][0], self.parts[-1][1]))
	#
	# 	for i in reversed(range(1, len(self.parts) - 1)):
	# 		self.parts[i] = self.parts[i - 1]
	# 	self.parts[0] = self.head
	#
	# 	self.head = (self.head[0] + xChange, self.head[1] + yChange)
	

		
	def step_snake(self):
		self.move_snake()
		self.draw_snake()
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

		if self.flagEatenApple:
			self.parts.append(self.tail)
		else:
			self.tail = self.parts[-1]
		self.flagEatenApple = False
		
		for i in reversed(range(1, len(self.parts))):
			self.parts[i] = self.parts[i - 1]
		self.parts[0] = self.head

		self.head = (self.head[0] + xChange, self.head[1] + yChange)
		
	def draw_snake(self):
		# Создайте отдельные surface для каждой части змейки
		head_surface = self.imgHead.convert_alpha()
		part_surface = self.imgPart.convert_alpha()
		tail_surface = self.imgTail.convert_alpha()
		
		# Очистите главную surface
		self.thisSurface.fill((0, 0, 0, 0))
		
		# Рисуйте и перемещайте каждую часть змейки
		self.thisSurface.blit(head_surface, self.get_new_anchorPoint(self.head))
		
		for part in self.parts:
			self.thisSurface.blit(part_surface, self.get_new_anchorPoint(part))
		
		self.thisSurface.blit(tail_surface, self.get_new_anchorPoint(self.tail))
		
	
	def change_direction(self, dir: str):
		if (dir == "U" and self.direction == "D") or (dir == "D" and self.direction == "U"):
			pass
		elif (dir == "R" and self.direction == "L") or (dir == "L" and self.direction == "R"):
			pass
		else:
			self.direction = dir
	
	def get_new_anchorPoint(self, coord):
		return ((self.myField.PIXEL_CELL * coord[0]), (self.myField.PIXEL_CELL * coord[1]))