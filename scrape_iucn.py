# Deprecated
## Now using https://github.com/chikity/Red to scrape iucn data instead of building my own


from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
chrome_driver_binary = "/opt/homebrew/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, options=options)

# Set Up
scientific_name = []
common_name = []
last_assessed = []
scope = []
assessment = []
annotation = []

# Launch Browser
driver.get("https://www.iucnredlist.org/species/166073/6165399")

content = driver.page_source
soup = BeautifulSoup(content)

name=a.find('div', attrs={'class':'_3wU53n'})
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})

scientific_name = a.find('div', attrs={'class':'headline__title'})
common_name = a.find('div', attrs={'class':'headline__title'})
last_assessed = []
scope = []
assessment = []
annotation = []
