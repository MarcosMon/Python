from regularItem import RegularItem

class Sulfuras(RegularItem):

	def update_quality(self):
		if self.sell_in >0:
			self.setQuality(0)
		else:
			self.setQuality(0)
			


if __name__ == "__main__":


	miSulfura= Sulfuras("Sulfuras", 100, 40)

	miSulfura.update_quality()

	assert miSulfura.getQuality() == 40
	assert miSulfura.getSell_in() == 100
	