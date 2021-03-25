from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = 'U53rN4M3'
email ="Tarea1Intento2@yopmail.com"
passWord = "password123"

path = "C:\\Users\\Daniela\\Desktop\\Tarea 1 criptologia\\chromedriver.exe"
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(path,chrome_options=options )

driver.get("https://eu.4game.com/")


def register(userName,email,passWord):
    #by css_selector
    link = driver.find_element_by_css_selector("#page-header > header > div > div > div.UserBar__container__A0i7N.UserBar__responsive__2vyGM > a")
    link.click()

    try: 
        #by xpath
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"""//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[1]/a[2]"""))        
        )
        element.click()
        #by link_text
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"via email"))        
        )
        element.click()
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#gatsby-focus-wrapper > div > div.Layout__layoutInner__qgpH4 > div.Auth__container__3sO1H > div > div > div > div.AuthGeneral__tabsPanel__2g5bH > div > form > div.RegisterForm__login__1361p.Input__theme-light__2bGpB > div > input"))        
        )
        #userName
        element.send_keys(userName)
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#gatsby-focus-wrapper > div > div.Layout__layoutInner__qgpH4 > div.Auth__container__3sO1H > div > div > div > div.AuthGeneral__tabsPanel__2g5bH > div > form > div.RegisterForm__email__WFSvx.Input__theme-light__2bGpB > div > input"))        
        )
        #password
        element.send_keys(email)
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#gatsby-focus-wrapper > div > div.Layout__layoutInner__qgpH4 > div.Auth__container__3sO1H > div > div > div > div.AuthGeneral__tabsPanel__2g5bH > div > form > div.RegisterForm__password__1sn3z.Input__theme-light__2bGpB > div > input"))        
        )
        element.send_keys(passWord)
        #click in privacy policy
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div[3]/div/form/label[1]"))        
        )
        element.click()
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#gatsby-focus-wrapper > div > div.Layout__layoutInner__qgpH4 > div.Auth__container__3sO1H > div > div > div > div.AuthGeneral__tabsPanel__2g5bH > div > form > button"))        
        )
        element.click()
    except:
        driver.quit()

register(userName,email,passWord)