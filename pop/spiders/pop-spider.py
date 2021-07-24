import scrapy
import string

from scrapy.loader import ItemLoader
from pop.items import PopItem

class PopSpider(scrapy.Spider):
	name = 'pop'

	custom_settings = {
        'FEED_EXPORT_FIELDS': [
            'nama',
			'gender',            
			'asalNama',
			'artiNama'
        ]
    }

	def start_requests(self):
		self.logger.info('Start request')
		sexList = ['male', 'female']
		alphabetList = list(string.ascii_lowercase)

		baseUrl = 'https://www.popmama.com/baby-name'
		
		for sex in sexList:
			for alphabet in alphabetList:
				targetUrl = baseUrl + '/' + sex + '/' + alphabet

				prodResponse = scrapy.Request(targetUrl, callback = self.parseName)
				prodResponse.meta['dont_cache'] = True

				yield prodResponse

	def parseName(self, response):
		self.logger.info('Parse')
		#rows = response.css('div.result-content li')

		#for row in rows:
		for row in response.css('div.result-content li'):
			#loader = ItemLoader(item = PopItem(), selector = row)
			#loader.add_css('nama', 'a::text')

			#nameItem = loader.load_item()
			detailUrl = row.css('a::attr(href)').get()

			#yield response.follow(detailUrl, self.parseDetail, meta = {'nameItem': nameItem})
			yield response.follow(detailUrl, self.parseDetail)
		
	def parseDetail(self, response):
		self.logger.info('Parse detail')
		#nameItem = response.meta['nameItem']

		artiNamaList = response.css('div.description > ul > li::text').extract()
				
		if (len(artiNamaList) > 0):
			for row in artiNamaList:
				self.logger.info(response.url)
				loader = ItemLoader(item = PopItem(), response = response)
				loader.add_css('nama', 'h2.h3::text')
				loader.add_value('artiNama', row)
				if (response.css('i.fa-mars')):
					loader.add_value('gender', 'Laki-laki')
				else:
					loader.add_value('gender', 'Perempuan')

				yield loader.load_item()
		else:
			self.logger.info(response.url)
			loader = ItemLoader(item = PopItem(), response = response)
			loader.add_css('nama', 'h2.h3::text')
			loader.add_value('artiNama', '')
			if (response.css('i.fa-mars')):
				loader.add_value('gender', 'Laki-laki')
			else:
				loader.add_value('gender', 'Perempuan')

			yield loader.load_item()		

		'''
		loader = ItemLoader(item = nameItem, response = response)		
		loader.add_css('artiNama', 'div.description > ul > li::text')
		if (response.css('i.fa-mars')):
			loader.add_value('gender', 'Laki-laki')
		else:
			loader.add_value('gender', 'Perempuan')
		#loader.add_value('asalNama', 'default')

		yield loader.load_item()
		'''