import pygame


class Block(pygame.Surface):
	def __init__(self, width: int, height: int, anchorPoint: tuple):
		super().__init__((width, height))
		self.width = width
		self.height = height
		self.anchorPoint = anchorPoint
		self.myDrawnObj = []
	
	def draw(self):
		pass
	
	def add_new_DrawObj(self, drawnObj):
		self.myDrawnObj = drawnObj
	
	def get_main_corner(self):
		return self.anchorPoint

	def fill_color(self, color: pygame.Color):
		self.fill(color)