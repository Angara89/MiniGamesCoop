import DrawnObj

class Snake(DrawnObj.DrawnObj):
	
	def __init__(self):
		self.coord = (0, 0)
		self.coodrBody = []
		