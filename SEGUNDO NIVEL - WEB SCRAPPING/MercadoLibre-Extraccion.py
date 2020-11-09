from scrapy.item import Field
from scrapy.item import Item 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()
    
class MercadoLibre(CrawlSpider):
    name = "MercadoLibre"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 2000
    }
    
    download_delay = 1
    
    allowed_domains = ['listado.mercadolibre.com.pe', 'articulo.mercadolibre.com.pe']
    
    start_urls=["https://listado.mercadolibre.com.pe/laptop-gamer#D[A:laptop%20gamer,L:undefined]"]
    
    rules = (
        #REGLA PARA PAGINACION
        Rule(
            LinkExtractor(
                allow=r'/_Desde_'
            ), follow=True
        ),
        #DETALLE DE LOS PRODUCTOS
        Rule(
            LinkExtractor(
                allow=r'/MPE-'
            ), follow=True, callback='parse_item'
        ),
    )
    
    def LimpiezaTitulo(self, texto):
        texto_nuevo = texto.replace("\n", "").replace("\t", "").replace("\r", "")
        return texto_nuevo
    
    def parse_item(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo', '//h1/text()', MapCompose(self.LimpiezaTitulo))
        item.add_xpath('descripcion', '//div[@class="item-description__text"]/p/text()')
        item.add_xpath('precio', '//span[@class="price-tag-fraction"]/text()')
        
        yield item.load_item()
    
    
    