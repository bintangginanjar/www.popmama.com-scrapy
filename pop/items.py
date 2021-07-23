# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst, Join

def removeNewLine(text):
        text = text.split('\n')
        text = text[0].lstrip()

        return text

class PopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nama = Field(input_processor = MapCompose(removeNewLine), output_processor = TakeFirst())
    gender = Field()
    artiNama = Field(output_processor = Join(separator = '; '))
        
    pass
