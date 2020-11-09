import random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Net/PycharmProjects/pythonProject/TERCER NIVEL - WEB SCRAPPING/chromedriver.exe')

#La pagina se tiene que cargar por completo para que se continue ejecutando el codigo.
driver.get('https://www.olx.com.pe/autos_c378')

# Va a dormir entre 4 y 6 segundos:
sleep(random.uniform(4.0,6.0))
boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')


#que se repita 5 veces
for i in range(5):
    try:
        boton.click()
        #Va a dormir entre 8 y 10 segundos :
        sleep(random.uniform(8.0,10.0))
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

#OBTENER TODOS LOS ELEMENTOS CON EL TAG LI CUYO ATRIBUTO DATA-AUT-ID SEA ITEMBOX :

autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# .// -> significa dentro del elemento.
for auto in autos:
    try:
        titulo = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
        print("Titulo: {}".format(titulo))
        precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
        print('Precio: {}'.format(precio))
        año_km = auto.find_element_by_xpath('.//span[@data-aut-id="itemDetails"]').text
        print('Año - Cantidad de Kilometros: {}'.format(año_km))
        ubicacion = auto.find_element_by_xpath('.//span[@data-aut-id="item-location"]').text
        print('Ubicacion: {}'.format(ubicacion))
        print('---------------------------------------------------------')
    except:
        pass

    
    
    