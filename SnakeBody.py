import random
import pygame
class Body:
	def __init__(self, field, x, y):
		self.snakeHead = [100, 50]
		self.field = field
		self.body = [[100, 50], [90,50], [90, 50]]
		self.snakeColor = snakeColor
		self.direction = "right"
		self.changeTo = self.direction
	
	def change_head_position(self):
		if self.direction == "RIGHT":
			self.snake_head_pos[0] += 10
		elif self.direction == "LEFT":
			self.snake_head_pos[0] -= 10
		elif self.direction == "UP":
			self.snake_head_pos[1] -= 10
		elif self.direction == "DOWN":
			self.snake_head_pos[1] += 10
			# К нулевому элементу не прибавляется переменная, неп оперенацинализации к снейкхеду позу
		
			
	def body_mech(self, score, foodPos, width, heigth):
		self.snakebody.insert(0, list(self.snakeHead))
		if (self.snakeHead[0] == foodPos[0] and self.snakeHead[1] == foodPos[1]):
			foodPos = [random.randrange(1, width/10)*10, random.randrange(1, heigth/10)*10]
			score += 1
		else:
			self.body.pop()
		return score, foodPos
	
	def draw_snake(self, surface, surfaceColor):
		surface.fill(surfaceColor)
		for pos in self.body:
			pygame.draw.rect(surface, self.surfaceColor, pygame.rect(pos[0], pos[1], 10, 10))
			
	def ChekOver(self, gameOver, wight, height):
		if any (self.snake_head_pos[0] > wight-10 or self.snake_head_pos[0] < 0, self.snake_head_pos[1]> height-10 or self.snake_head_pos[1] < 0):
			for block in self.body[1:]:
				if (block[0] == self.snake_head_pos[0] and block[1]== self.snaka_head_pos[1]):
					gameOver()
			
	