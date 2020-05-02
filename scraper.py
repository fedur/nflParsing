from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def count(x):
	totalCount=x
	while(totalCount>0):
		time.sleep(1)
		print(totalCount)
		totalCount -= 1


def scrape(url):
	def findDiv(driver):
		return driver.find_element_by_xpath("//div[@id='all_receiving_advanced']//ul/li")
	options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(chrome_options=options)
	driver.get(url)
	menu = WebDriverWait(driver, 5).until(findDiv)
	ActionChains(driver).move_to_element(menu).send_keys(Keys.PAGE_DOWN).perform()
	count(1)
	ActionChains(driver).move_to_element(menu).move_by_offset(0,100).click().perform()
	csvData = driver.find_element_by_id("csv_receiving_advanced")
	return csvData.text