from bs4 import BeautifulSoup
import urllib2 # I'm using Python 2.7 and so it's urllib2 for me
import csv
import json

# Define the fields to be extracted at the county level
# HAS TO MATCH ORDERING FLAGGED BELOW
field_defs = [
	'HRC (%)', 'HRC (raw votes)',
	'DJT (%)', 'DJT (raw votes)',
	'GJ (%)', 'GJ (raw votes)',
	'JS (%)', 'JS (raw votes)',
	'Write-in (%)', 'Write-in (raw votes)',
	'Total Votes'
]

# allCountyData: stores data for all counties
allCountyData = []

# Starting URL Data
html = urllib2.urlopen('http://www.alabamavotes.gov/electionnight/chooseCounty.aspx?ecode=1000500')
soup = BeautifulSoup(html,'html.parser')

# Loop through each individual county link
for a in soup.select('strong a'):

	# thisCountyData: temporary storage for single county data
	thisCountyData = {'County Name': a.get_text()}

	# Get detailed county data
	h = urllib2.urlopen("http://www.alabamavotes.gov/electionnight/" + a['href'])
 	s = BeautifulSoup(h,'html.parser')

	# !!!!!! THIS IS WHERE THE ORDERING FOR field_defs COMES FROM !!!!!!
	# Extract fields, using labels as defined above in field_defs
	for i,val in enumerate(s.find_all('div',class_='numberValue')[0:11]):
		rawVal = val.get_text()

		# Convert values to numbers to ensure proper JSON output formatting later on
		if '%' in rawVal:
			processedVal = round(float(rawVal.replace('%',''))/100,4);
		else:
			processedVal = int(rawVal.replace(',',''))

		# Write data point
		thisCountyData[field_defs[i]] = processedVal

	# Add this county's data to allCountyData
	allCountyData.append(thisCountyData)

# Write as CSV
with open('AL_CountyLevelResults.csv', 'w') as csv_fs:
	writer = csv.DictWriter(csv_fs, ['County Name']+field_defs)
	writer.writeheader()
	writer.writerows(allCountyData)

# Write as JSON
with open('AL_CountyLevelResults.json', 'w') as json_fs:
	json_fs.write(json.dumps(allCountyData,indent=1,sort_keys=True))	
