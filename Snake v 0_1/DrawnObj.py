import pygame
from block import Block


# TODO придумать как отображать все обьекты данного класса на своем блоке
class DrawnObj(pygame.Surface):
	
	def __init__(self, block: Block, tup: tuple, aPoint: tuple):
		super().__init__(tup)
		self.width = tup[0]
		self.height = tup[1]
		self.anchorPoint = aPoint
		self.myBlock = block
	
	def draw(self):
		pass
	
	
