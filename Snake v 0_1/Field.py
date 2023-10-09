import pygame.rect

import DrawnObj
import block

PIXELCELL = 100


class Field(DrawnObj.DrawnObj):
	
	def __init__(self, tblock: block.Block):
		super().__init__(tblock)
		self.apples = []
		self.snakes = []
		self.allCellsInW = int(tblock.width / 20)
		self.allCellsInH = int(tblock.height / 20)
		self.draw_border_rect()
		tblock.myDrawnObj.append(self)
	
	def draw(self):
		pass
	
	def draw_border_rect(self):
		indent = 30
		w = self.block.width - indent * 2
		h = self.block.height - indent * 2
		rect = pygame.Rect(indent, indent, w, h)
		self.rectField = rect
		rectColor = (100, 100, 100)
		pygame.draw.rect(self.block, rectColor, rect, border_radius=20)
		self.draw_cells()
	
		
		
	
	def draw_cells(self):
		rect = self.rectField
		cellsSize = PIXELCELL
		indent = 10
		rLeft = rect.left + indent
		rRight = rect.right + indent
		rTop = rect.top + indent
		rBottom = rect.bottom + indent
		for line in range(self.allCellsInW):
			pygame.draw.line(self.block,
			                 (255, 255, 255),
			                 (rLeft + line * cellsSize, rTop),
			                 (rLeft + line * cellsSize, rect.bottom - indent*2),
			                 5)
		
		for line in range(self.allCellsInH):
			pygame.draw.line(self.block,
			                 (255, 255, 255),
			                 (rLeft, rTop + line * cellsSize),
			                 (rRight - indent*2, rTop + line * cellsSize),
			                 5)
		