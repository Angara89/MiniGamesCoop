from  stats import Stats
from DrawnObj import DrawnObj
import pygame

class Stat(DrawnObj):
	mainIndent = -1

	sizeMainFont = -1
	sizeMiniFont = -1
	sizeMediumFont = -1
	indentFromBottom = -1
	indentFromLeft = -1
	
	yCommon = -1
	xCommon = -1
	def new_obj(self):
		Stat.sizeMainFont = int(self.myStats.size[1] / 100 * 70)
		Stat.sizeMediumFont = int(Stat.sizeMainFont / 100 * 75)
		Stat.sizeMiniFont = int(Stat.sizeMainFont / 100 * 50)
		
		Stat.mainIndent = Stat.sizeMainFont
		
		Stat.indentFromBottom = int(Stat.sizeMainFont / 20)
		Stat.indentFromLeft = int(Stat.sizeMainFont / 10)
		
		Stat.yCommon = int((self.myStats.size[1] - Stat.sizeMainFont) / 2)
		Stat.xCommon = Stat.sizeMainFont
		
		
	
	def __init__(self,
	             stats: Stats,
	             qIndent: int,
	             xSizeOnIndent: int,
	             text: str,
	             textColor:tuple,
	             sizeFont: str,
	             haveChangingText: bool = False,
	             picture: str = "___",
	             havePicture: bool = False,
	             number: float = -1,
	             haveNumber: bool = False):
		
		self.myStats = stats
		if (Stat.mainIndent == -1):
			self.new_obj()
		anchorPoint = (Stat.xCommon + qIndent * Stat.mainIndent, Stat.yCommon)
		size = (xSizeOnIndent * Stat.mainIndent, Stat.sizeMainFont)
		
		super().__init__(blockT=stats, size=size,  aPoint=anchorPoint)
		
		if (haveChangingText == True):
			pass  # TODO написать код по изменяющемуся тексту
		
		self.text = text
		self.textColor = textColor
		if (sizeFont == "mainFont"):
			self.myFont = pygame.font.Font(r"material\FRM3216x16.ttf", Stat.sizeMainFont)
		elif (sizeFont == "mediumFont"):
			self.myFont = pygame.font.Font(r"material\FRM3216x16.ttf", Stat.sizeMediumFont)
		elif (sizeFont == "miniFont"):
			self.myFont = pygame.font.Font(r"material\FRM3216x16.ttf", Stat.sizeMiniFont)
		else:
			raise Exception("ошибка при выборе размерпа шрифта")
			
		self.havePicture = havePicture
		if (havePicture == True):
			if (picture != "___"):
				pass #  TODO написать загрузку и работу с пикчами
			else:
				raise Exception("ошибка в передаче параметров, передали что картинка есть но путь к ней не передали")
		
		
		self.haveNumber = haveNumber
		if (haveNumber == True):
			self.number = number
			
			
			
			
		Stat.xCommon += self.size[0]
		self.thisSurface.fill((100, 100, 100))
		self.print()
	
	def plus_my_number(self):
		self.number += 1
		self.print()
			
	def print(self):
		thisText = self.text
		if (self.haveNumber == True):
			thisText = self.text + str(self.number)
		
		textAPoint = (Stat.indentFromLeft,
		              self.size[1] - Stat.indentFromBottom - self.myFont.size("A")[1])
		text = self.myFont.render(thisText, True, self.textColor)
		# self.thisSurface.fill((0, 100, 255, 128))
		self.thisSurface.fill((0 ,0, 0, 50))
		self.thisSurface.blit(text, textAPoint)
