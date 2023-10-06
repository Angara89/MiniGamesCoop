import pygame


class Block(pygame.Surface):
	def __init__(self, width, height, snapPoint: tuple):
		super().__init__(width, height)
		self.width = width
		self.height = height
		self.apples = []
		self.cellsSnake = []
		self.snapPoint = snapPoint
	
	def draw(self):
		pass
	
	def get_main_corner(self):
		return self.snapPoint
