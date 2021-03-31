from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


email ="JuanitoPerezTarea2@yopmail.com"


path = "C:\\Users\\Daniela\\Desktop\\Codigos\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(path,chrome_options=options )

driver.get("https://tibiachile.cl")


def recovery(email):
    link = driver.find_element_by_xpath("/html/body/div[2]/div/div/a")
    link.click()

    try: 
        #navegate
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Entrar"))        
        )
        element.click()
        #click
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"¿Ha olvidado su contraseña?"))
        )
        element.click()
        #email
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"email"))        
        )
        element.send_keys(email)
        #button
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[2]/input"))        
        )
        element.click()
        
    except:
        driver.quit()

recovery(email)









