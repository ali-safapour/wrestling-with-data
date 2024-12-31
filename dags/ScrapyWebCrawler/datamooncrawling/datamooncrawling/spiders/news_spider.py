import scrapy
from scrapy.spiders import Spider
from scrapy import Request

class MySpider(Spider):
    name = "news_spider"
    allowed_domains = ["isna.ir", "irna.ir", "farsnews.ir"]
    start_urls = [
        "https://www.isna.ir/",
        "https://www.irna.ir/",
        "https://www.farsnews.ir/"
    ]
    custom_settings = {
        "DEPTH_LIMIT": 2
    }

    def parse(self, response, depth=0):
        # if depth > 1:
        #     return
        data = response.xpath("//p//text() | //h//text() | //h1//text() | //h2//text() | //h3//text() | //h4//text() | //h5//text() | //h6//text()").getall()
        data = [data_item.strip() for data_item in data if data_item.strip() not in ['', None]]
        yield {'data': data}
        
        for href in response.xpath("//a/@href").getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
            # yield scrapy.Request(response.urljoin(href), self.parse, cb_kwargs=dict(depth=depth+1))