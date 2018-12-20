# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影排名
    serial_number = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 电影介绍
    movie_introduce = scrapy.Field()
    # 电影星级
    movie_star = scrapy.Field()
    # 评论数
    movie_commits = scrapy.Field()
    # 电影描述
    movie_describe = scrapy.Field()

