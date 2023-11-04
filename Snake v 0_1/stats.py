from DrawnObj import DrawnObj
from block import Block
import pygame
from stat_ import Stat


# FRM325x8 FRM325x16

class Stats(Block):

	def __init__(self, size: tuple, anchorPoint: tuple):
		super().__init__(size, anchorPoint)
		self.points = 0
	
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