from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import sys

driver = webdriver.Chrome("본인 웹드라이버 저장 주소")
driver.get('http://ssullog.joins.com/speech/speechList')

#크롤링할 페이지로 들어가기
#태그는 페이지 열 때마다 새로 설정해두어야 한다.
sample = driver.find_element_by_css_selector('#speech_no_24713 > div.box-header > div > a')
sample.send_keys('\n')
time.sleep(5)

#크롤링 해오기
html = driver.page_source
soup = BeautifulSoup(html, "html.parsar")

notices = soup.select("pop_search > div.db > div.box01")

for n in notices:
	print(n.text.strip())
	contents = n.text.strip() #필요한  텍스트를 contents에 저장 


#페이지 닫기
closer = driver.find_element_by_id('btn_layer_speechall')
closer.send_keys('\n')


#텍스트를 파일로 저장하기
sys.stdout = open('output.txt','w')
print(contents) #print()안의 내용이 output.txt 파일에 저장됨.
