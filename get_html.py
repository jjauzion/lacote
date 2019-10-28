from selenium import webdriver
import time
from pathlib import Path
from bs4 import BeautifulSoup
import re

html = "https://www.leboncoin.fr/motos/1693837061.htm/"
output = "moto.html"

driver = webdriver.Firefox()
driver.get(html)
time.sleep(2)
soup = BeautifulSoup(driver.page_source)
with Path(output).open(mode='w', encoding='utf-8') as fp:
    fp.write(str(soup))

pattern = re.compile("(?<=window\.FLUX_STATE = {).*(?=})", re.MULTILINE)
data = soup.find("script", text=pattern)
