import time
import requests
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
start_url = "https://www.basketball-reference.com/players/r/rosede01/gamelog/{}"
#for year in derrick_rose_tenure:
url = start_url.format(2009)
driver.get(url)
driver.execute_script("window.scrollTo(1,1000)")
time.sleep(2)
html = driver.page_source