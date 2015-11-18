# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import pymongo


class GetpicsPipeline(object):
	pass

class EncodePipeline(object):
	def process_item(self, item, spider):
		pass

class JsonWritePipeline(object):

	def __init__(self):
		self.file = open('item.json', 'wb')
	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + '\n'
		self.file.write(line)
		return item

class CreatFloderPipeline(object):

	def process_item(self, item, spider):
		for image_path in item['image_paths']:
			image_path = "../pictures/" + image_path
			os.mkdir(image_path)
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
