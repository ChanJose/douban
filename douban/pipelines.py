# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from douban.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection


class DoubanPipeline(object):
    def __init__(self):
        host = mongo_host  # 域名，ip地址
        port = mongo_port  # 端口号
        dbname = mongo_db_name  # 数据库名
        sheetname = mongo_db_collection  # 数据表名
        client = pymongo.MongoClient(host=host, port=port)  # 代理，连接数据库
        mydb = client[dbname]  # 选择数据库
        self.post = mydb[sheetname]  # 选择数据表
    def process_item(self, item, spider):
        # 进行数据的插入
        data =dict(item)  # item就是douban_spider.py里yield过来的
        self.post.insert(data)  # 插入到mongoDB中
        return item
