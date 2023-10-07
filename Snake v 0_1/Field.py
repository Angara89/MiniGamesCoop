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
		self.rectField = rect
		rectColor = (100, 100, 100)
		pygame.draw.rect(self.block, rectColor, rect, border_radius=20)
		self.draw_cells()
		
		
	def draw_cells(self):
		rect = self.rectField
		cellsSize = 50
		for line in range(self.allCellsInW+1):
			pygame.draw.line(self.block, (255, 255, 255), (rect.left+5+line*cellsSize, rect.top+5), (rect.right-5+line*cellsSize, rect.bottom-5), 5)
		
		for line in range(self.allCellsInH+1):
			pygame.draw.line(self.block, (0, 255, 255), (rect.top+5+line*cellsSize, rect.left + 5),(rect.bottom-5+line*cellsSize, rect.right - 5), 5)
