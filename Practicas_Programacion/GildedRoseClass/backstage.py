from regularItem import RegularItem
class Backstage(RegularItem):

	def update_quality(self):

		
		if self.sell_in <=10 and self.sell_in >5:
			self.setQuality(2)

		elif self.sell_in <=5 and self.sell_in >0:
			self.setQuality(3)

		elif self.sell_in  <= 0:
			self.setQuality(0)
		self.setSell_in()




if __name__ == "__main__":


	miBackstage=Backstage("Backstage",6,8)

	miBackstage.update_quality()

	assert miBackstage.getQuality()== 10


	miBackstage1=Backstage("Backstage",4,40)

	miBackstage1.update_quality()

	assert miBackstage1.getQuality()== 43

	miBackstage2=Backstage("Backstage",-2,40)

	miBackstage2.update_quality()

	assert miBackstage2.getQuality()== 40


