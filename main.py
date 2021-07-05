import time
import csv
import pandas as pd
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Init of webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);

# Website to scrape
driver.get("https://en.wikipedia.org/wiki/Snake")
print("Welcome to:", driver.title)


tags = driver.find_element_by_tag_name("h1")
print("Tags", tags.text)

elements = driver.find_elements_by_tag_name("p")
for x in elements:
    text_arr = [x.text]


print(text_arr)

data = {'Page': [driver.title],'Text':[x.text]}


df = pd.DataFrame(data)
print(df)
df.to_csv('textdata.csv')




# Searching
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

