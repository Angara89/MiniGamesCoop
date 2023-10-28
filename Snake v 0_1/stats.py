from DrawnObj import DrawnObj
from block import Block
import pygame
import sys


class Stats(DrawnObj):
	mainIndentV = None
	subIndentV = None
	minIndentV = None
	mainIndentH = None
	
	aPointNow = 0
	def __init__(self, blockT: Block, flag: int, text: str, color: tuple = (255, 255, 255)):
		if (self.mainIndentV == None):
			self.mainIndentV = int(blockT.size[1] / 100 * 5)
			self.subIndentV = int(self.mainIndentV / 2)
			self.minIndentV = int(self.mainIndentV / 4)
			self.mainIndentH = int(blockT.size[0] / 100 * 10)
		
		self.text = text
		self.var = -1
		
		self.myFont = pygame.font.Font(None, int(self.mainIndentV))
		self.color = color
		if (flag == 1):
			if (self.aPointNow != 0):
				raise Exception("Two main text")
			self.centering = True
			self.sizeFont = self.mainIndentV
			super().__init__(blockT,
			                 (blockT.size[0] - self.mainIndentH * 2, self.mainIndentV),
			                 (self.mainIndentH, self.mainIndentV))
			self.aPointNow += (self.mainIndentV * 2)
		self.print_text()
	
	
	
	def print_text(self):
		
		if self.var == -1:
			textSurface = self.myFont.render(self.text, True, self.color)
		else:
			textSurface = self.myFont.render(self.text + " " + str(self.var), True, self.color)
		self.thisSurface.fill((100, 100, 100))
		
		if self.centering == False:
			self.thisSurface.blit(textSurface, (0, 0))
		else:
			indentX = int((self.thisSurface.get_size()[0] - textSurface.get_size()[0]) / 2)
			self.thisSurface.blit(textSurface, (indentX, 0))