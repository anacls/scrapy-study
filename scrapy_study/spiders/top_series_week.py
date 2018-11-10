# -*- coding: utf-8 -*-
import scrapy


class TopSeriesWeekSpider(scrapy.Spider):
    name = 'top_series_week'
    start_urls = ['http://www.adorocinema.com/series-tv/top/']

    def parse(self, response):
        series = response.xpath('//a[@class="meta-title-link"][contains(@href, "/series/serie")]')
        for serie in series:
            serie_title = serie.xpath('./text()').extract_first()
            serie_link = serie.xpath('./@href').extract_first()
            yield scrapy.Request(
                url=response.urljoin(serie_link),
                callback=self.parse_series,
                meta={
                    'serie_title': serie_title,
                }
            )

    def parse_series(self, response):
        last_episode= response.xpath('//div[contains(@class, "prev-episode")]')
        next_episode= response.xpath('//div[@class="card-entity card-episode row row-col-padded-10"]')
        
        if last_episode:
            last_episode_title = last_episode.xpath('.//div[@class="meta-title"]//span/text()').extract_first(),
            last_episode_date = last_episode.xpath('.//div[@class="meta-body"]//strong/following-sibling::text()').extract_first().replace(', ', '')
        else:
            last_episode_title = 'N/A'
            last_episode_date = 'N/A'
        
        if next_episode:
            next_episode_title = next_episode.xpath('.//div[@class="meta-title"]//span/text()').extract_first()
            next_episode_date = next_episode.xpath('.//div[@class="meta-body"]//strong/following-sibling::text()').extract_first().replace(', ','')
        else:
            next_episode_title = 'N/A'
            next_episode_date = 'N/A'
        
        
        yield{
            'Title': response.meta.get('serie_title'),
            'Description': response.xpath('//div[contains(@class, "content-txt")]/text()').extract_first(),
            'Seasons': response.xpath('//div[@class="stats-info"][contains(text(), "Temporadas")]/preceding-sibling::div/text()').extract_first(),
            'Episodes': response.xpath('//div[@class="stats-info"][contains(text(), "Epis")]/preceding-sibling::div/text()').extract_first(),
            'Last EP': last_episode_title,
            'Last EP date': last_episode_date,
            'Next EP': next_episode_title,
            'Next EP date': next_episode_date,
            'Serie link': response.url        
        }

        