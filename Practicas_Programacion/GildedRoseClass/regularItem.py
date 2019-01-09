from item import Item
from updatable import Updatable
class RegularItem(Item,Updatable):

	def setSell_in(self):
		self.sell_in-=1

	def setQuality(self,valor):
		if self.quality + valor >50:
			self.quality = 50
		elif self.quality + valor >=0:
			self.quality += valor
		else:
			self.quality = 0

	def update_quality(self):
		if self.sell_in >0:
			self.setQuality(-1)
		else:
			self.setQuality(-2)
		self.setSell_in()
		





if __name__ == "__main__":

	miRegularitem=RegularItem("Sanoque", 100, 15)
	miRegularitem.update_quality()
	assert miRegularitem.getQuality() == 14
	assert miRegularitem.getSell_in() == 99

	miRegularitem1=RegularItem("Ezequiel", 100, 55)
	miRegularitem1.update_quality()
	assert miRegularitem1.getQuality() == 50
	assert miRegularitem1.getSell_in() == 99

	miRegularitem2=RegularItem("Sanbernardino", -2 , 30)
	miRegularitem2.update_quality()
	assert miRegularitem2.getSell_in() == -3
	assert miRegularitem2.getQuality() == 28

	miRegularitem3=RegularItem("MazaHelada", 20, -2)
	miRegularitem3.update_quality()
	assert miRegularitem3.getSell_in() ==19
	assert miRegularitem3.getQuality() == 0




