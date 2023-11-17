from DrawnObj import DrawnObj
from Field import Field
from common import FPS
import pygame
class Snake(DrawnObj):
	
	
	def __init__(self, field: Field, speed: int, path: str = "___"):
		# вызываем метод родителя и размром поверхности в весь главный прямоуголник
		super().__init__(field.myBlock, field.mainRect.size, field.mainRect.topleft, path)
		self.myField = field
		
		self.direction = "U" # по умолчанию змейка "идет" в верх
		self.head = (int(self.myField.quantityCellsX/2), int(self.myField.quantityCellsY/2)) # ставим координаты змейки по центру координат
		self.tail = (self.head[0], self.head[1] + 1) # стави хвост змейки ниже по Y на 1
		self.parts = [self.tail] # инициализируем список частей змейки хвостом
		self.tail = (self.head[0], self.head[1] + 2) # создаем новый хвост ниже прошлого еще на один
		PIXEL_CELL = self.myField.PIXEL_CELL # для удобства временно запоминаем размер клетки
		self.imgHead = pygame.image.load(r"material\snake_part_5.png") # загружаем изображение змейки и запоминаем
		self.imgHead = pygame.transform.scale(self.imgHead, (PIXEL_CELL, PIXEL_CELL)) # скалируем изображение в соответствии с размером блока
		
		self.imgPart = pygame.image.load(r"material\snake_part_5.png") # то же самое
		self.imgPart = pygame.transform.scale(self.imgPart, (PIXEL_CELL, PIXEL_CELL)) # то же самое
		
		self.imgTail = pygame.image.load(r"material\snake_part_5.png") # то же самое
		self.imgTail = pygame.transform.scale(self.imgTail, (PIXEL_CELL, PIXEL_CELL)) # то же самое
		
		self.flagEatenApple = False # ставим что яблоко не сьедено
		
		# self.draw_snake() # рисуем змейку(старый метод)
		self.speed = speed # запоминаем скорость змейки
		self.fps = FPS # запоминаем фпс приложения
		
		self.soundStep = pygame.mixer.Sound(r"material\sound\wshuuu_1.wav") # запоминаем звук передвижения
	

		
	def step_snake(self): # шаг змейки вызываеться каждый шаг
		self.soundStep.play() # проигрывание звука шага змейки
		# self.move_snake()
		self.draw_animation() # рисование анимации передвижение змейки
	
	def draw_animation(self): # здесь мы в зависимости от скорости и фпс рисуем анимацию передвижения змейки
		clock = pygame.time.Clock() # запоминаем время
		head_surface = self.imgHead.convert_alpha() # получаем изображение головы
		part_surface = self.imgPart.convert_alpha() # получаем изображение части
		tail_surface = self.imgTail.convert_alpha() # получаем изображение хвоста
		countFrame = self.fps / self.speed # получаем количество кадров которые нам надо в данном "шаге змейки" отрисовать
		
		headPos = self.get_new_anchorPoint(self.head) # получаем текущую позицию головы
		tailPos = self.get_new_anchorPoint(self.tail) # получаем текущую позицию хвоста
		partsPos = []
		for part in self.parts: # в списке получаем текущую позицию всех частей змейки
			partsPos.append(self.get_new_anchorPoint(part))
		
		self.move_snake() # передвигаем КООРДИНАТЫ змейки на новые позиции
		
		headNeedPos = self.get_new_anchorPoint(self.head) # получаем необходимую позицию головы
		tailNeedPos = self.get_new_anchorPoint(self.tail) # получаем необходимую позицию хвоста
		partsNeedPos = []
		for part in self.parts: # получаем необходимую позицию для всего хвоста
			partsNeedPos.append(self.get_new_anchorPoint(part))
		
		partPosAndChange = [] # создаем список в котором будут храниться ТЕКУЩАЯ позиция части змейки и ИЗМЕНЕНИЯ В ОДНОМ КАДРЕ
		for i in range(len(partsPos)): # в данном цикле делаем список такого вида - list(tuple(int, int), tuple(int, int))
			# где первый тюпл это текущая опорная точка в пикселях, а второй тюпл это те изменения который мы должны применять в кадре для создания собственно анимации
			partPosAndChange.append(
				(
					partsPos[i],
					(
						int((partsNeedPos[i][0] - partsPos[i][0]) / countFrame),
						int((partsNeedPos[i][1] - partsPos[i][1]) / countFrame)
					)
				)
			)
		
		changeXT = (tailNeedPos[0] - tailPos[0]) / countFrame # изменения в одном кадре по X для хвоста
		changeYT = (tailNeedPos[1] - tailPos[1]) / countFrame # изменения в одном кадре по Y для хвоста
		
		changeX = (headNeedPos[0] - headPos[0]) / countFrame # изменения в одном кадре по X для головы
		changeY = (headNeedPos[1] - headPos[1]) / countFrame # изменения в одном кадре по Y для головы
		
		p = 0
		while p != countFrame:
			p += 1
			self.thisSurface.fill((0, 0, 0, 0)) # очищаем поверхность змейки
			
			self.thisSurface.blit(tail_surface, tailPos) # отображаем по позиции хвоста змейки её изображение
			for i in reversed(range(len(partPosAndChange))): # пробегаемся по всем частям и изменяем их позицию для каждого кадра
				self.thisSurface.blit(part_surface, partPosAndChange[i][0])
				partPosAndChange[i] = (
					(
						partPosAndChange[i][0][0] + partPosAndChange[i][1][0],
						partPosAndChange[i][0][1] + partPosAndChange[i][1][1],
					),
					partPosAndChange[i][1]
				)
			self.thisSurface.blit(head_surface, headPos) # отображаем изображение головы змейки по соответствующей позиции
			headPos = (headPos[0] + changeX, headPos[1] + changeY) # меняем позицию головы змейки
			tailPos = (tailPos[0] + changeXT, tailPos[1] + changeYT) # меняем позицию хвоста змейки
			clock.tick(self.fps) # синхронизируемся с временем по ФПС НЕ скорости, именно ФПС
			

	def move_snake(self): # в зависимости от направление змеи передвижения голову в то направление и передвижения все частей на следующего
		xChange = 0 # изменения по X в координатах
		yChange = 0 # изменения по Y в координатах
		if self.direction == "D": # изменяем соответственно напралению головы змейки её положение
			yChange += 1
		elif self.direction == "U":
			yChange -= 1
		elif self.direction == "R":
			xChange += 1
		elif self.direction == "L":
			xChange -= 1

		if self.flagEatenApple: # если на прошлом шаге было сьедено яблоко, то добавляем хвост в конец, иначе передвигаем его в последнюю часть змейки
			self.parts.append(self.tail)
		else:
			self.tail = self.parts[-1]
		self.flagEatenApple = False # по любому к этому моменту мы обработаем событие сьеденого яблока
		
		for i in reversed(range(1, len(self.parts))): # пробегаемся по частям змейки в обратном порядке
			self.parts[i] = self.parts[i - 1] # присваеваем координаты следующего
		self.parts[0] = self.head # присваеваем первой части в частях координаты головы

		self.head = (self.head[0] + xChange, self.head[1] + yChange) # меняем координаты головы в соответсующей стороной
		
	# def draw_snake(self):
	# 	# Создайте отдельные surface для каждой части змейки
	# 	head_surface = self.imgHead.convert_alpha()
	# 	part_surface = self.imgPart.convert_alpha()
	# 	tail_surface = self.imgTail.convert_alpha()
	#
	# 	# Очистите главную surface
	# 	self.thisSurface.fill((0, 0, 0, 0))
	#
	# 	# Рисуйте и перемещайте каждую часть змейки
	# 	self.thisSurface.blit(head_surface, self.get_new_anchorPoint(self.head))
	#
	# 	for part in self.parts:
	# 		self.thisSurface.blit(part_surface, self.get_new_anchorPoint(part))
	#
	# 	self.thisSurface.blit(tail_surface, self.get_new_anchorPoint(self.tail))
		
	
	def change_direction(self, dir: str): # метод для изменения направления змейки
		# проверяем чтобы нельзя было поползти назад в хвост
		if (dir == "U" and self.direction == "D") or (dir == "D" and self.direction == "U"):
			pass
		elif (dir == "R" and self.direction == "L") or (dir == "L" and self.direction == "R"):
			pass
		else:
			self.direction = dir # иначе если все хорошо то меняем направления
	
	def get_new_anchorPoint(self, coord): # получаем новую  опорную точку от координат
		return ((self.myField.PIXEL_CELL * coord[0]), (self.myField.PIXEL_CELL * coord[1]))
	
	