from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

def scrape(url):
	def findDiv(driver):
		return driver.find_element_by_xpath("//div[@id='all_receiving_advanced']//ul/li")

	driver = webdriver.Chrome()
	driver.get(url)
	element = WebDriverWait(driver, 10).until(findDiv)
	return element.text;
	