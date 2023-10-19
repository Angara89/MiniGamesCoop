import pygame
from block import Block


# TODO придумать как отображать все обьекты данного класса на своем блоке
class DrawnObj:
	
	def __init__(self, blockT, size: tuple, aPoint: tuple, path: str = "___"):
		self.anchorPoint = aPoint
		self.myBlock = blockT
		self.size = size
		
		self.thisSurface = pygame.Surface(self.size, pygame.SRCALPHA)
		if path != "___":
			self.img = pygame.image.load(path)  # TODO сделать загрузку изображение другого
			self.img = pygame.transform.scale(self.img, self.size)
			self.thisSurface.blit(self.img, (0, 0))


		self.myBlock.add_new_DrawObj(self)
	
		

	
	
