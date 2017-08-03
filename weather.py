'''
weather.py

This application pulls the current weather report
from the Yahoo API based on user input

You'll need to install yahooweather before running this program.
'''

import sys, urllib.request, json, yweather
from yahooweather import YahooWeather, UNIT_F

client = yweather.Client()
zipcode = str(input("Please enter a 5-digit ZIP code: "))
zipid = client.fetch_woeid(zipcode) #gets the woeid based on the zipcode value

baseURL = "https://query.yahooapis.com/v1/public/yql?"
yqueryString = ("select * from weather.forecast where woeid=" + zipid)

yqueryString = baseURL + urllib.parse.urlencode({'q':yqueryString}) + "&format=json"
result = urllib.request.urlopen(yqueryString).read()
data = json.loads(result)

location = data['query']['results']['channel']['location']
city = location['city']
state = location['region']
forecast = data['query']['results']['channel']['item']['forecast'][0]
day = forecast['day']
date = forecast['date']
high = forecast['high']
low = forecast['low']
text = forecast['text']

print("-" * 70)
print("Here's today's weather forecast in {},{}".format(city, state))
print("\tDate:", day, date)
print("\tHigh: {}°F".format(high))
print("\tLow: {}°F".format(low))
print("\tConditions: {}".format(text))

sys.exit(0)
