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

day = data['query']['results']['channel']['item']['forecast'][0]['day']
date = data['query']['results']['channel']['item']['forecast'][0]['date']
city = data['query']['results']['channel']['location']['city']
state = data['query']['results']['channel']['location']['region']
high = data['query']['results']['channel']['item']['forecast'][0]['high']
low = data['query']['results']['channel']['item']['forecast'][0]['low']
text = data['query']['results']['channel']['item']['forecast'][0]['text']


print("-" * 70)
print("Here's today's weather forecast in {},{}:".format(city, state))
print("Date:", day, date)
print("High: {}°F".format(high))
print("Low: {}°F".format(low))
print(text)

sys.exit(0)
