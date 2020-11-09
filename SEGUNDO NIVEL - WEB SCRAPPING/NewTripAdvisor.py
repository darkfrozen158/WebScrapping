from scrapy.item import Field
from scrapy.item import Item
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose


class Opinion(Item):
    titulo_opinion = Field()
    clasificacion = Field()
    contenido = Field()
    autor = Field()
    
class TripAdvisor_Crawler(CrawlSpider):
    name = "TripAdvisor"
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 100 # Un poco alto
    }
    
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g294316-Lima_Lima_Region-Hotels.html']
    
    download_delay = 1
    
    rules = (
        # // -> LOS QUE ESTAN FUERA Y / -> CUANDO VIENEN DESPUES DEL DIV
        #PAGINACION HOTELES
        Rule( LinkExtractor(
            allow=r'-oa\d+-' #\d+ sirve para que vaya cualquier numero en la paginación 
        ), follow=True
        ),
        
        #DETALLE DE HOTELES
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-',
                restrict_xpaths = ['//div[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]//a[@data-clicksource="HotelName"]']
            ), follow=True
        ),
        
        #DETALLES DE OPINIONES DE CADA HOTEL
        Rule(
            LinkExtractor(
                allow=r'-or\d+-'
            ), follow=True
        ),
        
        #DETALLE PERFIL DE USUARIO QUE BRINDO OPINIÓN
        Rule(
            LinkExtractor(
                allow=r'/Profile/',
                restrict_xpaths=['//div[@data-test-target="reviews-tab"]//a[contains(@class, "ui_header_link _1r_My98y")]']
            ), follow=True, callback='parse_opiniones'
        ),
    )
    
    def ObtenerValoracion(self, texto):
        #"ui_bubble_rating bubble_50"
        #["ui, buble, rating buble, 50]
         calificacion = texto.split("_")[3]
         return calificacion
    
    def parse_opiniones(self, response):
        sel = Selector(response)
        opiniones = sel.xpath('//div[@id="content"]/div/div')
        autor = sel.xpath('//h1/span/text()').get()
        
        for i in opiniones:
            item = ItemLoader(Opinion(), i)
            item.add_value('autor', autor)
            item.add_xpath('titulo_opinion', '//div[@class="_3IEJ3tAK _2K4zZcBv"]/text()')
            item.add_xpath('contenido', './/q/text()') #dentro de la opinión
            item.add_xpath('clasificacion', './/div[contains(@class, "_1VhUEi8g _2K4zZcBv")]/span/@class', MapCompose(self.ObtenerValoracion))
            yield item.load_item()

   

    