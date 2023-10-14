import pygame
from block import Block


# TODO придумать как отображать все обьекты данного класса на своем блоке
class DrawnObj:
	
	def __init__(self, block: Block, size: tuple, aPoint: tuple, path: str):
		self.anchorPoint = aPoint
		self.myBlock = block
		self.size = size
		self.img = pygame.image.load(path) # TODO сделать загрузку изображение другого
		self.img = pygame.transform.scale(self.img, self.size)
		self.mySurface = pygame.Surface(size)
		self.myBlock.add_new_DrawObj(self.mySurface)
	
		
	def draw(self):
		self.myBlock.blit(self.mySurface, self.anchorPoint)
	
	
