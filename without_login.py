#WITHOUT LOGGING IN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\user\Documents\chromedriver.exe') 

driver.get("https://www.flipkart.com/")
time.sleep(3)

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')

file = open("searchtag.txt","r")
con = file.read()
print('Searching for ' + con)
file.close()

element.send_keys(con)
element.send_keys(Keys.RETURN)

