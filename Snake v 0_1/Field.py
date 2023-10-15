import pygame.rect
from coord import Coord
from DrawnObj import DrawnObj
from block import Block
from Snake import Snake

INDENT_TO_BORDER_FIELD = 10

class Field(DrawnObj):
	
	
	
	def __init__(self, tBlock: Block):
		self.PIXEL_CELL = 30
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
		
		self.create_snake()
		self.draw_snake()
		
	def move_aPoint_snake(self, direction: str):
		xChange = 0
		yChange = 0
		if direction == "UP":
			yChange += 1
		if direction == "DOWN":
			yChange -= 1
		if direction == "RIGHT":
			xChange += 1
		if direction == "LEFT":
			xChange -= 1
		
		self.snake.tail = self.snake.parts[-1]
		
		for i in reversed(range(1, len(self.snake.parts))):
			self.snake.parts[i] = self.snake.parts[i - 1]
		self.snake.parts[0] = self.snake.head
		
		self.snake.head = (self.snake.head[0] + xChange,self.snake.head[1] + yChange)
		
		
		
		
	def create_snake(self):
		cPointHead = (int(self.quantityCellsX / 2), int(self.quantityCellsY / 2))
		cPointTail = (int(self.quantityCellsX / 2), int(self.quantityCellsY / 2) + 1)
		self.snake = Snake(cPointHead, cPointTail, self.PIXEL_CELL)
		
	def draw_snake(self):
		aPointHead = self.get_new_anchorPoint_on_coordin(self.snake.head)
		self.thisSurface.blit(self.snake.imgHead, aPointHead)
		
		aPointTail = self.get_new_anchorPoint_on_coordin(self.snake.tail)
		self.thisSurface.blit(self.snake.imgTail, aPointTail)
		
		for part in self.snake.parts:
			aPointPart = self.get_new_anchorPoint_on_coordin(part)
			self.thisSurface.blit(self.snake.imgPart, aPointPart)
	
	def get_new_anchorPoint_on_coordin(self, coord: Coord):
		return (self.mainRect.left + (self.PIXEL_CELL * coord.x),
		        self.mainRect.top + (self.PIXEL_CELL * coord.y))
		

	def get_new_anchorPoint_on_coordin(self, coord):
		return (self.mainRect.left + (self.PIXEL_CELL * coord[0]),
		        self.mainRect.top + (self.PIXEL_CELL * coord[1]))
		
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
		