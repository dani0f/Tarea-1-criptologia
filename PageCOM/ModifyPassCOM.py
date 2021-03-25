from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = "U53rN4M3"
passWord = "hola1234"
passWordNew = "password1234"

path = "C:\\Users\\Daniela\\Desktop\\Tarea 1 criptologia\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(path,chrome_options=options )
driver.get("https://eu.4game.com/")

def login(userName,passWord,passWordNew):
    #by css_selector
    link = driver.find_element_by_css_selector("#page-header > header > div > div > div.UserBar__container__A0i7N.UserBar__responsive__2vyGM > a")
    link.click()

    try: 
        #userName
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[1]/div/input"))        
        )
        element.send_keys(userName)
        #passWord
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[2]/div/input"))        
        )
        element.send_keys(passWord)
        #buttonLogin
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button"))        
        )
        element.click()
        #navegate 1
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div[1]/header/div/div/div[1]/div[1]/span"))        
        )
        element.click()
        #navegate 2
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Security"))        
        )
        element.click()
        #button change
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button"))        
        )
        element.click()
        #passWord
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/section/div/div/form/div[1]/div/div/input"))        
        )
        element.send_keys(passWord)
        #passWordNew
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/section/div/div/form/div[2]/div/div/input"))        
        )
        element.send_keys(passWordNew)
        #buttonSave
        time.sleep(5)
        element = WebDriverWait(driver,10).until(
            
            EC.presence_of_element_located((By.CSS_SELECTOR,"#gatsby-focus-wrapper > div > section > div > div > form > button"))        
        )
        element.click()


    except:
        driver.quit()


login(userName,passWord,passWordNew)


