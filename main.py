import time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);

# Chhoosing website
driver.get("https://en.wikipedia.org/wiki/Snake")
print("Welcome to:", driver.title)

# Locating website elements examples
# tag = driver.find_element_by_tag_name('h1')
# element = driver.find_element_by_id("content")
# print("Finding Tags:", "\n", tag)
# print("Finding Elements:", "\n", element)

# <input type="search" name="search" placeholder="Search Wikipedia" autocapitalize="sentences" title="Search Wikipedia [alt-shift-f]" accesskey="f" id="searchInput" autocomplete="off">

search = driver.find_element_by_name("search")
search.send_keys("snake")
search.send_keys(Keys.RETURN)

try: 
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    articles = main.find_elements_by_class_name('mw-search-result')
    for article in articles:
        header = article.find_element_by_class_name("mw-search-result-heading")
        print(header.text)
finally:
    driver.quit()


# time.sleep(5)

# driver.quit()

