import scrapy
from scrapy import Request

class TrilhasTDC(scrapy.Spider):
    name = "trilhas_tdc"

    start_urls = [
        "http://www.thedevelopersconference.com.br/tdc/2018/saopaulo/trilhas"
    ]

    def parse(self, response):
        colunas = response.xpath('//div[contains(@class, "col-sp")]')

        for coluna in colunas:
            dia = coluna.xpath('./h4/text()').extract_first()
            links_trilhas = coluna.xpath('./a/@href').extract()
            for link_trilha in links_trilhas:
                yield Request(
                    url=response.urljoin(link_trilha),
                    callback=self.parse_trilha,
                    meta={
                        'dia' : dia,
                    }
                )
    def parse_trilha(self,response):
        yield{
            'dia' : response.meta.get('dia'),
            'titulo' : response.xpath('//h1[@class="titulo-trilha"]/text()').extract_first(),
            'subtitulo': response.xpath('//h1[@class="titulo-trilha"]/small/text()').extract_first(),
            'descricao': response.xpath('//div[@class="lead"]//p/text()').extract(),
            'link' : response.url,
        }
