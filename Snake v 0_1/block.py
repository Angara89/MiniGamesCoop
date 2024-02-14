import pygame


class Block(pygame.Surface): # наследуемся от данного класса, так как класс block обертка для surface, у которого есть своя опорная точка
	def __init__(self, size: tuple, anchorPoint: tuple): # передаем конструктору размер и опорную точку
		# вызываем супер метод родительского класса surface передавая размер в ширину и высоту, и делаем возможность альфа канала
		super().__init__(size,  pygame.SRCALPHA)
		self.size = size  # присваеваем размер в тьюпле в пикселях
		self.anchorPoint = anchorPoint  # присваеваем опорную точку (левый верхний угол)
		self.myDrawnObjs = []  # создаем список рисуемых обьектов для метода draw_all_DrawnObj
	
	def draw_all_DrawnObj(self): # метод для обнавления изображения на данном блоке
		self.fill((0, 0, 0, 0)) # заливаем всю поверхность блока "прозрачным" цветом
		for drawnObj in self.myDrawnObjs: # для каждого "рисуемого" обьекта делаем следующее
			self.blit(drawnObj.thisSurface, drawnObj.anchorPoint) # отображаем на себе поверхность "рисуемого обьекта" по его anchorPoint

	
	def add_new_DrawObj(self, drawnObj): # метод для добавления нового обьекта в наш списко таких обьектов
		self.myDrawnObjs.append(drawnObj)
	
	def get_anchorPoint(self): # простой гетор вовзращающий нашу опорную точку
		return self.anchorPoint