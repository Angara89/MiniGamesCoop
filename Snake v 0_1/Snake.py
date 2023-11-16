from DrawnObj import DrawnObj
import pygame
from Field import Field
from common import FPS
class Snake(DrawnObj):
	
	
	def __init__(self, field: Field, speed: int, path: str = "___"):
		super().__init__(field.myBlock, field.mainRect.size, field.mainRect.topleft, path)
		self.myField = field
		
		self.direction = "U"
		self.head = (int(self.myField.quantityCellsX/2), int(self.myField.quantityCellsY/2))
		self.tail = (self.head[0], self.head[1] + 1)
		self.parts = [self.tail]
		self.tail = (self.head[0], self.head[1] + 2)
		PIXEL_CELL = self.myField.PIXEL_CELL
		self.imgHead = pygame.image.load(r"material\snake_head_3.png")
		self.imgHead = pygame.transform.scale(self.imgHead, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgPart = pygame.image.load(r"material\snake_part_5.png")
		self.imgPart = pygame.transform.scale(self.imgPart, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgTail = pygame.image.load(r"material\snake_part_5.png")
		self.imgTail = pygame.transform.scale(self.imgTail, (PIXEL_CELL, PIXEL_CELL))
		
		self.flagEatenApple = False
		
		self.draw_snake()
		self.speed = speed
		self.fps = FPS
	

		
	def step_snake(self):
		# self.move_snake()
		self.draw_animation()
	
	def draw_animation(self):
		clock = pygame.time.Clock()
		head_surface = self.imgHead.convert_alpha()
		part_surface = self.imgPart.convert_alpha()
		tail_surface = self.imgTail.convert_alpha()
		countFrame = self.fps / self.speed
		
		
		headPos = self.get_new_anchorPoint(self.head)
		tailPos = self.get_new_anchorPoint(self.tail)
		partsPos = []
		for part in self.parts:
			partsPos.append(self.get_new_anchorPoint(part))
		
		self.move_snake()
		
		headNeedPos = self.get_new_anchorPoint(self.head)
		tailNeedPos = self.get_new_anchorPoint(self.tail)
		partsNeedPos = []
		for part in self.parts:
			partsNeedPos.append(self.get_new_anchorPoint(part))
		
		partPosAndChange = []
		for i in range(len(partsPos)):
			partPosAndChange.append(
				(
					partsPos[i],
					(
						int((partsNeedPos[i][0] - partsPos[i][0]) / countFrame),
						int((partsNeedPos[i][1] - partsPos[i][1]) / countFrame)
					)
				)
			)
		
		changeXT = (tailNeedPos[0] - tailPos[0]) / countFrame
		changeYT = (tailNeedPos[1] - tailPos[1]) / countFrame
		
		changeX = (headNeedPos[0] - headPos[0]) / countFrame
		changeY = (headNeedPos[1] - headPos[1]) / countFrame
		
		p = 0
		while p != countFrame:
			p += 1
			
			
			self.thisSurface.fill((0, 0, 0, 0))
			self.thisSurface.blit(head_surface, headPos)
			self.thisSurface.blit(tail_surface, tailPos)
			
			for i in range(len(partPosAndChange)):
				self.thisSurface.blit(part_surface, partPosAndChange[i][0])
				partPosAndChange[i] = (
					(
						partPosAndChange[i][0][0] + partPosAndChange[i][1][0],
						partPosAndChange[i][0][1] + partPosAndChange[i][1][1],
					),
					partPosAndChange[i][1]
				)
				
			headPos = (headPos[0] + changeX, headPos[1] + changeY)
			tailPos = (tailPos[0] + changeXT, tailPos[1] + changeYT)
			clock.tick(self.fps)
			
			
		
		
		
	def move_snake(self):
		
		xChange = 0
		yChange = 0
		if self.direction == "D":
			yChange += 1
		elif self.direction == "U":
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
	
	