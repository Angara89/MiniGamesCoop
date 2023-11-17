from block import Block
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
	def new_obj(self, stats: Block):# метод вызываеться один раз при первом обьекте тут мы считаем отступы и шрифты относительно настроек приложения
		Stat.sizeMainFont = int(stats.size[1] / 100 * 60) # главный размер шрифта
		Stat.sizeMediumFont = int(Stat.sizeMainFont / 100 * 75) # средний размер шрифта
		Stat.sizeMiniFont = int(Stat.sizeMainFont / 100 * 50) # малый размер шрифта
		
		Stat.mainIndent = Stat.sizeMainFont  # главный отступ равен главному размеру шрифта
		
		Stat.indentFromBottom = int(Stat.sizeMainFont / 20) # получаем отступ от низа блока
		Stat.indentFromLeft = int(Stat.sizeMainFont / 10) # получаем отступ с левого края блока
		
		Stat.yCommon = int((stats.size[1] - Stat.sizeMainFont) / 2) # координата пикселей по Y ОБЩАЯ
		Stat.xCommon = Stat.sizeMainFont  # координата пикселей по X ОБЩАЯ
		
		
	
	def __init__(self,
	             stats: Block,
	             qIndent: int,
	             xSizeOnIndent: int,
	             text: str,
	             textColor:tuple,
	             sizeFont: str,
	             haveChangingText: bool = False,
	             picture: str = "___",
	             havePicture: bool = False,
	             number: float = -1,
	             haveNumber: bool = False): # огромный конструктор для настройки блока статистики
		
		if (Stat.mainIndent == -1): # если создаем первый обьект данного класса то вызываем метод ниже
			self.new_obj(stats)
			
		anchorPoint = (Stat.xCommon + qIndent * Stat.mainIndent, Stat.yCommon) # получаем опорную точку в зависимости от все отступов
		size = (xSizeOnIndent * Stat.mainIndent, Stat.sizeMainFont) # получаем размер блока в зависимости от всех констант и настрек
		
		super().__init__(blockT=stats, size=size,  aPoint=anchorPoint)
		
		if (haveChangingText == True): # пока не пригодился
			pass  # TODO написать код по изменяющемуся тексту
		
		self.text = text # запоминаем наш текст
		self.textColor = textColor # запоминаем наш цвет текста
		if (sizeFont == "mainFont"): # в зависимости от размера рифта получаем наш шрифт
			self.myFont = pygame.font.Font(r"material\FRM3216x16.ttf", Stat.sizeMainFont)
		elif (sizeFont == "mediumFont"):
			self.myFont = pygame.font.Font(r"material\FRM3216x16.ttf", Stat.sizeMediumFont)
		elif (sizeFont == "miniFont"):
			self.myFont = pygame.font.Font(r"material\FRM3216x16.ttf", Stat.sizeMiniFont)
		else:
			raise Exception("ошибка при выборе размерпа шрифта")
			
		self.havePicture = havePicture
		if (havePicture == True): # пока не приго дилось
			if (picture != "___"):
				pass #  TODO написать загрузку и работу с пикчами
			else:
				raise Exception("ошибка в передаче параметров, передали что картинка есть но путь к ней не передали")
		
		self.haveNumber = haveNumber
		if (haveNumber == True): # есил имеем число то запоминаем начальное число
			self.number = number
	
		Stat.xCommon += self.size[0] # передвигаем X на весь размер нашего блока
		self.thisSurface.fill((100, 100, 100)) # заполняем поверхность цветом
		self.print() # отображаем на блоке  текст
	
	def plus_my_number(self): # метод который инкрементирует и обновляет число у обьекта
		self.number += 1 # увеличиваем число на 1
		self.print() # обновляем всю надпись
	
	def set_my_number(self, n: int): # устанавливаем число в соответсвии с тем которое было передано в аргументах
		self.number = n
		self.print()
			
	def print(self): # обновляем всесь блок статистики
		thisText = self.text # получаем наш текст
		if (self.haveNumber == True): # если мы имеем число то наш добовляем к нашему тексту число
			thisText = self.text + str(self.number)
		
		# получаем опорную точку для текста относительно всех отступов
		textAPoint = (Stat.indentFromLeft,
		              self.size[1] - Stat.indentFromBottom - self.myFont.size("A")[1])
		
		# получаем отрендереным новые текс
		text = self.myFont.render(thisText, True, self.textColor)
		self.thisSurface.fill((0 ,0, 0, 0)) # очищаем поверхность нашего блока
		self.thisSurface.blit(text, textAPoint) # отображаем текст по опорной точке текста
