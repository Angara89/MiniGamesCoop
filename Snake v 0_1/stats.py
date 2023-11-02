from DrawnObj import DrawnObj
from block import Block
import pygame



# FRM325x8 FRM325x16

class Stats(Block):
	def __init__(self, size: tuple, anchorPoint: tuple):
		super().__init__(size, anchorPoint)