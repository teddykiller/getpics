
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class GetpicsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # main page
	title = Field()
	title_url = Field()
	# second page
	subject = Field()

	author = Field()
	author_url = Field()
	image_urls = Field()
	images = Field()
