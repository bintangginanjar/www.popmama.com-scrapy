# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

from itemadapter import ItemAdapter

class DataCleanPipeline(object):
    def __init__(self):		
        logging.info("****Data cleaning****")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        def getCleanName(text):
            text = text.split('\n')
            text = text[0].lstrip()

            return text

        if adapter.get('nama'):
            item['nama'] = getCleanName(item['nama'][0])

        return item


class DataParsePipeline(object):
    def __init__(self):
        logging.info("****Data parsing****")