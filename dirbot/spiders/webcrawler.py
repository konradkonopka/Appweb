from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

from scrapy.item import Item, Field

class Nazwy(Item):
    opis = Field()
    typ = Field()
    ilosc = Field()

class mojpajak(Spider):
    name = "webcrawler"
    allowed_domains = ["msbase.org"]
    start_urls = ['https://www.msbase.org/cms/benchmarking.json']

    def parse(self, response):
        sel = Selector(response)
        labels = sel.xpath('//tr[@class="wc_title"] | //tr[not(@*)] ')
        items = []
        typ = []
        open('result.json', 'w').close()
        for data in labels:
            item = Nazwy()
            item['typ'] = data.xpath('th[@style="font-weight: bold; text-align:left; padding:5px; font-size:11px;"]/text()').extract()
            item['ilosc'] = data.xpath('td[2]/text()').extract()
            if item['ilosc'] != []:
                item['opis'] = data.xpath('td[1]/text()').extract()
                items.append(item)
            if item['typ'] == []:
                item['typ'] = typ
            else:
                typ = item['typ']
        return items

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'result.json'
})

process.crawl(webcrawler)
process.start() # the script will block here until the crawling is finished
