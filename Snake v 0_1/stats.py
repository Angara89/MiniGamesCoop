from DrawnObj import DrawnObj
from block import Block
import pygame
import sys


class Stats(DrawnObj):
	
	def __init__(self, blockT: Block, size: tuple, anchorPoint: tuple, text: str):
		
		
		super().__init__(blockT, size, anchorPoint)
		self.text = text
		self.var = -1
		self.myFont = pygame.font.Font(None, int(size[1]))
		self.color = (255, 0, 0)
		self.indentText = (int(self.size[0] / 100 * 5), int(self.size[1] / 100 * 5))
		self.print_text()
	
	def print_text(self):
		if (self.var == -1):
			textSurface = self.myFont.render(self.text, True, self.color)
		else:
			textSurface = self.myFont.render(self.text + " " + str(self.var), True, self.color)
		self.thisSurface.fill((0, 0, 0, 0))
		self.thisSurface.blit(textSurface, self.indentText)
