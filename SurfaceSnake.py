import pygame
import sys

class Surface:
	def __init__(self):
		self.white = (255, 255, 255)
		self.yellow = (255, 255, 102)
		self.blue = (121, 197, 216)
		self.red = (181, 65, 111)
		self.black = (0, 0, 0)
		self.green = (0, 255, 0)
		
		self.disWight = 800
		self.disHeight = 600
		
	def chek_errors(self):
		checkErrors = pygame.init()
		if checkErrors[1]> 0:
			sys.exit()
		else:
			print("Ok")
			
	def Set_surface(self):
		self.playSurface = pygame.display.set_mode(self.disWight, self.disHeight)
		
	def show_score(self, choice=1):
		sFront = pygame.front.SysFront("Monaco", 24)
		sSurf = sFront.render('Score: {0}'.format(self.score), True, self.black)
		sRect = sSurf.get_rect()
		if choice == 1:
			sRect.midtop = (80, 10)
		else:
			sRect.midtop = (360, 120)
			
		self.playSurface.blit(sSurf, sRect)
		

			
