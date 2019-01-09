
from agedBrie import *
from sulfuras import *
from backstage import *

class Gildedrose():

    def __init__(self, stock):
        self.stock = stock

    def getItem(self):
        return self.stock

    def actualizarItem(self):
        for objeto in stock:
            objeto.update_quality()


if __name__ == "__main__":

    stock = [AgedBrie("paquito",-5,40), Backstage(
        "Backstage", 10, 30), Sulfuras("Sulfuras", 60, 10)]
    
    tienda = Gildedrose(stock)
    tienda.actualizarItem()
    assert tienda.getItem()[0].getQuality() == 42
    assert tienda.getItem()[1].getQuality() == 32
    assert tienda.getItem()[2].getQuality() == 10
