from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


email ="modifypasstarea0@yopmail.com"
passWord = "password123"
passWordNew = "password1234"

path ="C:\\Users\\Daniela\\Desktop\\Codigos\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(path,chrome_options=options )

driver.get("https://tibiachile.cl")



def modify(email,passWord,passWordNew):
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
        #sendi
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Mis datos personales"))        
        )
        element.click()

        #send
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"old_passwd"))        
        )
        element.send_keys(passWord)
        #send
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"passwd"))        
        )
        element.send_keys(passWordNew)
        #send
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"confirmation"))        
        )
        element.send_keys(passWordNew)
        #send
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[9]/input"))        
        )
        element.click()
        
        
        
        
        
        
    except:
        driver.quit()

modify(email,passWord,passWordNew)