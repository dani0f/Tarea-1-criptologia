from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email ="TareaCintento0@yopmail.com"
passWord = "password123"

path = "C:\\Users\\Daniela\\Desktop\\Tarea-1-criptologia\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(path,chrome_options=options )

driver.get("https://tibiachile.cl")


def login(email,passWord):
    link = driver.find_element_by_xpath("/html/body/div[2]/div/div/a")
    link.click()

    try: 
        #navegate
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Entrar"))        
        )
        element.click()
        #email
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"email"))        
        )
        element.send_keys(email)
        #pass
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"passwd"))
        )
        element.send_keys(passWord)
        #send
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[4]/input[2]"))        
        )
        element.click()
        
        
    except:
        driver.quit()

login(email,passWord)