# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    followings =Field()#关注的人
    followers = Field()#粉丝
    words = Field()
    likes = Field()
    articles = Field()



    pass
