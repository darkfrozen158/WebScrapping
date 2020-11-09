from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
 
 
class Pregunta(Item):
    id = Field()
    pregunta = Field()
    vistas = Field()
    #descripcion = Field()
    votos = Field()
    respuestas = Field()
    
    
 
class StackOverFlowSpider(Spider):
    name = "MiPrimerSpider"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    }
 
    start_urls = ["https://es.stackoverflow.com/questions"]
 
    #Ya me saca la web al poner response en el parse
    def parse(self, response):
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
        n = 1
        for i in preguntas:
            item = ItemLoader(Pregunta(), i)
            item.add_xpath('pregunta', './/h3/a/text()')
            #item.add_xpath('descripcion', './/div[@class="excerpt"]/text()')
            item.add_value('id', n)
            item.add_xpath('vistas', './/div[@class="views "]/text()')
            item.add_xpath('votos', './/span/strong/text()')
            item.add_xpath('respuestas', './/strong/text()')
            n +=1
            yield item.load_item()
            
    

    

