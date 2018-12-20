# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url,扔到调度器里
    start_urls = ['https://movie.douban.com/top250']

    # 默认的解析方法
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            # 声明一个DoubanItem类的对象
            # item文件导进来
            douban_item = DoubanItem()
            # 电影排名
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()  # extract.first解析到第一个数据
            # 电影名称
            douban_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            # 电影介绍
            content = i_item.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract()  # extract:访问到数据即可
            for i_content in content:
                content_s = "".join(i_content.split())  # 把<p>中的内容链接起来
                douban_item['movie_introduce'] = content_s
            # 电影星级
            douban_item['movie_star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            # 电影评论
            douban_item['movie_commits'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            # 电影描述
            douban_item['movie_describe'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            # 需要将数据yield导pipelines中去，进行数据的清洗、存储
            yield douban_item

        # 解析下一页
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:  # 如果为真，防止到最后一页，翻页时已经没有下一页了
            next_href = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_href, callback=self.parse)  # callback回调函数是当前写的parse函数
