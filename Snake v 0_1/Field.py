import pygame
from DrawnObj import DrawnObj
from block import Block
INDENT_TO_BORDER_FIELD = 10

class Field(DrawnObj):
	
	
	
	def __init__(self, tBlock: Block, speed):
		self.barriers = []
		self.PIXEL_CELL = 60
		super().__init__(tBlock, tBlock.size, (0, 0))
		self.indent = int(self.myBlock.size[1] / 100)  # делаем отступы для рамки в 1 процент от высоты
		# присваеваем rect обьект в точке отступов,  шириной и длинной минус двойные отступы(так как отступы существуют с двух сторон
		self.rectField = pygame.Rect(self.indent, self.indent,
		                             self.myBlock.size[0] - (2 * self.indent),
		                             self.myBlock.size[1] - (2 * self.indent))
		# pygame.draw.rect(self.myBlock, (255, 0, 255), self.rectField)
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
		
		
		
		self.pictureField = DrawnObj(self.myBlock, self.myBlock.size, (0, 0))
		
		img = pygame.image.load(r"material\stone_texture_1.jpg")
		img = pygame.transform.scale(img, self.myBlock.size)
		
		# self.pictureField = DrawnObj(self.myBlock, self.myBlock.size, (0, 0), path=r"material\grass_1.jpg")
		t = pygame.Surface(self.myBlock.size, pygame.SRCALPHA)
		GREY = 0
		t.fill((GREY, GREY, GREY, 200))
		img.blit(t, (0, 0))
		# self.pictureField.thisSurface.fill()
		self.pictureField.thisSurface.blit(img, (0, 0))
		# self.thisSurface.fill((0, 100, 0, 0))
		self.create_background()
		from Snake import Snake
		from Apple import Apple
		
		self.snake = Snake(self, speed=speed)
		self.apples = []
		for _ in range(1):
			self.apples.append(Apple(self, (self.PIXEL_CELL, self.PIXEL_CELL), path=r"material\apple_1.png"))
			
		self.myBlock.fill((0, 0, 0, 0))
		
		self.borders_field()


	def borders_field(self):
		self.borders = DrawnObj(blockT=self.myBlock, aPoint=self.mainRect.topleft, size=self.mainRect.size)
		board = pygame.Surface(size=self.mainRect.size, flags=pygame.SRCALPHA)
		board.fill(((17, 55, 13, 240)))
		tIndent = self.PIXEL_CELL / 10
		pygame.draw.rect(
			board,
			(0, 0, 0, 0),
			pygame.Rect(
				tIndent,
				tIndent,
				self.mainRect.width-tIndent * 2,
				self.mainRect.height - tIndent*2
			)
		)
		
		self.borders.thisSurface.blit(board, (0, 0))
		# self.borders.thisSurface.fill((0, 0, 0, 240))
	
	
	
	def is_it_a_loss(self):
		if (self.snake.head[0] == -1 or self.snake.head[1] == -1 or
			self.snake.head[0] == self.quantityCellsX or self.snake.head[1] == self.quantityCellsY):
			return True
		
		for part in self.snake.parts:
			if part == self.snake.head:
				return True
			for barrier in self.barriers:
				if part == barrier.coord:
					return True
		return False
		
	def create_background(self):
		self.background = DrawnObj(self.myBlock, self.mainRect.size, self.mainRect.topleft)
		alphaChanel = 240
		colorMain = (107, 157, 41, alphaChanel)
		# colorSub = (107, 157, 41)
		colorSub = (83, 114, 43, alphaChanel)
		img = pygame.image.load(r"material\grass_3.jpg")
		img = pygame.transform.scale(img, self.mainRect.size)
		
		x, y = 0, 0
		tSur = pygame.Surface(self.mainRect.size, pygame.SRCALPHA)
		for row in range(self.quantityCellsX):
			for col in range(self.quantityCellsY):
				x = row * self.PIXEL_CELL
				y = col * self.PIXEL_CELL
				color = colorMain if (row + col) % 2 == 0 else colorSub
				
				pygame.draw.rect(tSur, color, pygame.Rect(x, y, self.PIXEL_CELL, self.PIXEL_CELL))
				# pygame.draw.rect(self.background.thisSurface, color, pygame.Rect(x, y, self.PIXEL_CELL, self.PIXEL_CELL))
		# img.fill((0, 0, 0, 250))
		self.background.thisSurface.blit(img, (0, 0))
		self.background.thisSurface.blit(tSur, (0, 0))
		
		
			
	def get_new_anchorPoint_from_topLeft(self, coord):
		return ((self.PIXEL_CELL * coord[0]), (self.PIXEL_CELL * coord[1]))

	def is_apple_eaten(self):
		for apple in self.apples:
			if (self.snake.head == apple.coord):
				apple.apple_is_eaten()
				self.stat_block_quantity_snake.plus_my_number()
				self.myStats.new_points()
				self.snake.flagEatenApple = True

	def get_new_anchorPoint_on_coord(self, coord):
		return (self.mainRect.left + (self.PIXEL_CELL * coord[0]),
		        self.mainRect.top + (self.PIXEL_CELL * coord[1]))

	
	
	def set_stats_block(self, stats):
		from stats import Stats
		self.myStats = stats
	def add_stat_block_quantity_snake(self, stat):
		from stat_ import Stat
		self.stat_block_quantity_snake = stat
	
	
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
		