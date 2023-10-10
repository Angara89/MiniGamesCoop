import pygame
from block import Block


class DrawnObj:
	
	def __init__(self,  block: Block):
		self.width = block.width
		self.height = block.height
		self.anchorPoint = (0, 0)
		self.myBlock = block
	
	def draw(self):
		pass
	
	