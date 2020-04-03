import sys
import math as mth
import bs4 as bsoup
import urllib.request
import nflReference as NFL
import html5lib
import lxml
from datetime import datetime
import scraper as Scraper

def getDate(str):
	#Format =: September 9th, 2019
	#9th becomes 9
	foo=str.split()[1]
	day=foo[0].join(i for i in foo if i.isdigit())
	if (len(day)==1):
		day = "0" + day
	date = str.replace(foo,day)
	dtime_obj = datetime.strptime(date, '%B %d %Y')
	return dtime_obj.strftime('%d_%m_%Y')

def scrapeTeamnames(url):
	print("lala")
	#req = urllib.request.Request(url)
	#response = urllib.request.urlopen(req)
	#rawHtml = response.read()
	#soup = bsoup.BeautifulSoup(rawHtml, 'lxml')
	#print(soup.find_all(id="csv_rushing_advanced"))

	##Basic infos
	#title=soup.title.text
	#foo = title.split(' at ');
	#visitor=foo[0].strip()
	#home=foo[1].split('-')[0].strip()
	#date = getDate(foo[1].split('-')[1].split('|')[0].strip())

	##Receiving_csv
	#receivingDiv = soup.find("div", id="all_receiving_advanced")
	#print(receivingDiv)
	#foo=receivingDiv.find("div",class_="section_heading_text")
	#foo=foo.find("ul")
	#print(soup.find_all(class_="hasmore"))


def scrape(url):
	print (Scraper.scrape(url))

def main(year):
	scrape('https://www.pro-football-reference.com/boxscores/201909080nwe.htm')

if __name__ == "__main__":
    main(1111)
