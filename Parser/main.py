import sys
import math as mth
import bs4 as bsoup
import urllib.request
import nflReference as NFL
import lxml
from datetime import datetime
import scraper as Scraper
from pathlib import Path


BASE_URL="https://www.pro-football-reference.com"

def bsoupRequest(url):
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	rawHtml = response.read()
	return bsoup.BeautifulSoup(rawHtml, 'lxml')

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

def getGameInfos(url):
	soup = bsoupRequest(url)

	##Basic infos
	title=soup.title.text
	foo = title.split(' at ');
	visitor=foo[0].strip()
	home=foo[1].split('-')[0].strip()
	print(f'visitor: {visitor}, home: {home}')
	date = getDate(foo[1].split('-')[1].split('|')[0].strip())
	return (NFL.getAcronym(home),NFL.getAcronym(visitor),date)

def scrapeGame(url, dataDir):
	#Receiving Data

	try:
		infos=getGameInfos(url)
		filename=infos[0]+"-"+infos[1]+"-"+infos[2]
		receivingCSV=Scraper.scrape(url)
	except Exception as inst:
		f=open(dataDir + "/errors.log","w+")
		f.write(url)
		f.close()

	#basic Game data
	else:	
		f=open(dataDir+filename,"w+")
		f.write(receivingCSV)
		f.close()

def main(year):
	year_url = BASE_URL + "/years/" + str(year)
	dataDir="../data/" + str(datetime.now()) + "/"
	Path(dataDir).mkdir(parents=True, exist_ok=True)
	for i in range(1,17): #weeks 1-17
		week_url = year_url + "/" + "week_" + str(i) + ".htm" 
		print(week_url)
		soup = bsoupRequest(week_url)
		gameLinks=soup.find_all("td",class_="right gamelink")
		for link in gameLinks:
			url=link.a['href']
			if url is not None:
				scrapeGame(BASE_URL + link.a['href'], dataDir)


if __name__ == "__main__":
    main(2019)
