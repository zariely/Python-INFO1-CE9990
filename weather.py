'''
weather.py

This application pulls the current weather report
from the Yahoo API based on user input

You'll need to install yahooweather and yweather
before running this program.
'''

import sys
import urllib.request
import json
import yweather
from yahooweather import YahooWeather, UNIT_F

client = yweather.Client()

zipcode = str(input("Please enter a 5-digit ZIP code: "))
zipid = client.fetch_woeid(zipcode) #gets the woeid based on the zipcode value

baseURL = "https://query.yahooapis.com/v1/public/yql?"
yqueryString = ("select * from weather.forecast where woeid=" + zipid)


yqueryString = baseURL + urllib.parse.urlencode({'q':yqueryString}) + "&format=json"
result = urllib.request.urlopen(yqueryString).read()
data = json.loads(result)

print("-" * 70)
print("Here's today's weather forecast in", data['query']['results']['channel']['location']['city'])
print("Date:", data['query']['results']['channel']['item']['forecast'][0]['day'],
      data['query']['results']['channel']['item']['forecast'][0]['date'])
print("High:", data['query']['results']['channel']['item']['forecast'][0]['high'])
print("Low:", data['query']['results']['channel']['item']['forecast'][0]['low'])
print(data['query']['results']['channel']['item']['forecast'][0]['text'])

sys.exit(0)
