import pygame
from DrawnObj import DrawnObj
from coord import Coord
from Field import Field
import block


class Apple(DrawnObj):
	
	def __init__(self, field: Field, size: tuple, aPoint: tuple, path: str):
		block = field.myBlock
		super().__init__(block, size, aPoint, path)
		self.appleCoord = Coord(2,3) # TODO сделать рандомну генерацию координат
		self.anchorPoint = field.get_new_anchorPoint_on_coordin(self.appleCoord)
		
		
	def draw(self):
		super().draw()
