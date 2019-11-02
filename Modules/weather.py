import json
import requests
from bs4 import BeautifulSoup

def sydney():
	r=requests.get('http://reg.bom.gov.au/fwo/IDN60901/IDN60901.94768.json')
	r=(r.json()['observations']['data'][0])
	print("Location: ", r.get("name"))
	print("Time: ", r.get("local_date_time_full"))
	print("TEMP", r.get("local_date_time"))
	print("Temperature: ", r.get("air_temp"))
	print("Pressure: ", r.get("press"))
	print("Humidity: ", r.get("rel_hum"))
	print("Wind Direction: ", r.get("wind_dir"))
	print("Wind Speed:", r.get("wind_spd_kmh"),"KM/H","(",r.get("wind_spd_kt"),"Knots",")")

def forecast():
	source = requests.get('http://www.bom.gov.au/places/nsw/sydney/forecast/').text
	soup = BeautifulSoup(source, 'lxml')
	for summary in soup.find_all('div', class_='day'):
		print(summary.getText())		

def airQuality():
	source = requests.get('https://www.environment.nsw.gov.au/aqms/aqiforecast.htm').text
	soup = BeautifulSoup(source, 'lxml')
	summary = soup.find('body')
	print(summary)

	#https://aqicn.org/city/australia/nsw/rozelle/sydney-east/ - PAST DATA
	#https://www.environment.nsw.gov.au/aqms/aqiforecast.htm - CURRENT LEVEL
	#No idea how to get any info from websites, its all event driven and cant find api for it. its not BOM.
	# Its environment.nsw.gov.au

def warning():
	source = requests.get('http://www.bom.gov.au/nsw/warnings/').text
	soup = BeautifulSoup(source, 'lxml')
	for summary in soup.find_all('div', {'id': 'content'}):
		print(summary.getText())

	#use "ul" tag to filter out other shit

def pollenCount():
	print()

#sydney()
#forecast()
#airQuality()
#warning()
#pollenCount()
