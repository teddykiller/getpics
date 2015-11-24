# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import json
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.conf import settings
# import pymongo
from scrapy import log


class GetpicsPipeline(object):
	pass

class EncodePipeline(object):
	def process_item(self, item, spider):
		pass

class JsonWritePipeline(object):

	def __init__(self):
		self.file = open('item.json', 'wb')
	def process_item(self, item, spider):

		# for title in item['title']:
			# print title
			# item['title'] = str(title).decode('ascii').encode('utf-8')
		line = json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + '\n'
		self.file.write(line)
		# log.msg("write to json file")
		return item

class CreatFloderPipeline(object):

	def process_item(self, item, spider):
		for title in item['title']:
			os.mkdir("../pictures/" + title)
			log.msg("sucess creat folder " + title.encode('utf-8'))

		return item

class MongoWritePipeline(object):
	def __init__(self):
		host = settings['MONGODB_HOST']
		port = settings['MONGODB_PORT']
		dbName = settings['MONGODB_DBNAME']
		client = pymongo.MongoClient(host=host, port=port)
		tdb = client[dbName]
		self.post = tdb[settings['MONGODB_DOCNAME']]
	def process_item(self, item, spider):
		postInfo = dict(item)
		self.post.insert(postInfo)
		return item	
		
# class MyImagesPipeline(ImagesPipeline):

# 	def get_media_requests(self, item, info):
# 		for image_url in item['image_urls']:
# 			yield scrapy.Request(image_url)

# 	def item_completed(self, results, item, info):
# 		pass
