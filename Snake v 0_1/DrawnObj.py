import pygame
from block import Block


class DrawnObj:
	
	def __init__(self, width, height, anchorPoint, block):
		self.width = width
		self.height = height
		self.anchorPoint = anchorPoint
		self.block = block
	
	def draw(self):
		pass
	
	