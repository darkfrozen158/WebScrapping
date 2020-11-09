import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd

scrollingScript = """ 
    document.getElementsByClassName('section-layout section-scrollbox scrollable-y scrollable-show')[0].scroll(0, 200)
"""

opts = Options()

opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome('C:/Users/Net/PycharmProjects/pythonProject/TERCER NIVEL - WEB SCRAPPING/chromedriver.exe',
                          chrome_options=opts)

driver.get("https://www.google.com/maps/place/Restaurante+Amazonico/@40.423706,-3.6872655,17z/data=!4m7!3m6!1s0xd422899dc90366b:0xce28a1dc0f39911d!8m2!3d40.423706!4d-3.6850768!9m1!1b1")

sleep(random.uniform(4.0,5.0))

SCROLLS = 0

datos = []

while(SCROLLS != 3):
    driver.execute_script(scrollingScript)
    sleep(random.uniform(5,6))
    SCROLLS +=1

reviews_restaurante = driver.find_elements(By.XPATH, '//div[contains(@class, "section-review ripple-container")]')

for review in reviews_restaurante:
    
    
    userLink = review.find_element(By.XPATH, './/div[@class="section-review-title"]')
    
    try:
        userLink.click()
        #cambiar de pestaña
        driver.switch_to.window(driver.window_handles[1])
        
        boton_opiniones = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//button[@class="section-tab-bar-tab ripple-container section-tab-bar-tab-selected"]'))
        )
        
        boton_opiniones.click()
        
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//div[@class="section-layout section-scrollbox scrollable-y scrollable-show"]'))
        )
        
        USER_SCROLLS = 0
        while(USER_SCROLLS != 3):
            driver.execute_script(scrollingScript)
            sleep(random.uniform(5,6))
            USER_SCROLLS +=1
            
        user_reviews = driver.find_elements(By.XPATH, '//div[contains(@class, "section-review ripple-container")]')
        
        #Cuando se ve &nbsp; en la consola f12 , significa que hay un espacio.
        for user in user_reviews:
           usuario = user.find_element(By.XPATH, './/div[@class="section-review-title section-review-title-consistent-with-review-text"]').text
           texto =  user.find_element(By.XPATH, './/span[@class="section-review-text"]').text
           rating = user.find_element(By.XPATH, './/span[@class="section-review-stars"]').get_attribute('aria-label')
           
           datos.append({
               "Usuario":usuario,
               "Opinión":texto,
               "Puntuación":rating
           })
           
           #print("Usuario: {}".format(usuario))
           #print("Opinión: {}".format(texto))
           #print("Puntuación: {}".format(rating))
           #print("---------------------------------------------------------------------------------------------------------------")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])    
         
    except Exception as e:
        print(e)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])  

df = pd.DataFrame(datos)

print(df)

#df.to_csv('GooglePlace2.csv', header=True)

