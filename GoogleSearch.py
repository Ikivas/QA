import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException        

class InvalidPageError(Exception):
    pass

driver = webdriver.Chrome()
driver.get("http://google.com")
PHRASE = 'What is Selenium'

elem = driver.find_element_by_name("q")
elem.send_keys(PHRASE)
elem.send_keys(Keys.RETURN)

try:
    driver.find_element_by_css_selector('div[class="srg"')
except NoSuchElementException:
    raise InvalidPageError()
finally:
    driver.close()