import pygame
import DrawnObj
import coord
import Field
import block


class Apple(DrawnObj.DrawnObj):
	
	def __init__(self, field: Field.Field, size: tuple, aPoint: tuple, path: str):
		super().__init__(field, size, aPoint, path)
		self.appleCoord = coord.Coord(2,3) # TODO сделать рандомну генерацию координат
		
	def get_new_anchorPoint(self, coord: coord.Coord):
		indent = self.myBlock.anchorPoint
		
	def draw(self):
		super().draw()
