from DrawnObj import DrawnObj
from block import Block
from Field import Field

class Barrier(DrawnObj):
	
	
	def __init__(self, field: Field, coord: tuple, isMove: bool = False, moveStep: list = ["U", "U", "R", "U", "L"]):
		self.coord = coord
		aPoint = field.get_new_anchorPoint_on_coord(self.coord)
		super().__init__(field.myBlock, (field.PIXEL_CELL, field.PIXEL_CELL), aPoint)
		self.thisSurface.fill((0, 0, 0, 255))
		self.field = field
		self.field.barriers.append(self)
		self.isMove = isMove
		self.moveStep = moveStep
		self.moveStepBack = []
		self.countSteps = 0
		self.isBack = False
		self.passMove = 0
		for step in moveStep:
			if step == "U":
				self.moveStepBack.append("D")
			if step == "D":
				self.moveStepBack.append("U")
			if step == "R":
				self.moveStepBack.append("L")
			if step == "L":
				self.moveStepBack.append("R")
				
		
	def move(self):
		
		if (self.isMove != True):
			return
		
		
		if self.passMove < 3:
			self.passMove += 1
			return
		else:
			self.passMove = 0
			
		if self.countSteps == len(self.moveStep):
			self.countSteps = 0
			if self.isBack == True:
				self.isBack = False
			else:
				self.isBack = True
			
		if self.isBack == True:
			step = self.moveStepBack[self.countSteps]
		else:
			step = self.moveStep[self.countSteps]
		k = self.field.PIXEL_CELL
		if step == "U":
			self.anchorPoint = (self.anchorPoint[0], self.anchorPoint[1] - k)
		if step == "D":
			self.anchorPoint = (self.anchorPoint[0], self.anchorPoint[1] + k)
		if step == "R":
			self.anchorPoint = (self.anchorPoint[0]+ k, self.anchorPoint[1])
		if step == "L":
			self.anchorPoint = (self.anchorPoint[0]- k, self.anchorPoint[1])
		
		self.countSteps += 1