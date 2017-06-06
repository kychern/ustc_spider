# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UstcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    class_name=scrapy.Field()
    class_time=scrapy.Field()
    class_teacher=scrapy.Field()
    #class_college=scrapy.Field()
    class_score=scrapy.Field()
    #class_score_num=scrapy.Field()
