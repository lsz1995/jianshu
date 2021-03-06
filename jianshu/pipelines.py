# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JianshuPipeline(object):
    def process_item(self, item, spider):
        return item




class JianshuPipeline(object):
    collection_name = 'user'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spiser(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].update({'id': item['id']}, dict(item), True)
        # id相同，只更新，不插入，去重作用。
        return 'ok!'