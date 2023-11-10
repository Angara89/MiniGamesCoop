import time

import pygame
import sys

class Surface:
	def __init__(self):
		self.white = pygame.Color(255, 255, 255)
		self.yellow = pygame.Color(255, 255, 102)
		self.blue = pygame.Color(121, 197, 216)
		self.red = pygame.Color(181, 65, 111)
		self.black = pygame.Color(0, 0, 0)
		self.green = pygame.Color(0, 255, 0)
		
		self.disWight = 1920
		self.disHeight = 1080
		self.score = 0
		
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
	def score(self, choice=1):
		s_font = pygame.font.SysFont("Monaco", 24)
		s_surf = s_font.render('Score: {0}'.format(self.score), True, self.black)
		s_rect = s_surf.get_rect()
		if choice == 1:
			s_rect.midtop = (80, 10)
		else:
			s_rect.midtop = (360, 120)
			
		self.playSurface.blit(s_surf, s_rect)
		
	def game_over(self):
		goFont = pygame.font.SysFont('monaco', 72)
		goSurf = goFont.render('Game over', True, self.red)
		goRect = goSurf.get_rect()
		goRect.midtop = (360, 15)
		self.playSurface.blit(goSurf, goRect)
		self.score=0
		pygame.display.flip()
		time.sleep(3)
		pygame.quit()
		sys.exit()

			
