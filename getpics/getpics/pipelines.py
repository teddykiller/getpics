# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class GetpicsPipeline(object):
	pass

class JsonWritePipeline(object):

	def __init__(self):
		self.file = open('item.json', 'wb')
	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line)
		return item

# class MyImagesPipeline(ImagesPipeline):

#     def get_media_requests(self, item, info):
#     	for image_url in item['image_url']:
# 			yield scrapy.Request(image_url)

# 	def item_completed(self, results, item, info):
# 		image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         yield item

