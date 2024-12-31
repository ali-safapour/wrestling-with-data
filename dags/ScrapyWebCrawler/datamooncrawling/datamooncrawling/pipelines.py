# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DatamooncrawlingPipeline:
    def open_spider(self, spider):
        self.f = open('output.txt', 'a', encoding='utf-8')
    
    def close_spider(self, spider):
        self.f.close()
        
    def process_item(self, item, spider):
        item_adapter = ItemAdapter(item)
        self.f.writelines(item_adapter['data'])
        return item