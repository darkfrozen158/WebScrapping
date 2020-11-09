from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo_articulo = Field()
    contenido = Field()
    fecha = Field()
    
    
class IGNCrawler(CrawlSpider):
    name = 'ign'
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 10000 # Un poco alto
    }


    allowed_domains = ['latam.ign.com']
    start_urls = ['https://latam.ign.com/se/?q=ps4&order_by=-date&model=article']
    
    download_delay = 1
    
    rules = (
        Rule(
        LinkExtractor(
            allow=r'&page=\d+'
        ), follow=True
    ),
         Rule(
             LinkExtractor(
                 allow=r'/news/'
             ), follow=True, callback='parse_articulos'
         ),    
             )
    
    def parse_articulos(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo_articulo', '//h1/text()')
        #item.add_xpath('contenido', '//div[@id="id_text"]//*/text()')
        item.add_xpath('fecha', '//div[@class="article-publish-date"]/span/text()')
        yield item.load_item()

    