from selenium import webdriver
from selenium.webdriver.common.keys import *


browser = webdriver.Firefox()

browser.get('http://www.facebook.com')

elem = browser.find_element_by_name("email")
elem.send_keys("manchala.kamesh@gmail.com"+ Keys.RETURN)

elem = browser.find_element_by_name("pass")
elem.send_keys("******"+ Keys.RETURN)


