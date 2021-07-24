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

class DataParseSavePipeline(object):
    def __init__(self):
        logging.info("****Data saving****")
        
        # Initializes database connection and sessionmaker
        engine = dbConnect()
        # Creates table
        createTable(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****Database connected****")

    def process_item(self, item, spider):

        def splitArtiNama(x):
            text = x.split(';')

            return text

        adapter = ItemAdapter(item)
        session = self.Session()

        name = Name()

        if adapter.get('artiNama'):
            # split artiNama into several part using semicolon
            #name.artiNama = item['artiNama']
            #for x in splitArtiNama(item['artiNama']):
            y = item['artiNama'].split(':')

            name.nama = item['nama']
            name.gender = item['gender'][0]
            name.artiNama = y[0]
            name.asalNama = y[1].lstrip()

            try:
                session.add(name)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()            
        else:
            name.nama = item['nama']            
            name.gender = item['gender'][0]
            name.asalNama = ''
            name.artiNama = ''

            try:
                session.add(name)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()    
        '''
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
        '''

        return item