from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome("본인 웹드라이버 저장 주소")

driver.get('http: // ssullog.joins.com/speech/speechList?searchValue=% 27)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

driver.find_element_by_css_selector(
    '#speech_no_24704 > div.box-header > div > a').click()
