from scrapy.item import Field, Item
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader

class Departamento(Item):
    nombre_proyecto = Field()
    direccion = Field()
    distrito = Field()
    distrito_estatus = Field()
    departamento = Field()
    
class Urbania(CrawlSpider):
    name="Urbania"
    custom_settings = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36',
        'CLOSESPIDER_ITEMCOUNT': 50
    }
    
    start_urls = [
        'https://urbania.pe/buscar/proyectos-departamentos?page=1',
        'https://urbania.pe/buscar/proyectos-departamentos?page=2',
        'https://urbania.pe/buscar/proyectos-departamentos?page=3',
        'https://urbania.pe/buscar/proyectos-departamentos?page=4',
        'https://urbania.pe/buscar/proyectos-departamentos?page=5'
    ]
    
    allowed_domains = ['urbania.pe']
    
    download_delay = 1
    
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/proyecto-'
            ),follow=True, callback="parse_urbania"
        ),
    )
    
    def EstatusDistrito(self, distrito):
        distritos = ['Chorrillos', 'Miraflores', 'Barranco', 'San Borja', 'San Isidro', 'San Miguel']
        
        if (distrito in distritos):
            distrito_estatus = "CLASE ALTA"
        else:
            distrito_estatus = "CLASE MEDIA"
        return distrito_estatus
    
    def parse_urbania(self, response):
        sel = Selector(response)
        item = ItemLoader(Departamento(), sel)
        
        item.add_xpath('nombre_proyecto', '//div[@class="section-title"]/h1/text()')
        item.add_xpath('direccion', '//div[@class="section-location"]/b/text()')
        item.add_xpath('departamento', '//li[5][@class="bread-item "]/a/span/text()')
        item.add_xpath('distrito', '//li[6][@class="bread-item "]/a/span/text()')
        item.add_xpath('distrito_estatus', '//li[6][@class="bread-item "]/a/span/text()', MapCompose(self.EstatusDistrito))
        
        yield item.load_item()

