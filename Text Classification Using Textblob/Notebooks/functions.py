import demoji
import re
import requests
from textblob import TextBlob as tb
demoji.download_codes()


#Function using Google Place API to identify countries
def google_api(place_name):
    API_KEY = 'AIzaSyB0VRPrmKiOf-aPVTGMHIkv-jPLMYdMhWs'
    place_name = place_name.strip()
    r = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='+place_name+'&inputtype=textquery&key='+API_KEY)
    while True:
        try:
            placeid = r.json()['candidates'][0]['place_id']
            r_place = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeid+'&key='+API_KEY)
        #print(r_place.json())
            nation_state = r_place.json()['result']['address_components']
            for part in nation_state:
                if part['types'][0]=='country':
                    country_name = part['long_name']
                    return country_name
        except IndexError:
            country_name = 'Unknown'
            return country_name



# preprocessing function. To remove RTs, handle names and hashtags along with text
def data_cleaner(column):
    column = column.apply(lambda x: demoji.replace(str(x),''))
    column = column.apply(lambda x:re.sub('RT @[\w_]+: ', ' ',str(x)))
    return column

# preprocessing function. To remove RTs, handle names and hashtags along with text
def data_cleaner_tweets(column):
    pattern = re.compile('RT @[\w_]+: |https?:\/\/.*[\r\n]*|[^A-Za-z0-9]+')
    column = column.apply(lambda x: demoji.replace(str(x),''))
    column = column.apply(lambda x:re.sub(pattern, ' ',str(x)))
    #column = column.apply(lambda x:re.sub('[^A-Za-z0-9]+',' ',x))
    #column = column.apply(lambda x:re.sub('[^A-Za-z0-9]+',' ',x))
    return column

#Sentiment classifer
def opinion(string):
    blob = tb(string)
    if blob.polarity >0.3:
        return 'Positive'
    elif blob.polarity < -0.3:
        return 'Negative'
    else:
        return 'Neutral'
