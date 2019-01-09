from regularItem import RegularItem
class Backstage(RegularItem):

	def update_quality(self):
		if self.sell_in <=10:
			self.setQuality(2)
		elif self.sell_in <=5:
			self.setQuality(3)
		else:
			self.setQuality(2)
		self.setSell_in()

		






if __name__ == "__main__":


	miBackstage=Backstage("Backstage",4,8)

	miBackstage.update_quality()

	assert miBackstage.getQuality()== 10