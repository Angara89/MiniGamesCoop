
import pygame


class Field(pygame.Surface):
	def __init__(self, width, height, size):
		super().__init__(size)
		self.width = width
		self.height = height
		self.apples = []
		self.cellsSnake = []
		
