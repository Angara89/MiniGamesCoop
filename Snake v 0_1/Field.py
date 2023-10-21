import pygame.rect
from coord import Coord
from DrawnObj import DrawnObj
from block import Block


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
		pygame.draw.rect(self.myBlock, (0, 255, 0), self.mainRect)
		self.thisSurface.fill((0, 255, 0))
		self.create_background()
		from Snake import Snake
		from Apple import Apple
		
		
		
		self.snake = Snake(self)
		
		self.apple = Apple(self, (self.PIXEL_CELL, self.PIXEL_CELL), path=r"material\apple_1.png")

	def is_it_a_loss(self):
		if (self.snake.head[0] == -1 or self.snake.head[1] == -1 or
			self.snake.head[0] == self.quantityCellsX or self.snake.head[1] == self.quantityCellsY):
			return True
		
		for part in self.snake.parts:
			if part == self.snake.head:
				return True

		return False
		
	def create_background(self):
		self.background = DrawnObj(self.myBlock, self.mainRect.size, self.mainRect.topleft)
		colorMain = (0, 200, 0)
		colorSub = (100, 255, 0)
		
		x, y = 0, 0
		for row in range(self.quantityCellsX):
			for col in range(self.quantityCellsY):
				x = row * self.PIXEL_CELL
				y = col * self.PIXEL_CELL
				color = colorMain if (row + col) % 2 == 0 else colorSub
				pygame.draw.rect(self.background.thisSurface, color, pygame.Rect(x, y, self.PIXEL_CELL, self.PIXEL_CELL))
			
	def get_new_anchorPoint_from_topLeft(self, coord):
		return ((self.PIXEL_CELL * coord[0]), (self.PIXEL_CELL * coord[1]))

	def is_apple_eaten(self):
		if (self.snake.head == self.apple.coord):
			self.apple.apple_is_eaten()
			self.snake.flagEatenApple = True

	def get_new_anchorPoint_on_coord(self, coord):
		return (self.mainRect.left + (self.PIXEL_CELL * coord[0]),
		        self.mainRect.top + (self.PIXEL_CELL * coord[1]))


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
		