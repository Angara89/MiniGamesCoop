import pygame
from block import Block


# TODO придумать как отображать все обьекты данного класса на своем блоке
class DrawnObj:
	
	def __init__(self, blockT, size: tuple = (-1, -1), aPoint: tuple = (0, 0), path: str = "___"):
		if size[0] == -1 and size[1] == -1:
			size = blockT.size
		self.anchorPoint = aPoint
		self.myBlock = blockT
		self.size = size
		if path != "___":
			self.img = pygame.image.load(path)  # TODO сделать загрузку изображение другого
			self.img = pygame.transform.scale(self.img, self.size)
		pygame.init()
		self.mySurface = pygame.Surface(size)
		self.myBlock.add_new_DrawObj(self)
	
		
	def draw(self):
		self.myBlock.blit(self.mySurface, self.anchorPoint)
	
	
