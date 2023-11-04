import time

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
		self.playSurface = pygame.display.set_mode((self.disWight, self.disHeight))
		pygame.display.set_caption("Stradivarius Snake")
		
	def event_loop(self, change_to):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key == ord('d'):
					change_to = "RIGHT"
				elif event.key == pygame.K_LEFT or event.key == ord('a'):
					change_to = "LEFT"
				elif event.key == pygame.K_UP or event.key == ord('w'):
					change_to = "UP"
				elif event.key == pygame.K_DOWN or event.key == ord('s'):
					change_to = "DOWN"
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
		return change_to
	
	def refresh_screen(self):
		pygame.display.flip()
		self.fpsControl = pygame.time.Clock(30)
	def show_score(self, choice=1):
		sFront = pygame.front.SysFront("Monaco", 24)
		sSurf = sFront.render('Score: {0}'.format(self.score), True, self.black)
		sRect = sSurf.get_rect()
		if choice == 1:
			sRect.midtop = (80, 10)
		else:
			sRect.midtop = (360, 120)
			
		self.playSurface.blit(sSurf, sRect)
		
	def game_over(self):
		goFont = pygame.font.SysFont('monaco', 72)
		goSurf = goFont.render('Game over', True, self.red)
		goRect = goSurf.get_rect()
		goRect.midtop = (360, 15)
		self.playSurface.blit(goSurf, goRect)
		self.show_score(0)
		pygame.display.flip()
		time.sleep(3)
		pygame.quit()
		sys.exit()

			
