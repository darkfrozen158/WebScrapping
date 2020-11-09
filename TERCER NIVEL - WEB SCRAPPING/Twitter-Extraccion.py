from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

opts = Options()

opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome('C:/Users/Net/PycharmProjects/pythonProject/TERCER NIVEL - WEB SCRAPPING/chromedriver.exe',
                          chrome_options=opts)

driver.get('https://twitter.com/login')

user = "leonardo158xd@gmail.com"

password = open('C:/Users/Net/PycharmProjects/pythonProject/TERCER NIVEL - WEB SCRAPPING/password.txt').readline().strip()

#Espera 10 segundos a que aparesca el formulario para colocar el usuario y contraseña en Twitter.
WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.XPATH, '//main//input[@name="session[username_or_email]"]'))
)

input_user = driver.find_element(By.XPATH, '//main//input[@name="session[username_or_email]"]')

input_password = driver.find_element(By.XPATH, '//main//input[@name="session[password]"]')

input_user.send_keys(user)

input_password.send_keys(password)

boton = driver.find_element(By.XPATH, '//main//div[@data-testid="LoginForm_Login_Button"]/div[@dir="auto"]')

boton.click()

WebDriverWait(driver, 10).until(
    ec.presence_of_all_elements_located((By.XPATH, '//section//article//div[@dir="auto"]'))
)

tweets = driver.find_elements(By.XPATH, '//section//article//div[@dir="auto"]')
try:
    for i in tweets:
        print(i.text)
except Exception as e:
    print(e)
    pass



