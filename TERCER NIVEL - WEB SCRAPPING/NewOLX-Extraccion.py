from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('C:/Users/Net/PycharmProjects/pythonProject/TERCER NIVEL - WEB SCRAPPING/chromedriver.exe')

driver.get('https://www.olx.com.pe/')

for i in range(3):
    try:
        #Se espera un evento por 10 segundos hasta que el elemento exista.
        boton = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,'//button[@data-aut-id="btnLoadMore"]'))
        )
        boton.click()
        
        #Verifica la presencia de los elementos a traves de un XPATH , en este caso la presencia del titulo del producto
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[data-aut-id="itemTitle"]'))
        )
    except:
        #Si hay algun error se rompe el lazo for
        break

anuncios = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for anuncio in anuncios:
    titulo = anuncio.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print("Titulo: {}".format(titulo))
    precio = anuncio.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print("Precio: {}".format(precio))
    print('-------------------------------------------------------------------')
    