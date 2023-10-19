import pygame
from DrawnObj import DrawnObj
from coord import Coord
from Field import Field
import block



class Apple(DrawnObj):
	
	def __init__(self, field: Field, size: tuple, aPoint: tuple = (0, 0), path: str = "___"):
		super().__init__(field.myBlock, (field.PIXEL_CELL, field.PIXEL_CELL), aPoint, path)
		self.myField = field
		self.coord = (3, 1)  # TODO сделать рандомну генерацию координат
		self.anchorPoint = self.myField.get_new_anchorPoint_on_coord(self.coord)
		
		
	
