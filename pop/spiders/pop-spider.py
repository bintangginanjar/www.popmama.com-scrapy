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
			'asalBahasa',
			'artiNama'
        ]
    }

	def start_requests(self):
		sexList = ['male', 'female']
		alphabetList = list(string.ascii_lowercase)

		baseUrl = 'https://www.popmama.com/baby-name'
		
		for sex in sexList:
			for alphabet in alphabetList:
				targetUrl = baseUrl + '/' + sex + '/' + alphabet

				prodResponse = scrapy.Request(targetUrl, callback = self.parse)
				prodResponse.meta['dont_cache'] = True

				yield prodResponse

	def parse(self, response):
		rows = response.css('div.result-content li')		

		for row in rows:
			loader = ItemLoader(item = PopItem(), selector = row)
			loader.add_css('nama', 'a::text')

			nameItem = loader.load_item()
			detailUrl = row.css('a::attr(href)').get()

			yield response.follow(detailUrl, self.parseDetail, meta = {'nameItem': nameItem})
		

	def parseDetail(self, response):
		nameItem = response.meta['nameItem']

		loader = ItemLoader(item = nameItem, response = response)		
		loader.add_css('artiNama', 'div.description > ul > li::text')
		if (response.css('i.fa-mars')):
			loader.add_value('gender', 'laki-laki')
		else:
			loader.add_value('gender', 'perempuan')

		yield loader.load_item()