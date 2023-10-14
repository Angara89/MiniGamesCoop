import pygame.rect
import coord
import DrawnObj
import block
import Apple

PIXEL_CELL = 50
INDENT_TO_BORDER_FIELD = 10

class Field(DrawnObj.DrawnObj):
	
	def __init__(self, tblock: block.Block):
		super().__init__(tblock)
		self.myBlock.myDrawnObj.append(self) # добавляем в список рисуемых обьектов блока, к которому относиться данный обьект
		self.apple = Apple.Apple()
		self.myBlock.myDrawnObj.append(self.apple)
		self.snakes = []
		self.indent = int(self.myBlock.height / 100) # делаем отступы для рамки в 1 процент от высоты
		# присваеваем rect обьект в точке отступов,  шириной и длинной минус двойные отступы(так как отступы существуют с двух сторон
		self.rectField = pygame.Rect(self.indent, self.indent, self.myBlock.width - (2 * self.indent), self.myBlock.height - (2 * self.indent))
		pygame.draw.rect(self.myBlock, (255, 255, 255), self.rectField)
		self.quantityCellsX = 0
		
		while ((self.quantityCellsX + 1) * PIXEL_CELL < self.rectField.width): #пока число клеток умноженное на её размер меньше длинный поля
			self.quantityCellsX += 1
		
		self.quantityCellsY = 0
		
		while ((self.quantityCellsY + 1) * PIXEL_CELL < self.rectField.height): #пока число клеток умноженное на её размер меньше ширины поля
			self.quantityCellsY += 1
			
		rectInnerX = int(self.rectField.width - (self.quantityCellsX * PIXEL_CELL))/2 + self.rectField.x
		rectInnerY = int(self.rectField.height - (self.quantityCellsY * PIXEL_CELL))/2 + self.rectField.y
		
		self.rectInner = pygame.Rect(rectInnerX, rectInnerY, (self.quantityCellsX * PIXEL_CELL), (self.quantityCellsY * PIXEL_CELL))
		pygame.draw.rect(self.myBlock, (100, 100, 100), self.rectInner)
		
		
		
		
		
	def draw_DrawnObj_by_coord(self, drawnObj: DrawnObj.DrawnObj, coord:()):
		pass

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
		