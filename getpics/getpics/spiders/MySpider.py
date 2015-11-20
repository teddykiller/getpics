# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from getpics.items import GetpicsItem
from scrapy import log
from scrapy.http import Request


class MySpider(scrapy.Spider):
	name = "kook"
	allowed_domains = ["8264.com"]
	start_urls = [
		"http://www.8264.com/list/871/"
	]
	download_delay = 2
	def parse(self, response):
		for sel in response.xpath('//div[@class="bbslistone"]'):
			item = GetpicsItem()
			# item['image_urls'] = sel.xpath('a/img/@src').extract()[0]
			# item['image_paths'] = sel.xpath('div/a/text()').extract()[0]
			# 抓取title
			title = sel.xpath('div[@class="bbslistone_name"]/a/text()').extract()[0]
			if len(title)  == 0:
				log.msg("fecth title failed")
				continue
			item['title'] = title
			title_url = sel.xpath('a/@href').extract()[0]
			# 抓取title_url
			if len(title_url) == 0:
				log.msg("fecth title_url failed")
				continue
			item['title_url'] = title_url
			yield Request(item['title_url'], callback=self.parse_item, meta={'item':item})
			# yield item



	def parse_item(self, response):
		# 获得由parse传来的item
		item = response.meta['item']
		# 抓取image_urls
		# print response.body
		for sel in response.xpath('//div[@class="lxch_new clboth"]'):
			# item = GetpicsItem()
			image_urls = sel.xpath('//td[@class="t_f"]/img/@src').extract()
			if len(image_urls) == 0:
				log.msg("there is no pics in the topic {--" + item['title'] + '--}')
				return
			item['image_urls'] = image_urls
			yield item

		# 抓取author
		# author