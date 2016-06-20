from scrapy.item import Item, Field


class Nazwy(Item):
    opis = Field()
    typ = Field()
    ilosc = Field()
