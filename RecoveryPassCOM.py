from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userNameORemail = "U53rN4M3"

path = "C:\\Users\\Daniela\\Desktop\\Tarea 1 criptologia\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(path,chrome_options=options )
driver.get("https://eu.4game.com/")

def recovery(userNameORemail):
    #by css_selector
    link = driver.find_element_by_css_selector("#page-header > header > div > div > div.UserBar__container__A0i7N.UserBar__responsive__2vyGM > a")
    link.click()

    try: 
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Forgot password?"))        
        )
        element.click()
        userName
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/div/input"))        
        )
        element.send_keys(userNameORemail)
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/button"))        
        )
        element.click()
    except:
        driver.quit()


recovery(userNameORemail)




