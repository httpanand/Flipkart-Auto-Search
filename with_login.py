#SEARCHING WITH LOGGING IN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\user\Documents\chromedriver.exe') 

driver.get("https://www.flipkart.com/")
time.sleep(3)

email = 'your flipkart email'
password = 'your flipkart password'

email_input = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
email_input.send_keys(email)

pass_input = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
pass_input.send_keys(password)

login_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button').click()
time.sleep(5)
element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')

file = open("searchtag.txt","r")
con = file.read()
print('Searching for ' + con)
file.close()

element.send_keys(con)
element.send_keys(Keys.RETURN)



