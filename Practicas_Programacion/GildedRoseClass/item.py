class Item():

	def __init__(self,name,sell_in,quality):

		self.name = str(name)
		self.sell_in = int(sell_in)
		self.quality = int(quality)

	def getName(self):

		return self.name

	def getSell_in(self):

		return self.sell_in

	def getQuality(self):
		
		return self.quality

	def __repr__(self):
		
		return "El nombre del item es %s, Tiene %s días restantes para su venta, y su calidad es de %s" % (self.getName(),self.getSell_in(),self.getQuality())





if __name__ == "__main__":

	miItem=Item("Selfulo",80,20)
	assert miItem.getName() == "Selfulo"
	assert miItem.getSell_in() == 80
	assert miItem.getQuality() == 20

