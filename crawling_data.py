from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import sys

#웹사이트 접속하기
driver = webdriver.Chrome('C:/Users/user/chromedriver')
driver.get('http://ssullog.joins.com/speech/speechList')

#크롤러 생성
text_file = [] #크롤링한 텍스트 데이터 저장
def crawling():
	count = 24713 #태그 번호

	for i in range(50):
		
		#크롤링할 페이지 들어가기
		link = '#speech_no_{} > div.box-header > div > a'.format(count)
		sample = driver.find_element_by_css_selector(link)
		sample.send_keys('\n')
		time.sleep(5)

		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')

		#데이터를 크롤링해 저장하기
		notices = soup.select('#pop_search > div.bd > div.box01')
		text.file.append(notices)


		#페이지 나가기
		tag = '//*[@{}="btn_layer_speechall"]'.format('id')
		closer = driver.find_element_by_xpath(tag)
		closer.send_keys('\n')

		count -= 1
	return text_file
		

#텍스트 데이터를 각 변수에 할당하기
num = 24713
for name in range(len(text_file)):
	globals()['statement{}'.format(num)] = text_file[name]
	num -= 1

#텍스트 데이터를 텍스트 파일로 저장하기
for i in range(len(text_file)):
	sys.stdout = open('statement{}.txt'.format(i), 'w', encoding = 'utf-8')
	print(text_file[i])
	sys.stdout.close()
