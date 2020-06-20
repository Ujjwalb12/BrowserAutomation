from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chromium()
browser.get('https://www.twitter.com')


time.sleep(2)

login = browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')


login[0].click()

print("Login in Twitter")

user = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')


user[0].send_keys('USER-NAME')

user = browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')


with open('test.txt', 'r') as myfile:
    Password = myfile.read().replace('\n', '')
user.send_keys(Password)

LOG = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()
print("Login Successful")
time.sleep(5)

elem = browser.find_element_by_name("q")
elem.click()
elem.clear()

elem.send_keys("ujjwalbhatnaga0 ")

elem.send_keys(Keys.RETURN)

print("Search Successful")


browser.close()
