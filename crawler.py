from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome("본인 웹드라이버 저장 주소")
driver.get('http://ssullog.joins.com/speech/speechList')

#크롤링할 페이지로 들어가기
#태그는 페이지 열 때마다 새로 설정해두어야 한다.
sample = driver.find_element_by_css_selector('#speech_no_24713 > div.box-header > div > a')
sample.send_keys('\n')

#크롤링 해오기
html = driver.page_source
soup = BeautifulSoup(html, "html.parsar")

notices = soup.select("pop_search > div.db > div.box01")

for n in notices:
	print(n.text.strip())

