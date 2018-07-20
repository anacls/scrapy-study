import scrapy

class Books(scrapy.Spider):
    name = "books"

    start_urls = [
        "http://books.toscrape.com/"
    ]

    def parse(self, response):
        books = response.xpath('//article[@class="product_pod"]')

        for book in books:
            title = book.xpath('./h3//a/@title').extract_first()
            price = book.xpath('//div[@class="product_price"]//p[@class="price_color"]/text()').extract_first()
            link = book.xpath('./h3//a/@href').extract_first()
            yield{
                'title': title,
                'price': price,
                'link': link,
            }
