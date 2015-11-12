# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('gb2312')
import scrapy
from getpics.items import GetpicsItem


class MySpider(scrapy.Spider):
	name = "kook"
	allowed_domains = ["8264.com"]
	start_urls = [
		"http://www.8264.com/list/871/"
	]

	def parse(self, response):
		for sel in response.xpath('//div[@class="bbslistone"]'):
			item = GetpicsItem()
			item['image_urls'] = sel.xpath('a/img/@src').extract()
			item['image_paths'] = sel.xpath('div/a/text()').extract()
			yield item