# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

from sqlalchemy.orm import sessionmaker
from itemadapter import ItemAdapter
from pop.models import Name, dbConnect, createTable

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


class DataSavePipeline(object):
    def __init__(self):
        logging.info("****Data saving****")

        """
        Initializes database connection and sessionmaker
        Creates tables
        """

        engine = dbConnect()
        createTable(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****Database connected****")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        session = self.Session()
        name = Name()

        if adapter.get('nama'):            
            name.nama = item['nama']

        if adapter.get('gender'):            
            name.gender = item['gender'][0]
        
        if adapter.get('asalNama'):
            name.asalNama = item['asalNama'][0]
        else:
            name.asalNama = ''

        if adapter.get('artiNama'):
            name.artiNama = item['artiNama']
        else:       
            name.artiNama = ''

        try:
            session.add(name)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item