import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.get("http://google.com")
PHRASE = 'What is Selenium'

elem = driver.find_element_by_name("q")
elem.send_keys(PHRASE)
# elem.send_keys(Keys.RETURN)

while True:
  try:
    webdriver.support.ui.WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div[class="srg"')))
    break
  except TimeoutException:
    print("Loading took too much time! Check if you pressed Enter!")
    break

time.sleep(5)