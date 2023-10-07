import pygame.rect

import DrawnObj
import block
PIXELCELL = 20
class Field(DrawnObj.DrawnObj):
	
	def __init__(self, tblock: block.Block):
		super().__init__(tblock)
		self.apples = []
		self.snakes = []
		self.allCellsInW = int(tblock.width /20)
		self.allCellsInH = int(tblock.height /20)

		self.draw_border_rect()
		tblock.myDrawnObj.append(self)
		
		
	def draw(self):
		pass
	
	def draw_border_rect(self):
		indent = 30
		w = self.block.width - indent*2
		h = self.block.height - indent*2
		rect = pygame.Rect(indent, indent, w, h)
		
		rectColor = (100, 100, 100)
		pygame.draw.rect(self.block, rectColor, rect, border_radius=20)
		
		

