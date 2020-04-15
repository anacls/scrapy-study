from scrapy import Spider, Request

class TripAdvisor(Spider):
    name = "tripadvisor"

    start_urls = [ 
        'https://www.tripadvisor.com.br/Restaurants-g303613-Indaiatuba_State_of_Sao_Paulo.html'
    ]

    def parse(self, response):
        restaurante_links = response.xpath('//div[@id="EATERY_LIST_CONTENTS"]//div[@class="wQjYiB7z"]/span/a')

        for restaurante_link in restaurante_links:
            url = restaurante_link.xpath('./@href').extract_first()
            yield Request(
                url=response.urljoin(url),
                callback=self.parse_restaurantes,
            )
        
        next_page = response.xpath('//a[contains(text(), "Próximas")]//@href').extract_first()
        if next_page:
            yield Request(
                url=response.urljoin(next_page),
                callback=self.parse
            )


    def parse_restaurantes(self, response):
        nome = response.xpath('//h1[@class="ui_header h1"]/text()').extract_first()
        nota = response.xpath('//span[@class="restaurants-detail-overview-cards-RatingsOverviewCard__overallRating--nohTl"]/text()').extract_first()
        endereco = response.xpath('//span[@class="restaurants-detail-overview-cards-LocationOverviewCard__detailLinkText--co3ei"]/text()').extract_first()
        url = response.url
        yield{
            'nome': nome,
            'endereco': endereco,
            'nota': nota,
            'link': url,
        }
        
        
