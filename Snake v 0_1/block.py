import pygame


class Block(pygame.Surface):
	def __init__(self, size: tuple, anchorPoint: tuple):
		super().__init__(size)  # вызываем супер метод родительского класса передавая размер в ширину и высоту
		self.size = size  # присваеваем размерв тьюпле
		self.anchorPoint = anchorPoint  # присваеваем опорную точку левый верхний угол
		self.myDrawnObjs = []  # создаем список рисуемых обьектов
	
	def draw_all_DrawnObj(self):
		for drawnObj in self.myDrawnObjs:
			self.blit(drawnObj.thisSurface, drawnObj.anchorPoint)
	
	def add_new_DrawObj(self, drawnObj):
		self.myDrawnObjs.append(drawnObj)
	
	def get_anchorPoint(self):
		return self.anchorPoint

	def fill_color(self, color):
		self.fill(color)
		
		