from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd

opts = Options()

opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome('C:/Users/Net/PycharmProjects/pythonProject/TERCER NIVEL - WEB SCRAPPING/chromedriver.exe',
                          chrome_options=opts)

#PASO 1 : Obtengo todas las URLS a las cuales voy a bajar verticalmente,
#dentro de la primera pagina del listado.

driver.get('https://listado.mercadolibre.com.pe/repuestos-autos-camiones-bujias#D[A:repuestos%20autos%20camiones%20bujias]')

try: # Encerramos todo en un try catch para que si no aparece el discilamer, no se caiga el codigo
  disclaimer = driver.find_element(By.XPATH, '//button[@id="cookieDisclaimerButton"]')
  disclaimer.click() # lo obtenemos y le damos click
except Exception as e:
  print (e) 
  None

while True:
    links_productos = driver.find_elements(By.XPATH, '//a[@class="ui-search-item__group__element ui-search-link"]')

    links_paginas = []

    for i in links_productos:
        links_paginas.append(i.get_attribute("href"))
        
    for e in links_paginas:
        
        try:
            driver.get(e)
            titulo = driver.find_element_by_xpath('//h1').text
            precio = driver.find_element(By.XPATH, '//span[@class="price-tag-fraction"]').text
            print("Titulo: {}".format(titulo))
            print("Precio: S/. {}".format(precio))
            print("---------------------------------------")
            driver.back()
        except Exception as error:
            print(error)
            driver.back()              
    try:     
        boton = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        boton.click()
    except:
        break

    