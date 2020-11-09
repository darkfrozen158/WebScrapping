from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# Defino una abstraccion para cada tipo de informacion que quiero extraer
# Cada una tiene sus propias propiedades diferentes
class Articulo(Item):
    titulo_articulo = Field()
    contenido = Field()

class Review(Item):
    titulo_review = Field()
    calificacion = Field()

class Video(Item):
    titulo_video = Field()
    fecha_de_publicacion = Field()


class IGNCrawler(CrawlSpider):
    name = 'ign'
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 100 # Un poco alto
    }

    allowed_domains = ['latam.ign.com']
    start_urls = ['https://latam.ign.com/se/?model=article&q=ps4']

    download_delay = 1

    rules = (
        Rule(
            LinkExtractor(
                allow=r'type='
            ), follow=True), # HORIZONTALIDAD POR TIPO => No tiene callback ya que aqui no voy a extraer datos
        Rule(LinkExtractor(
            allow=r'&page=\d+'
            ), follow=True), # HORIZONTALIDAD DE PAGINACION EN CADA TIPO => No tiene callback ya que aqui no voy a extraer datos
        
        # Una regla por cada tipo de contenido donde ire verticalmente
        # Cada una tiene su propia funcion parse que extraera los items dependiendo de la estructura del HTML donde esta cada tipo de item
        Rule(
            LinkExtractor( # VERTICALIDAD DE REVIEWS
                allow=r'/review/'
            ), follow=True, callback='parse_reviews'),
        Rule(
            LinkExtractor( # VERTICALIDAD DE VIDEOS
                allow=r'/video/'
            ), follow=True, callback='parse_videos'),
        Rule(
            LinkExtractor(
                allow=r'/news/' # VERTICALIDAD DE ARTICULOS
            ), follow=True, callback='parse_articulos'),
    )

    # DEFINICION DE CADA FUNCION PARSEADORA DE CADA TIPO DE INFORMACION
    
    # ARTICULO
    def parse_articulos(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo_articulo', '//h1/text()')
        item.add_xpath('contenido', '//div[@id="id_text"]//*/text()')
        yield item.load_item()

    # REVIEW
    def parse_reviews(self, response):
        item = ItemLoader(Review(), response)
        item.add_xpath('titulo_review', '//h1/text()')
        item.add_xpath('calificacion', '//span[@class="side-wrapper side-wrapper hexagon-content"]/text()')
        yield item.load_item()

    # VIDEO
    def parse_videos(self, response):
        item = ItemLoader(Video(), response)
        item.add_xpath('titulo_video', '//h1/text()')
        item.add_xpath('fecha_de_publicacion', '//span[@class="publish-date"]/text()')
        yield item.load_item()

