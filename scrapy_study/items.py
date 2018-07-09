import scrapy

class LineItem(scrapy.Item):
    name = scrapy.Field()
    situation = scrapy.Field()
    description = scrapy.Field()