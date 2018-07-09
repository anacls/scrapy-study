import scrapy
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from scrapy_study.items import LineItem


class TrainsSituationSpider(Spider):
    name = 'trains_situation'
    start_urls = [
        "http://www.cptm.sp.gov.br/Atendimento/"
    ]

    def parse(self, response):
        lines = response.xpath('//span[@class="nome_linha"]')
        for line in lines:
            l = ItemLoader(item=LineItem(), selector=line)
            l.add_xpath('name', './text()')
            l.add_xpath('situation', './following-sibling::span/text()')
            l.add_xpath('description', './following-sibling::span/@data-original-title')
            yield l.load_item()
