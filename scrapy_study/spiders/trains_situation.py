import scrapy


class TrainsSituation(scrapy.Spider):
    name = "trains_situation"

    def start_requests(self):
        urls = [
            'http://www.cptm.sp.gov.br/Atendimento/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lines = response.xpath('//span[@class="nome_linha"]')
        
        for line in lines:
            name = line.xpath('./text()').extract_first(default="")
            situation = line.xpath('./following-sibling::span/text()').extract_first(default="")
            print (name + ': ' + situation)
        