import pygame.rect
from coord import Coord
from DrawnObj import DrawnObj
from block import Block


INDENT_TO_BORDER_FIELD = 10

class Field(DrawnObj):
	
	def __init__(self, tBlock: Block):
		self.PIXEL_CELL = 50
		super().__init__(tBlock, tBlock.size, (0, 0))
		self.indent = int(self.myBlock.size[1] / 100)  # делаем отступы для рамки в 1 процент от высоты
		# присваеваем rect обьект в точке отступов,  шириной и длинной минус двойные отступы(так как отступы существуют с двух сторон
		self.rectField = pygame.Rect(self.indent, self.indent,
		                             self.myBlock.size[0] - (2 * self.indent),
		                             self.myBlock.size[1] - (2 * self.indent))
		pygame.draw.rect(self.myBlock, (255, 0, 255), self.rectField)
		self.quantityCellsX = 0
		
		while ((self.quantityCellsX + 1) * self.PIXEL_CELL < self.rectField.width): #пока число клеток умноженное на её размер меньше длинный поля
			self.quantityCellsX += 1
		
		self.quantityCellsY = 0
		
		while ((self.quantityCellsY + 1) * self.PIXEL_CELL < self.rectField.height): #пока число клеток умноженное на её размер меньше ширины поля
			self.quantityCellsY += 1
			
		rectInnerX = int(self.rectField.width -
		                 (self.quantityCellsX * self.PIXEL_CELL))/2 + self.rectField.x
		rectInnerY = int(self.rectField.height -
		                 (self.quantityCellsY * self.PIXEL_CELL))/2 + self.rectField.y
		
		self.mainRect = pygame.Rect(rectInnerX, rectInnerY,
		                            (self.quantityCellsX * self.PIXEL_CELL),
		                            (self.quantityCellsY * self.PIXEL_CELL))
		pygame.draw.rect(self.myBlock, (0, 100, 100), self.mainRect)
		
		
	def get_new_anchorPoint_on_coordin(self, coord: Coord):
		return (self.mainRect.left + (self.PIXEL_CELL * coord.x),
		        self.mainRect.top + (self.PIXEL_CELL * coord.y))
		
	
	def add_new_DrawObj(self, drawnObj):
		self.myBlock.add_new_DrawObj(drawnObj)

	# def draw_cells(self):
	# 	rect = self.rectField
	# 	cellsSize = PIXEL_CELL
	# 	indent = 10
	# 	rLeft = rect.left + indent
	# 	rRight = rect.right + indent
	# 	rTop = rect.top + indent
	# 	rBottom = rect.bottom + indent
	# 	for line in range(self.allCellsInW):
	# 		pygame.draw.line(self.block,
	# 		                 (255, 255, 255),
	# 		                 (rLeft + line * cellsSize, rTop),
	# 		                 (rLeft + line * cellsSize, rBottom - indent*2),
	# 		                 1)
	#
	# 	for line in range(self.allCellsInH):
	# 		pygame.draw.line(self.block,
	# 		                 (255, 255, 255),
	# 		                 (rLeft, rTop + line * cellsSize),
	# 		                 (rRight - indent*2, rTop + line * cellsSize),
	# 		                 1)
		