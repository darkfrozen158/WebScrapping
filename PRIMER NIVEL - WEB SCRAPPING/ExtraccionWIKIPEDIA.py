#EXTRAER LOS NOMBRES DE LOS IDIOMAS DE LA PAGINA wikipedia.org
import requests as r
from lxml import html as h

encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

#URL SEMILLA :

url = "https://www.wikipedia.org/"

respuesta = r.get(url, headers=encabezados )

parser = h.fromstring(respuesta.text)

esp = parser.xpath("//a[@id='js-link-box-es']/strong/text()")

ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")



#esta expresion hace que se obtenga todos los que en su clase contengan "central-featured-lang"
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")

for i in idiomas:
    print(i)


print("----")

idiomas2 = parser.find_class("central-featured-lang")

for e in idiomas2:
    print(e.text_content())





