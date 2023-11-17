import pygame
from DrawnObj import DrawnObj
from block import Block
INDENT_TO_BORDER_FIELD = 10

class Field(DrawnObj):
	# класс "поля" нужен для взаимодействия "яблока" "змии" "поля" "барьеров" и тд
	# в нем все создаеться и все контролируеться через него



	# конструктор в который передаеться скорость и блок к которому относиться поле и собственно все в данном классе
	def __init__(self, tBlock: Block, speed, pixCell = 60):
		super().__init__(tBlock, tBlock.size, (0, 0)) # вызываем конструктор "рисуемого обьекта" передавая блок и делаем размеров у поля в весь блок к которому мы относимся, таке рисуем в нулевой точки
		self.barriers = [] # инициализируем список барьеров
		self.PIXEL_CELL = pixCell # устанавливаем размер клетки константой в 60 пикселей если не передано другого
		self.indent = int(self.myBlock.size[1] / 100)  # делаем отступы  в 1 процент от высоты и приводим к целому числу
		
		# присваеваем rect обьект в точке равной отступу по x y
		# шириной и длинной для каждого минус двойные отступы(так как отступы существуют с двух сторон)
		# получаем квадрат с отступами в 1 процент по все сторонам
		self.rectField = pygame.Rect(self.indent, self.indent,
		                             self.myBlock.size[0] - (2 * self.indent),
		                             self.myBlock.size[1] - (2 * self.indent))
		
		self.quantityCellsX = int(self.rectField.width / self.PIXEL_CELL) # узнаем количество "клеток" (cells) по Х
		self.quantityCellsY = int(self.rectField.height / self.PIXEL_CELL) # узнаем количество "клеток" (cells) по Y
		
		# узнаем X опорной точки внутреннего прямоугольника
		rectInnerX = int(self.rectField.width - (self.quantityCellsX * self.PIXEL_CELL))/2 + self.rectField.x
		# узнаем Y опорной точки внутреннего прямоугольника
		rectInnerY = int(self.rectField.height - (self.quantityCellsY * self.PIXEL_CELL))/2 + self.rectField.y
		
		# создаем главный прямоугольник в котором в котором соблюдены все отступы
		# также он создан с учетом того что все "клетки" поместяться в нем и сам прямоугольник будет отцентрован
		self.mainRect = pygame.Rect(rectInnerX, rectInnerY,
		                            (self.quantityCellsX * self.PIXEL_CELL),
		                            (self.quantityCellsY * self.PIXEL_CELL))
		
		# создаем текстуру для поля, сначало создаем поверхность во все полу
		self.pictureField = DrawnObj(self.myBlock, self.myBlock.size, (0, 0))
		img = pygame.image.load(r"material\stone_texture_1.jpg") # загружаем текстуру и запоминаем её
		img = pygame.transform.scale(img, self.myBlock.size) # трансформируем  текстуру в размер всего блока и запоминаем
		t = pygame.Surface(self.myBlock.size, pygame.SRCALPHA) # создаем временную текстурку размером с блок с альфо каналом
		GREY = 0
		t.fill((GREY, GREY, GREY, 200)) # заливаем определенным цветом временную поверхность
		img.blit(t, (0, 0)) # отображам эту временую поверхность в нулевой опорной точке
		self.pictureField.thisSurface.blit(img, (0, 0)) # отображаем на нашей текстурку за полем в нулевых координатах наше обработаное изображение
		
		self.create_background() # вызываем метод для задачи обьемности внутри "поля"
		
		from Snake import Snake # распаковываем класс змеи в наш класс
		self.snake = Snake(self, speed=speed) # создаем змею, передавая её скорость и запоминаем её
		
		from Apple import Apple # распаковываем класс яблока в наш класс
		self.apples = [] # создаем список яблок
		for _ in range(1): # цикл для нескольких ябллок
			# добовляем в список яблок яблока передвая в конструктор яблока "поле"(себя), размер в одну "клетку" и картинку яблока
			self.apples.append(Apple(self, (self.PIXEL_CELL, self.PIXEL_CELL), path=r"material\apple_1.png"))
			
			
		self.borders_field() # создаем красивую границу для поля

		

	def borders_field(self): # создаем границы поля, грубо говоря создаем границу у mainRect
		# создаем "рисуемый обьект" границ на нашем блоке размером с mainRect в опорной точке mainRect
		self.borders = DrawnObj(blockT=self.myBlock, aPoint=self.mainRect.topleft, size=self.mainRect.size)
		board = pygame.Surface(size=self.mainRect.size, flags=pygame.SRCALPHA) # создаем временый обьект поверхности размером mainRect
		board.fill(((17, 55, 13, 240))) # заливаем цветом нашу временную поверхность
		tIndent = self.PIXEL_CELL / 10 # получаем грубо говоря размер наших границ
		# отображаем пустое поле чуть внутри нашего board, тем самым создав границы
		pygame.draw.rect(
			board,
			(0, 0, 0, 0),
			pygame.Rect(
				tIndent,
				tIndent,
				self.mainRect.width-tIndent * 2,
				self.mainRect.height - tIndent*2
			)
		) # отображаем на нашем board (временной поверхности) прямоуголник(внутрений по отношщению к board) цветом прозрачности
		self.borders.thisSurface.blit(board, (0, 0)) # отоброжаем наш временый на поврхности "поля" в нулевой точки

	
	
	
	def is_it_a_loss(self): # метод проверяющие находиться ли змейка в проигрошном положении
		# проверяет выход координат головы за границы поля
		if (self.snake.head[0] == -1 or self.snake.head[1] == -1 or
			self.snake.head[0] == self.quantityCellsX or self.snake.head[1] == self.quantityCellsY):
			return True
		
		for part in self.snake.parts: # для каждой части змейки проверяет
			if part == self.snake.head: # если голова находиться в своей части (хвосте) то венуть True
				return True
			for barrier in self.barriers: # для каждого барьера в списке барьеров проверяем
				if part == barrier.coord: # если часть змейки в координатах барьера то вернуть True
					return True
		return False # если все проверки пройденны вернуть Fasle, это не проигрыш в этом шаге
		
	def create_background(self): # создаем фон для клеток основного поля
		self.background = DrawnObj(self.myBlock, self.mainRect.size, self.mainRect.topleft) # создаем "рисуемый обьект" фона
		alphaChanel = 240 # альфа канал для цветов
		colorMain = (107, 157, 41, alphaChanel) # запоминаем цвет
		colorSub = (83, 114, 43, alphaChanel) # запоминаем цвет
		img = pygame.image.load(r"material\grass_3.jpg") # загружаем изображение фона
		img = pygame.transform.scale(img, self.mainRect.size) # трансформируем изображение фона размером в главный прямоугольник и запоминаем его
		
		tSur = pygame.Surface(self.mainRect.size, pygame.SRCALPHA) # создаем временную поверхность с альфа каналом размером в главный прямоугольик
		for row in range(self.quantityCellsX): # для каждой строки длинной в количесво клеток в Х
			for col in range(self.quantityCellsY): # для каждой строки длинной в количесво клеток в Х65
				x = row * self.PIXEL_CELL # получаем Х опорной точки данной итерации
				y = col * self.PIXEL_CELL # получаем Y опорной точки данной итерации
				color = colorMain if (row + col) % 2 == 0 else colorSub # выбираем цвет блока, если четный то  colorMain иначе colorSub
				pygame.draw.rect(tSur, color, pygame.Rect(x, y, self.PIXEL_CELL, self.PIXEL_CELL)) # рисуем квадрат на временной поверхности соответстующих параметров

		self.background.thisSurface.blit(img, (0, 0)) # отображаем на поверхности фона отредактированную картинку картинку
		self.background.thisSurface.blit(tSur, (0, 0)) # отображаем на поверхности фона временую поверхность с клетками
		
		
			
	def get_new_anchorPoint_from_topLeft(self, coord): # возвращает опорную точку в пикселях принимая координаты
		# для каждой коориднаты просто умножаем её на константу "PIXELL_CELL" которая отвечает за размер одной клетки
		return ((self.PIXEL_CELL * coord[0]), (self.PIXEL_CELL * coord[1]))

	def is_apple_eaten(self): # метод проверяющий седенно ли яблокок
		for apple in self.apples: # для каждого яблока в списке яблок
			if (self.snake.head == apple.coord): # если координаты яблока равны координатам головы выполняем
				apple.apple_is_eaten() # вызываем метод у яблокок что оно сьедено
				self.stat_block_quantity_snake.plus_my_number() # в блоке статистики длины змейки увеличиваем число вызывая метод у этой статистики
				self.myStats.new_points() # у другого блока статистики вызываем метод обнуления счетчика очков
				self.snake.flagEatenApple = True  # ставим фалг змейки что яблоко сьедено (нужно чтобы при передвижении змейка увеличилась на 1 блок

	def get_new_anchorPoint_on_coord(self, coord): # метод возвращающий новуюу опорную точку в зависимости от координат, от опорной точки главного прямоугольника
		return (self.mainRect.left + (self.PIXEL_CELL * coord[0]),
		        self.mainRect.top + (self.PIXEL_CELL * coord[1]))

	
	
	def set_stats_block(self, stats): # запоминаем блок статистик
		from stats import Stats
		self.myStats = stats
	def add_stat_block_quantity_snake(self, stat): # запоминаем блок статистики по дланне змейки
		from stat_ import Stat
		self.stat_block_quantity_snake = stat
		