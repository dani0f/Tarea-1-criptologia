from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = 'u53rN4Me'
#username no key sensitive?
firstName="Maria"
lastName="kawai"
email ="Tarea1Intento1@yopmail.com"
passWord = "Pa$$w0rd12345AAAAA"
passWordNew = "Pa$$w0rd12345AAAAAA"

path = "C:\\Users\\Daniela\\Desktop\\Tarea-1-criptologia\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(path,chrome_options=options )

driver.get("https://mariakawaii.cl")


def modify(fistName,lastName,userName,passWord,passWordNew):
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
        #navegate 1
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/header/div/div[2]/div[1]/div[4]/ul/li[1]/a"))        
        )
        element.click()
        #navegate 2 
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div/div/div/div/div/div/ul/li[5]/a"))        
        )
        element.click()
        #names
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"account_first_name"))        
        )
        element.send_keys(firstName)
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"account_last_name"))        
        )
        element.send_keys(lastName)
        #passwords
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"password_current"))        
        )
        element.send_keys(passWord)
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"password_1"))        
        )
        element.send_keys(passWordNew)
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"password_2"))        
        )
        #confirm
        element.send_keys(passWordNew)
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div/div/div/div/div/div/form/p[5]/button"))        
        )
        element.click()
        
    except:
        driver.quit()

modify(firstName,lastName,userName,passWord,passWordNew)