import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);
  

driver.get("https://en.wikipedia.org/wiki/Snake")


tag = driver.find_element_by_tag_name('h1')
element = driver.find_element_by_id("content")
print("Finding Tags:", "\n", tag)
print("Finding Elements:", "\n", element)