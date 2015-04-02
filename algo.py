#to-do - google finance python api integration
# resources - http://nsetools.readthedocs.org/en/latest/introduction.html
# https://code.google.com/p/yahoo-finance-managed/wiki/YahooFinanceAPIs
import urllib2, urllib, json
 
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind from weather.forecast where woeid=2460286"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
 
print data['query']['results']