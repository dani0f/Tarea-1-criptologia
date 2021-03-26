from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = 'u53rN4Me'
#username no key sensitive?
email ="Tarea1Intento1@yopmail.com"
passWord = "password123"

path = "C:\\Users\\Daniela\\Desktop\\Tarea-1-criptologia\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(path,chrome_options=options )

driver.get("https://mariakawaii.cl")


def recovery(userName):
    link = driver.find_element_by_link_text("ACCEDER")
    link.click()

    try: 
        #navegate 1
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"¿Olvidaste la contraseña?"))        
        )
        element.click()
        #password
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"user_login"))
        )
        element.send_keys(userName)
        #button confirm
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div/div/div/div/div/form/p[3]/button"))        
        )
        element.click()
        
    except:
        driver.quit()

recovery(userName)









