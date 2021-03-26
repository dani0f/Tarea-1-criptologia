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


def login(userName,passWord):
    #by css_selector
    link = driver.find_element_by_link_text("ACCEDER")
    link.click()

    try: 
        #username
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"username"))        
        )
        element.send_keys(userName)
        #password
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"password"))
        )
        element.send_keys(passWord)
        #button confirm
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div/form/p[3]/button"))        
        )
        element.click()
        
    except:
        driver.quit()

login(userName,passWord)