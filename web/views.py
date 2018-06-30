from django.shortcuts import render, redirect
from coinmarketcap import Market
from twitter import Twitter
from twython import Twython
from .models import Cryptocurrency, Price

import oauth2
import secrets
import os
#import twitter
#from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#import coinmarketcap
#from requests_oauthlib import OAuth1Session
#import json
#import settings

from django.contrib import auth



# Create your views here.
def home(request):
    coinmarketcap = Market()
    json_result = coinmarketcap.ticker(start=0, limit=10, convert='USD')

    result = []
    for j in json_result:
        result_line = {
            "id": j['id'],
            "name": j['name'],
            "symbol": j['symbol'].lower(),
            "rank": j['rank'],
            "price_usd": j['price_usd'],
            "market_cap_usd": j['market_cap_usd'],
            "percent_change_24h": j['percent_change_24h'],
            "percent_change_7d": j['percent_change_7d'],
        }
        result.append(result_line)

    return render(request, 'home.html',{'result':result})

#def login(request):
#    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    #return render(request, 'home.html')
    return redirect('/')

#how did we define id as a coin name?
def detail(request, id):
#   print(id, 'this is id')
    #coinmarketcap
    coinmarketcap = Market()
    json_result = coinmarketcap.ticker(id, limit=10, convert='USD')
    t = Twython(secrets.TWITTER_APP_KEY,
            secrets.TWITTER_APP_KEY_SECRET,
            secrets.TWITTER_ACCESS_TOKEN,
            secrets.TWITTER_ACCESS_TOKEN_SECRET)
    search = t.search(q='#bitcoin',count=100)
    cryptocurrency = Cryptocurrency.objects.get(name=id)
    #cryptocurrency = Cryptocurrency.objects.get(name=json_result.name)
    #cryptocurrency = Cryptocurrency.objects.filter(name=name)
    print(cryptocurrency, 'this is coin')
    #date = Price.date
    #price = Price.open
    #get,filter,all
    #the next challnge is coin_id=id
    #price1 = Price.objects.all()
    price = Price.objects.filter(coin_id=cryptocurrency.id)
    print(price, 'this is prices')

    tweets = search['statuses']
    #for tweet in tweets:
    #    print(tweet['id_str'], '\n', tweet['text'], '\n\n\n'),'tweet': tweet,, 'date':date, 'price':price
    return render(request, 'detail.html', {'json_result':json_result[0], 'cryptocurrency':cryptocurrency})

    """
    # ...
    twitter = Twitter(
      auth=OAuth(token, token_key, con_secret, con_secret_key))

    api = twitter.Api(consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET)
    home_timeline = api.VerifyCredentials()


    def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
        consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        token = oauth2.Token(key=key, secret=secret)
        client = oauth2.Client(consumer, token)
        resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
        return content

    home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/home_timeline.json', ACCESS_TOKEN, ACCESS_SECRET, "GET", "A" )

    twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    params = {}
    req = twitter.get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = params)

    home_timeline = json.loads(req.text)
    return render(request, 'detail.html', {'json_result':json_result[0], 'home_timeline':home_timeline})
    """
    """
    t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    TWITTER_APP_KEY = os.environ.get('TWITTER_APP_KEY')
    TWITTER_APP_KEY_SECRET = os.environ.get('TWITTER_APP_KEY_SECRET')
    TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    """

#print(result)
