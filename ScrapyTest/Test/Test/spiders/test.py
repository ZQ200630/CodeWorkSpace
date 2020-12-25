import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.body)
