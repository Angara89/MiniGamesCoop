from DrawnObj import DrawnObj
import pygame
class Snake():
	
	def __init__(self):
		self.head = (0, 0)
		self.tail = (0, 0)
		self.parts = []
	
	def __init__(self, head: tuple, tail: tuple, PIXEL_CELL: int):
		self.myDirection = "DOWN"
		self.head = head
		self.tail = tail
		self.parts = []
		self.imgHead = pygame.image.load(r"material\snake_head.png")
		self.imgHead = pygame.transform.scale(self.imgHead, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgPart = pygame.image.load(r"material\snake_part.png")
		self.imgPart = pygame.transform.scale(self.imgPart, (PIXEL_CELL, PIXEL_CELL))
		
		self.imgTail = pygame.image.load(r"material\sneak_last_part.png")
		self.imgTail = pygame.transform.scale(self.imgTail, (PIXEL_CELL, PIXEL_CELL))