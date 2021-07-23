# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst, Join

class PopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #nama = Field(input_processor = MapCompose(removeNewLine), output_processor = TakeFirst())
    nama = Field()
    gender = Field()
    asalNama = Field()
    artiNama = Field(output_processor = Join(separator = '; '))
        
    pass
