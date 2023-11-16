from DrawnObj import DrawnObj
from block import Block
import pygame
from stat_ import Stat


# FRM325x8 FRM325x16

class Stats(Block):

	def __init__(self, size: tuple, anchorPoint: tuple):
		super().__init__(size, anchorPoint)
		self.points = 0
		self.borders_field()
	
	def borders_field(self):
		self.borders = DrawnObj(blockT=self, aPoint=(0, 0), size=self.size)
		board = pygame.Surface(size=self.size, flags=pygame.SRCALPHA)
		board.fill(((150, 21, 21, 230)))
		tIndent = 5
		pygame.draw.rect(
			board,
			(0, 0, 0, 0),
			pygame.Rect(
				tIndent,
				tIndent,
				self.size[0] - tIndent * 2,
				self.size[1] - tIndent * 2
			)
		)
		
		self.borders.thisSurface.blit(board, (0, 0))
	
	# self.borders.thisSurface.fill((0, 0, 0, 240))
	
	def set_pointsStat(self, stat: Stat):
		self.pointsStat = stat
		
	def set_addToPointsStat(self, stat: Stat):
		self.addToPointsStat = stat
		
	def new_points(self):
		self.pointsStat.set_my_number(self.points + self.pointsStat.number)
		self.points = 100
		self.addToPointsStat.set_my_number(self.points)
	def step_snake(self):
		self.points -= 1
		self.addToPointsStat.set_my_number(self.points)