import random
from time import sleep
from selenium import webdriver

# CARGAMOS EL DRIVER:
driver = webdriver.Chrome('./chromedriver.exe')

# BUSCAMOS EL URL:
driver.get('https://www.olx.com.pe/autos_c378?filter=currency_type_eq_PEN&sorting=desc-creation')

# Buscamos el boton cargar mas:
sleep(random.uniform(4.0,6.0))
boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

# Para darle cargar mas varios veces entre los intervalos de 8 a 10 segundos.
for i in range(8):
    try:
        boton.click()
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
        sleep(random.uniform(4.0,6.0))
    except:
        break
    
# BUSCAMOS LOS DATOS DE LOS AUTOS:
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for auto in autos:
    try:
        precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
        print('Precio: {}'.format(precio))
        titulo = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
        print("Titulo: {}".format(titulo))
        AñoKm = auto.find_element_by_xpath('.//span[@data-aut-id="itemDetails"]').text
        print("Año - Cantidad de Kilometros: {}".format(AñoKm))
        ubicacion = auto.find_element_by_xpath('.//span[@data-aut-id="item-location"]').text
        print("Ubicacion: {}".format(ubicacion))
        print('---------------------------------------------------------')
    except:
        pass