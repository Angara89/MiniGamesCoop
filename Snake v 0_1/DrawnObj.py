import pygame
from block import Block


# TODO придумать как отображать все обьекты данного класса на своем блоке
class DrawnObj: # класс родительский класс для всех "рисуемых обьектов"
	
	# конструктор который принимает блок к которому относиться наш обьект, размер и опорная точка нашего обьект
	def __init__(self, blockT: Block, size: tuple, aPoint: tuple, path: str = "___"): # если надо можно указать путь к картинке
		self.anchorPoint = aPoint # запоминаем нашу опорную точку
		self.myBlock = blockT # запоминаем наш блок
		self.size = size # запоминаем наш ращмер
		
		self.thisSurface = pygame.Surface(self.size, pygame.SRCALPHA) # создаем обьект поверхности соответствубщего размера и запоминаем
		if path != "___": # если путь передан идем в блок
			self.img = pygame.image.load(path) # загружаем картинку по пути и запоминаем
			self.img = pygame.transform.scale(self.img, self.size) # трансформируем картинку, делая её соответствующего размера и обновляем
			self.thisSurface.blit(self.img, (0, 0)) # отображаем в нулевой точке картинку на поверхности этого обьекта
			
		self.myBlock.add_new_DrawObj(self) # добавляем в  список "рисуемые обьекты" наш обьект
	
		

	
	
