from  stats import Stats
from DrawnObj import DrawnObj


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
		Stat.sizeMainFont = int(self.myStats.size[1] / 100 * 80)
		Stat.sizeMediumFont = int(Stat.sizeMainFont / 100 * 75)
		Stat.sizeMiniFont = int(Stat.sizeMainFont / 100 * 50)
		
		Stat.mainIndent = Stat.sizeMainFont
		
		Stat.indentFromBottom = int(Stat.sizeMainFont / 20)
		Stat.indentFromLeft = int(Stat.sizeMainFont / 10)
		
		Stat.yCommon = int((self.size[1] - Stat.sizeMainFont) / 2)
		Stat.xCommon = Stat.sizeMainFont
		
		
	
	def __init__(self, stats: Stats, qIndent: int, xSizeOnIndent: int, text: str, textColor:tuple,
	             sizeFont: str, picture: str = "___", havePicture: bool = 0, number: float = -1, haveNumber: bool = 0):
		self.myStats = stats
		if (Stat.mainIndent == -1):
			self.new_obj()
		anchorPoint = (Stat.xCommon + qIndent * Stat.mainIndent, Stat.yCommon)
		size = (xSizeOnIndent * Stat.mainIndent, Stat.sizeMainFont)
		
		super().__init__(blockT=stats, size=size,  aPoint=anchorPoint)
		
		self.text = text
		self.textColor =textColor
		self.sizeFont = sizeFont
		self.havePicture = havePicture
		if (havePicture == True):
			if (picture != "___"):
				pass #  TODO написать загрузку и работу с пикчами
			else:
				raise Exception("ошибка в передаче параметров, передали что картинка есть но путь к ней не передали")
		self.haveNumber = haveNumber
		if (haveNumber == True):
			self.number = number