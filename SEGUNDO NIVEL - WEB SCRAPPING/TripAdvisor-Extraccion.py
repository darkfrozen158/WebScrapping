from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Hotel(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()
    servicios_ofrecidos = Field()
    
class TripAdvisor(CrawlSpider):
    name = "Hoteles"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    
    start_urls = ["https://www.tripadvisor.com/Hotels-g294316-Lima_Lima_Region-Hotels.html"]
    
    #download_delay es el tiempo de espera para que Scrapy haga un nuevo requerimiento de información
    download_delay = 2
    
    #ALLOW => PERMITIR CUYO LINKS EN LA URL TENGAN 
    #parse_hotel => funcion que recibe los requerimientos de la web., se llama cuando se haga un requerimiento.
    rules = (
        Rule( # Regla de movimiento VERTICAL hacia el detalle de los hoteles
            LinkExtractor(
                allow=r'/Hotel_Review-' # Si la URL contiene este patron, haz un requerimiento a esa URL
            ), follow=True, callback="parse_hotel"), # El callback es el nombre de la funcion que se va a llamar con la respuesta al requerimiento hacia estas URLs
    )
    
    def LimpiarPrecio(self, precio):
        precio_limpio = precio.replace("PEN\u00a0","S/. ")
        return precio_limpio
    
    def LimpiarDescripcion(self, texto):
        texto_nuevo = texto.replace("\n", "").replace("\r", "").replace("\t", "")
        return texto_nuevo
        
    def parse_hotel(self, response):
        sel = Selector(response)
        item = ItemLoader(Hotel(), sel)
        item.add_xpath('nombre', '//h1[@id="HEADING"]/text()')
        item.add_xpath('precio', '//div[@class="CEf5oHnZ"]/text()', MapCompose(self.LimpiarPrecio))
        item.add_xpath('descripcion', '//div[contains(@class, "cPQsENeY")]/text()', MapCompose(self.LimpiarDescripcion))
        item.add_xpath('servicios_ofrecidos', '//div[contains(@class, "_2rdvbNSg")]//text()')
        
        yield item.load_item()
        
        

    
