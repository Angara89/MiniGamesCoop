import DrawnObj
import coord
import block

class Apple(DrawnObj.DrawnObj):
	
	def __init__(self, block: block.Block, tup: tuple, aPoint: tuple):
		super().__init__(block, tup, aPoint)
		self.appleCoord = coord.Coord(2,3) # TODO сделать рандомну генерацию координат
		

