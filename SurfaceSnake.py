class Surface():
	def __int__(self, width, height):
		self.width = width
		self.height = height
		self.grid = [[0 for 800 in range(width) ] for 600 in range(height)]
		
	def setFood(self, x, y):
		self.grid[x][y] = 1
		
	def setObstacle(self, x, y):
		set.grid[x][y] = 2
		
	def setSnake(self, x, y):
		set.grid[x][y] = 3
		
	def clearCell(self, x, y):
		set.grid[x][y] = 0
		
	def printSurface(self):
		for row in self.grid:
			print("". join(str(cell) for cell in row))