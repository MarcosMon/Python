from regularItem import RegularItem
class AgedBrie(RegularItem):

	def update_quality(self):
		if self.sell_in >0:
			self.setQuality(1)
		else:
			self.setQuality(2)
		self.setSell_in()




if __name__ == "__main__":

	##Dentro de fecha, aumenta calidad 1
	miAgedBrie=AgedBrie("Paquito", 100, 20)
	miAgedBrie.update_quality()
	assert miAgedBrie.getQuality() == 21