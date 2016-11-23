from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

#grabs html
html = urlopen('http://www.alabamavotes.gov/electionnight/chooseCounty.aspx?ecode=1000500')
soup = BeautifulSoup(html,'html.parser')

#create a empty list
x = list()
y = list()
#searched through the html to find the text between the <a href> tags
for link in soup.find_all('a'):
	x.append(link.get_text())					#Pulls the text between <a href> tags
	y.append(link.get('href'))					#Pulls the link


#editing the unwanted data out, county names stored in county_names
counties = x[:-7]
counties[0:9]=[]

#editing the unwanted links from the list!
links = y[:-7]
links[0:9]=[]


#WORKS!
#Gives a huge list with 11 entries per counties with vote totals and percentages
numbers = list()	
for link in links:
	html = urlopen("http://www.alabamavotes.gov/electionnight/" + link)
	soup = BeautifulSoup(html,'html.parser')
	dums = soup.find_all('div',class_='numberValue')
	for i in range(0,11):
		numbers.append(dums[i].get_text())


#Sorts it out to make a list of 11 entries, created a list of lists. 
data = list()
for j in range(0,67):
	i = 11*j
	data.append(numbers[0+i:11+i])

#Attach the county name to the associated vote result list
for i in range(len(data)):
	data[i].append(counties[i])


#WRITES TO CSV FILE
with open('test.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(data)
