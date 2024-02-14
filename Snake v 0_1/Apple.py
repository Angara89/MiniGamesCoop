from DrawnObj import DrawnObj
from Field import Field
import block
import random
import pygame

class Apple(DrawnObj): # класс яблока наследуеться от "рисуемого обьекта " так как он может отображаться
	
	def __init__(self, field: Field, size: tuple, aPoint: tuple = (0, 0), path: str = "___"):
		super().__init__(field.myBlock, (field.PIXEL_CELL, field.PIXEL_CELL), aPoint, path) # вызываем метод родителя вытаскивая из поля блок, и получая размер из размера клетки из поля
		self.myField = field # запоминаем наше поля
		self.coord = self.new_random_coord() # получаем наши координаты
		self.anchorPoint = self.myField.get_new_anchorPoint_on_coord(self.coord) # получаем нашу опорную точку в пикселях от координат
		self.soundEat = pygame.mixer.Sound(r"material\sound\hhhhraaaaaammm_1.wav") # запоминаем наш звук сьедания
	
	
	def apple_is_eaten(self): # если яблоко сьедено то то поле вызывает этот метод
		self.soundEat.play() # проигрываем звук сьеденого яблока
		self.coord = self.new_random_coord() # получаем новые координаты яблока
		self.anchorPoint = self.myField.get_new_anchorPoint_on_coord(self.coord) # конвертируем координаты в опорную точку
		
	def new_random_coord(self): # метод передающий новые координаты в которые можно поставить яблоко
		flag = 0 # флаг обозначающий что координаты не найдены
		newCoord = (0, 0) # новые координаты
		while flag == 0: # пока не найдеться свободные координаты выполнять
			yq = self.myField.quantityCellsY # узнаем максимум по Y
			xq = self.myField.quantityCellsX # узнаем максимум по X
			yVar = random.randint(0, yq-1) # получаем рандомное число по y от нуля до максимума для этого числа
			xVar = random.randint(0, xq-1) # получаем рандомное число по x от нуля до максимума для этого числа
			newCoord = (xVar, yVar) # присваеваем новые координаты
			
			flag = 1 # ставим что координаты созданы
			for part in self.myField.snake.parts: # для каждой части змейки проверяем чтобы не совпадали коориднаты части и новые координаты для яблока
				if(newCoord == part):
					flag = 0
			if self.myField.snake.tail == newCoord or self.myField.snake.head == newCoord: # ули новые координаты равны хвосту змейки или голове флаг 0
				flag = 0
			for barrier in self.myField.barriers: # для каждого барьера проверяем на то чтобы координаты не были равны
				if (barrier.coord == newCoord):
					flag = 0
			
		return newCoord # вовращаем координаты